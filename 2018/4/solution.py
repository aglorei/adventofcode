from collections import defaultdict
from datetime import datetime
import fileinput
import re

class SleepSchedule:
    def __init__(self):
        self.totals = defaultdict(int)
        self.minutes = defaultdict(lambda: defaultdict(int))
        for line in self.lines():
            if 'Guard' in line:
                guard = self.parse_guard(line)
            elif 'falls asleep' in line:
                start = self.parse_minute(line)
            elif 'wakes up' in line:
                for minute in range(start, self.parse_minute(line)):
                    self.totals[guard] += 1
                    self.minutes[guard][minute] += 1

    def lines(self):
        for line in sorted(fileinput.input(), key=self.parse_timestamp):
            yield line.strip()

    def part1(self):
        best = max(self.totals, key=self.totals.get)
        minute = max(self.minutes[best], key=self.minutes[best].get)
        return best * minute

    def part2(self):
        best = max(self.max_counts, key=self.max_counts.get)
        minute = self.max_minutes[best]
        return best * minute

    @property
    def max_counts(self):
        return {k: v[max(v, key=v.get)] for k, v in self.minutes.items()}

    @property
    def max_minutes(self):
        return {k: max(v, key=v.get) for k, v in self.minutes.items()}

    @staticmethod
    def parse_guard(line):
        return int(re.findall(r'\d+', line[19:])[0])

    @staticmethod
    def parse_minute(line):
        return int(line[15:17])

    @staticmethod
    def parse_timestamp(line):
        pattern = '%Y-%m-%d %H:%M'
        return datetime.strptime(line[1:17], pattern)

def main():
    sleep_schedule = SleepSchedule()
    print(sleep_schedule.part1())
    print(sleep_schedule.part2())

if __name__ == '__main__':
    main()
