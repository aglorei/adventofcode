import fileinput
import itertools

def lines():
    for line in fileinput.input():
        yield line

def part1(frequencies, start=0):
    return start + sum(map(int, frequencies))

def part2(frequencies, start=0):
    seen = {start}
    for i in itertools.cycle(frequencies):
        start += int(i)
        if start in seen:
            return start
        seen.add(start)

def main():
    print(part1(lines()))
    print(part2(lines()))

if __name__ == '__main__':
    main()
