import fileinput

def line():
    return [line.strip() for line in fileinput.input()][0]

def react(polymer, ignore=''):
    result = ['']
    for char in polymer:
        if char in ignore:
            continue
        if char.swapcase() == result[-1]:
            result.pop()
        else:
            result += char
    return ''.join(result)

def part1():
    polymer = line()
    done = False
    while not done:
        reacted = react(polymer)
        if polymer == reacted:
            done = True
        else:
            polymer = reacted
    return len(polymer)

def part2():
    polymer = line()
    units = set(polymer.upper())
    lowest = len(polymer)
    for char in units:
        ignore = char+char.swapcase()
        lowest = min(lowest, len(react(polymer, ignore)))
    return lowest

def main():
    print(part1())
    print(part2())

if __name__ == '__main__':
    main()
