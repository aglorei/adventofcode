from collections import defaultdict
import fileinput

def lines():
    return list(map(parse_coordinate, fileinput.input()))

def parse_coordinate(line):
    return tuple(map(int, line.strip().split(', ')))

def distance(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))

def distance_collection(origin, coordinates):
    enum = enumerate(coordinates)
    return sorted((distance(origin, (cx, cy)), (cx, cy)) for i, (cx, cy) in enum)

def part1():
    coordinates = lines()
    counts = defaultdict(int)
    perimeter = set()
    x_min, x_max = min(x for x, y in coordinates), max(x for x, y in coordinates)
    y_min, y_max = min(y for x, y in coordinates), max(y for x, y in coordinates)
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            distances = distance_collection((x, y), coordinates)
            if distances[0][0] != distances[1][0]:
                counts[distances[0][1]] += 1
                if x == x_min or x == x_max or y == y_min or y == y_max:
                    perimeter.add(distances[0][1])
    for coordinate in perimeter:
        counts.pop(coordinate)
    return max(counts.values())

def main():
    print(part1())

if __name__ == '__main__':
    main()
