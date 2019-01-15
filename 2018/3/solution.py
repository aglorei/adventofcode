from collections import defaultdict
import fileinput
import re

def lines():
    for line in fileinput.input():
        yield line.strip()

def part1():
    claims = defaultdict(set)
    for line in lines():
        claim, x, y, w, h = map(int, re.findall(r'\d+', line))
        for i in range(x, x + w):
            for j in range(y, y + h):
                claims[(i, j)].add(claim)
    return sum(len(value) > 1 for value in claims.values())


def main():
    print(part1())

if __name__ == '__main__':
    main()
