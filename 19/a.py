# NOTE I used this to write to a file that only had the strings with solutions
# then changed my input.txt to only have those


import copy
import time


def find_matches(patterns: list[str], target: str, current_pattern: str, start) -> bool:
    successful = False
    for pattern in patterns:
        if time.time() - start > .01:
            return False

        if current_pattern == target:
            return True

        if successful:
            return True

        if len(current_pattern) > len(target):
            return False

        potential_pattern = copy.copy(current_pattern) + pattern

        if not target.startswith(potential_pattern):
            continue

        successful = find_matches(patterns, target, potential_pattern, start)

    return False


def main():
    patterns = []
    targets = []

    with open("input.txt", "r") as file:
        for line in file:
            if ',' in line:
                patterns += line.split(', ')
            elif line != '\n' and not line.startswith('//'):
                targets.append(line.strip())

    total = 0
    with open("output.txt", "w") as file:
        for target in targets:
            print(f"Checking: {target}")
            if find_matches(patterns, target, "", time.time()):
                file.write(f"{target}\n")
                total += 1

    print(total)


if __name__ == "__main__":
    main()
