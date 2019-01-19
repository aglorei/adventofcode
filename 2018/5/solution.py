import fileinput

def line():
    return [line.strip() for line in fileinput.input()][0]

def part1():
    polymer = list(line())
    done = False
    while not done:
        reactives = []
        for i in range(len(polymer)-1):
            if i in reactives:
                continue
            if polymer[i].swapcase() == polymer[i+1]:
                reactives += [i, i+1]
        if reactives:
            for i in reactives[::-1]:
                polymer.pop(i)
        else:
            done = True
    return len(polymer)

def main():
    print(part1())

if __name__ == '__main__':
    main()
