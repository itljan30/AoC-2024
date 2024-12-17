UP = (0, -1)
UP_RIGHT = (1, -1)
RIGHT = (1, 0)
DOWN_RIGHT = (1, 1)
DOWN = (0, 1)
DOWN_LEFT = (-1, 1)
LEFT = (-1, 0)
UP_LEFT = (-1, -1)


def XMAScount(wordsearch: list[str], x: int, y: int) -> int:
    matches = 0

    for direction in [UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT]:
        word = ""
        for i in range(4):
            nx = x + direction[0] * i
            ny = y + direction[1] * i

            if 0 <= ny < len(wordsearch) and 0 <= nx < len(wordsearch[x]):
                word += wordsearch[ny][nx]

        if word == "XMAS":
            matches += 1

    return matches


def main():
    wordsearch = []

    with open("input.txt", "r") as file:
        for line in file:
            wordsearch.append(line.strip())

    total = 0
    for y, line in enumerate(wordsearch):
        for x, char in enumerate(line):
            if char == "X":
                total += XMAScount(wordsearch, x, y)

    print(total)


if __name__ == "__main__":
    main()
