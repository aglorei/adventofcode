from collections import defaultdict
from datetime import datetime
import fileinput
import re

def lines():
    for line in sorted(fileinput.input(), key=parse_timestamp):
        yield line.strip()

def parse_guard(line):
    return int(re.findall(r'\d+', line[19:])[0])

def parse_minute(line):
    return int(line[15:17])

def parse_timestamp(line):
    pattern = '%Y-%m-%d %H:%M'
    return datetime.strptime(line[1:17], pattern)

def part1():
    totals = defaultdict(int)
    minutes = defaultdict(lambda: defaultdict(int))
    for line in lines():
        if 'Guard' in line:
            guard = parse_guard(line)
        elif 'falls asleep' in line:
            start = parse_minute(line)
        elif 'wakes up' in line:
            for minute in range(start, parse_minute(line)):
                totals[guard] += 1
                minutes[guard][minute] += 1
    best = max(totals, key=totals.get)
    minute = max(minutes[best], key=minutes[best].get)
    return best * minute

def part2():
    minutes = defaultdict(lambda: defaultdict(int))
    for line in lines():
        if 'Guard' in line:
            guard = parse_guard(line)
        elif 'falls asleep' in line:
            start = parse_minute(line)
        elif 'wakes up' in line:
            for minute in range(start, parse_minute(line)):
                minutes[guard][minute] += 1
    max_counts = {k: v[max(v, key=v.get)] for k, v in minutes.items()}
    max_minutes = {k: max(v, key=v.get) for k, v in minutes.items()}
    best = max(max_counts, key=max_counts.get)
    minute = max_minutes[best]
    return best * minute

def main():
    print(part1())
    print(part2())

if __name__ == '__main__':
    main()
