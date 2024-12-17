def is_valid(rule: list[str], update: list[str]) -> bool:
    second = False
    for number in update:
        if rule[0] == number:
            if second == True:
                return False
        elif rule[1] == number:
            second = True
    
    return True


def swap_invalid(rule: list[str], update: list[str]):
    first = update.index(rule[0])
    second = update.index(rule[1])
    update[first], update[second] = update[second], update[first]


def main():
    rules = []
    updates = []

    with open("input.txt", "r") as file:
        for line in file:
            if '|' in line:
                rules.append(line.strip().split('|'))
            else:
                updates.append(line.strip().split(','))

    invalid_updates = []

    finished = False
    while not finished:
        finished = True;
        for update in updates:
            for rule in rules:
                if not is_valid(rule, update):
                    if update not in invalid_updates:
                        invalid_updates.append(update)
                    swap_invalid(rule, update)
                    finished = False

    total = 0
    for update in invalid_updates:
        total += int(update[len(update) // 2])
    
    print(total)


if __name__ == "__main__":
    main()
