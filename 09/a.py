def expand(data: str) -> list[int | None]:
    id = 0
    disk = []

    for i in range(len(data)):
        if i % 2 != 0:
            continue
        for _ in range(int(data[i])):
            disk.append(id)

        if i + 1 < len(data):
            for _ in range(int(data[i+1])):
                disk.append(None)
        
        id += 1

    return disk


def compact(data: list[int | None], lo=0, hi=None) -> list:
    lo = 0
    hi = len(data) - 1
    
    while True:
        while data[lo] != None:
            lo += 1

        while data[hi] == None:
            hi -= 1

        if hi <= lo:
            break

        data[lo] = data[hi]
        data[hi] = None

    return [x for x in data if x != None]
    


def get_check_sum(disk: list[int]) -> int:
    total = 0
    for i in range(len(disk)):
        total += i * disk[i]

    return total


def main():
    disk: str = ""

    with open("input.txt", "r") as file:
        for line in file:
            disk += line.strip()

    expanded_disk: list[int | None] = expand(disk)

    compacted_disk: list[int] = compact(expanded_disk)

    print(get_check_sum(compacted_disk))


if __name__ == "__main__":
    main()
