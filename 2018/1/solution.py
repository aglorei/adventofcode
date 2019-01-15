import fileinput
import itertools

def lines():
    for line in fileinput.input():
        yield line.strip()

def part1():
    return sum(map(int, lines()))

def part2():
    start = 0
    seen = {start}
    for i in itertools.cycle(lines()):
        start += int(i)
        if start in seen:
            return start
        seen.add(start)
    return None

def main():
    print(part1())
    print(part2())

if __name__ == '__main__':
    main()
