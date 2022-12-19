class Valve:
    def __init__(self, name: str, rate: int, neighbours: list[str]) -> None:
        self.name = name
        self.rate = rate
        self.neighbours = neighbours

    def __str__(self) -> str:
        return f'valve: {self.name}, rate: {self.rate}, neighbours: {self.neighbours}'

def parseInput():
    valves = {}
    with open('input.in', 'r') as reader:
        line = reader.readline()

        while line != '':
            valvePart, tunnelPart = line.strip().split('; ')
            splitted = valvePart.split(' ')
            valveName = splitted[1]
            valveRate = int(splitted[-1].split('=')[-1])

            tunnels = tunnelPart.replace(',', '').split()[4:]
            valve = Valve(valveName, valveRate, tunnels)
            # print(valve)

            valves[valveName] = valve
        
            line = reader.readline()
    
    return valves

def findDistances(valves: dict):
    keyValves = {valveName for valveName in valves if valves[valveName].rate > 0 or valveName == 'AA'}
    distances = {}

    for startValve in valves:
        if startValve not in keyValves:
            continue
        
        curr = set([startValve])
        next = set()
        dist = 0
        distances[(startValve, startValve)] = 0

        while curr:
            dist += 1
            for valve in curr:
                for newpos in valves[valve].neighbours:
                    if (startValve, newpos) not in distances:
                        distances[(startValve, newpos)] = dist
                        next.add(newpos)

            curr, next = next, set()

    return distances, keyValves

def getMaxFlow(valves: dict, distances, keyValves):
    def find_best_total_flow(cur="AA", time=30, seen=set(), targets=keyValves):
        seen = seen | {cur}
        targets = targets - seen

        maxPressure = 0
        for target in targets:
            # we move to target and open it
            time_left = time - distances[(cur, target)] - 1
            if time_left > 0:
                flow = valves[target].rate * time_left
                flow += find_best_total_flow(target, time_left, seen, targets)
                maxPressure = max(maxPressure, flow)

        return maxPressure
    
    print("Part 1:", find_best_total_flow())

def part2(valves: dict, distances, keyValves):
    # Finds the best flow rate for a certain set of valves
    endpoints = {}

    def find_and_record(cur="AA", curflow=0, time=26, seen=set()):
        seen = seen | {cur}
        targets = keyValves - seen

        torecord = frozenset(seen - {"AA"})
        
        if torecord not in endpoints:
            endpoints[torecord] = 0
        
        endpoints[torecord] = max(endpoints[torecord], curflow)

        maxPressure = 0
        for target in targets:
            time_left = time - distances[(cur, target)] - 1
            if time_left > 0:
                newflow = valves[target].rate * time_left
                newflow += find_and_record(target, curflow + newflow, time_left, seen)
                maxPressure = max(maxPressure, newflow)

        return maxPressure

    find_and_record()

    # Then fill in all the missing endpoints. The goal is to know the best 
    # flow rate to get if you 'control' a certain set of key rooms
    def fill_in_endpoints(cur=frozenset(keyValves - {"AA"})):
        if cur not in endpoints:
            best_flow = 0
            for e in cur:
                subset = cur - {e}
                new_flow = fill_in_endpoints(subset)
                best_flow = max(best_flow, new_flow)
            endpoints[cur] = best_flow
        return endpoints[cur]
    
    fill_in_endpoints()

    # Now we iterate over all the possible assignments of keyValves to 
    # human or elephant, adding together their scores.
    best_flow = 0
    for human_work in endpoints:
        elephant_work = frozenset(keyValves - {"AA"} - human_work)
        total_flow = endpoints[human_work] + endpoints[elephant_work]
        best_flow = max(best_flow, total_flow)
    print("Part 2:", best_flow)

def main():
    valves = parseInput()
    distances, keyValves = findDistances(valves)
    # res = getMaxFlow(valves, distances, keyValves)
    part2(valves, distances, keyValves)

if __name__ == "__main__":
    main()