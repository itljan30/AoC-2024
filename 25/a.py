# keys/locks are 5 x 7

def compatible(key: list[int], lock: list[int]):
    for i in range(5):
        if key[i] + lock[i] > 7:
            return False

    return True


def main():
    keys: list[list[int]] = []
    locks: list[list[int]] = []
    
    key = False
    lock = False
    col1 = 0
    col2 = 0
    col3 = 0
    col4 = 0
    col5 = 0
    with open("input.txt", "r") as file:
        for i, line in enumerate(file):
            if lock == False and key == False:
                if '#' in line:
                    lock = True
                else:
                    key = True

            if line == "\n":
                item = []
                item.append(col1)
                item.append(col2)
                item.append(col3)
                item.append(col4)
                item.append(col5)
                if key:
                    keys.append(item)
                else:
                    locks.append(item)
                
                lock = False
                key = False
                col1 = 0
                col2 = 0
                col3 = 0
                col4 = 0
                col5 = 0
                continue

            if line[0] == '#':
                col1 += 1
            if line[1] == '#':
                col2 += 1
            if line[2] == '#':
                col3 += 1
            if line[3] == '#':
                col4 += 1
            if line[4] == '#':
                col5 += 1

            if i == 3998:
                item = []
                item.append(col1)
                item.append(col2)
                item.append(col3)
                item.append(col4)
                item.append(col5)
                if key:
                    keys.append(item)
                else:
                    locks.append(item)
                
                lock = False
                key = False
                col1 = 0
                col2 = 0
                col3 = 0
                col4 = 0
                col5 = 0

    total: int = 0
    for key in keys:
        for lock in locks:
            if compatible(key, lock):
                total += 1

    print(total)


if __name__ == "__main__":
    main()
