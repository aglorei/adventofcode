import fileinput

def line():
    return next(fileinput.input()).strip()

def react(polymer):
    result = ['']
    for char in polymer:
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

def main():
    print(part1())

if __name__ == '__main__':
    main()
