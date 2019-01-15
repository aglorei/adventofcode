from collections import defaultdict
import fileinput
import re

def lines():
    for line in fileinput.input():
        yield line.strip()

def claims_dict():
    claims = defaultdict(set)
    for line in lines():
        claim, x, y, w, h = map(int, re.findall(r'\d+', line))
        for i in range(x, x + w):
            for j in range(y, y + h):
                claims[(i, j)].add(claim)
    return claims

def part1():
    return sum(len(value) > 1 for value in claims_dict().values())

def part2():
    values = claims_dict().values()
    singles = set.union(*[value for value in values if len(value) == 1])
    overlaps = set.union(*[value for value in values if len(value) > 1])
    return (singles - overlaps).pop()

def main():
    print(part1())
    print(part2())

if __name__ == '__main__':
    main()
