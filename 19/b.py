# IDEA if we split the target into substrings that are the length of the longest given substring
# or less, we would could probably brute force the other way a lot easier. I don't know exactly
# how the brute forcing the other way would be, but I think it would be way more efficient maybe?


import copy


def find_matches(patterns: list[str], target: str, current_pattern: str) -> int:
    total = 0
    for pattern in patterns:
        if current_pattern == target:
            return 1

        if len(current_pattern) > len(target):
            return 0

        potential_pattern = copy.copy(current_pattern) + pattern

        print(potential_pattern)

        if not target.startswith(potential_pattern):
            continue

        total += find_matches(patterns, target, potential_pattern)

    return total


def main():
    patterns = []
    targets = []

    with open("input.txt", "r") as file:
        for line in file:
            if ',' in line:
                patterns += line.split(', ')
            elif line != '\n':
                targets.append(line.strip())

    total = 0
    for target in targets:
        subtotal = find_matches(patterns, target, "")
        print(subtotal)
        total += subtotal

    print(total)


if __name__ == "__main__":
    main()
