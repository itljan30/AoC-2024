def XMAScount(wordsearch: list[str], x: int, y: int) -> int:
    word1 = ""
    word2 = ""
    
    # \
    nx = x - 1
    ny = y - 1
    if not 0 <= ny < len(wordsearch) or not 0 <= nx < len(wordsearch[x]):
        return 0
    word1 += wordsearch[ny][nx]

    word1 += wordsearch[y][x]

    nx = x + 1
    ny = y + 1
    if not 0 <= ny < len(wordsearch) or not 0 <= nx < len(wordsearch[x]):
        return 0
    word1 += wordsearch[ny][nx]

    # /
    nx = x - 1
    ny = y + 1
    if not 0 <= ny < len(wordsearch) or not 0 <= nx < len(wordsearch[x]):
        return 0
    word2 += wordsearch[ny][nx]

    word2 += wordsearch[y][x]

    nx = x + 1
    ny = y - 1
    if not 0 <= ny < len(wordsearch) or not 0 <= nx < len(wordsearch[x]):
        return 0
    word2 += wordsearch[ny][nx]

    if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM"):
        return 1

    return 0


def main():
    wordsearch = []

    with open("input.txt", "r") as file:
        for line in file:
            wordsearch.append(line.strip())

    total = 0
    for y, line in enumerate(wordsearch):
        for x, char in enumerate(line):
            if char == "A":
                total += XMAScount(wordsearch, x, y)

    print(total)


if __name__ == "__main__":
    main()
