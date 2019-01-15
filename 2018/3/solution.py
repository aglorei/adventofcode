from collections import Counter
import fileinput

def lines():
    for line in fileinput.input():
        yield line.strip()

def part1():
    claimed = []
    for line in lines():
        edge, dimensions = line.split()[2:]
        edge = tuple(map(int, edge[:-1].split(',')))
        dimensions = tuple(map(int, dimensions.split('x')))
        for x_coordinate in range(dimensions[0]):
            for y_coordinate in range(dimensions[1]):
                claimed.append(tuple([sum(n) for n in zip(edge, [x_coordinate, y_coordinate])]))
    return len([coordinate for coordinate, count in Counter(claimed).items() if count > 1])


def main():
    print(part1())

if __name__ == '__main__':
    main()
