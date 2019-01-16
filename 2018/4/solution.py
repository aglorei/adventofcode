from collections import defaultdict
from datetime import datetime
import fileinput
import re

def lines():
    for line in sorted(fileinput.input(), key=prase_timestamp):
        yield line.strip()

def parse_guard(line):
    return int(re.findall(r'\d+', line[19:])[0])

def parse_minute(line):
    return int(line[15:17])

def prase_timestamp(line):
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

def main():
    print(part1())

if __name__ == '__main__':
    main()
