import re


def mult(x, y):
    return x * y


def main():
    matches = []

    # can probably do something with .split() or something but I can't think right now
    with open("input.txt", "r") as file:
        for line in file:

            # should be a list of all matches in a form like [(3, 5), (51, 3), (999, 53)]
            matches += re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)

    total = 0
    for numbers in matches:
        total += mult(int(numbers[0]), int(numbers[1]))

    print(total)


if __name__ == "__main__":
    main()
