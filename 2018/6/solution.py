from collections import defaultdict
import fileinput

class ChronalCoordinates:
    def __init__(self):
        self.points = list(map(self.parse_coordinate, fileinput.input()))
        self.x_min = min(x for x, y in self.points)
        self.x_max = max(x for x, y in self.points)
        self.y_min = min(y for x, y in self.points)
        self.y_max = max(y for x, y in self.points)
        self.distance_maps = {c: self.sorted_distances(c) for c in self.coordinates()}

    def part1(self):
        counts = defaultdict(int)
        for dmap in self.distance_maps.values():
            if dmap[0][0] != dmap[1][0]:
                counts[dmap[0][1]] += 1
        for c in self.perimeter:
            counts.pop(c)
        return max(counts.values())

    def part2(self, threshold=10000):
        count = 0
        for dmap in self.distance_maps.values():
            if sum(d for d, c in dmap) < threshold:
                count += 1
        return count

    def coordinates(self):
        for x in range(self.x_min, self.x_max+1):
            for y in range(self.y_min, self.y_max+1):
                yield (x, y)

    def is_perimeter(self, coordinate):
        return (coordinate[0] == self.x_min
                or coordinate[0] == self.x_max
                or coordinate[1] == self.y_min
                or coordinate[1] == self.y_max)

    def sorted_distances(self, coordinate):
        enum = enumerate(self.points)
        return sorted((self.distance(coordinate, (cx, cy)), (cx, cy)) for i, (cx, cy) in enum)

    @property
    def perimeter(self):
        return set(self.distance_maps[c][0][1] for c in self.distance_maps if self.is_perimeter(c))

    @staticmethod
    def parse_coordinate(line):
        return tuple(map(int, line.strip().split(', ')))

    @staticmethod
    def distance(a, b):
        return sum(abs(x-y) for x, y in zip(a, b))

def main():
    chronal_coordinates = ChronalCoordinates()
    print(chronal_coordinates.part1())
    print(chronal_coordinates.part2())

if __name__ == '__main__':
    main()
