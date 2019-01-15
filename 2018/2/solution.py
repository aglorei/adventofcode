from collections import Counter
import fileinput

def lines():
    for line in fileinput.input():
        yield line.strip()

def part1():
    twice = 0
    thrice = 0
    for line in lines():
        counts = Counter(line).values()
        twice += 2 in counts
        thrice += 3 in counts
    return twice * thrice

def part2():
    _lines = list(lines())
    for i in range(len(_lines[0])):
        candidates = [line[:i] + line[i+1:] for line in _lines]
        dupes = [line for line, count in Counter(candidates).items() if count > 1]
        if dupes:
            return dupes[0]
    return ''

def main():
    print(part1())
    print(part2())

if __name__ == '__main__':
    main()
