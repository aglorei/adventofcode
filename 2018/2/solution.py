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

def main():
    print(part1())

if __name__ == '__main__':
    main()
