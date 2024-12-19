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


def find_space(data: list[int | None], size: int, end: int) -> int | None:
    start_index = None
    space = 0
    for i, element in enumerate(data):
        if element == None:
            if start_index == None:
                start_index = i
            space += 1
            if space == size:
                if start_index < end:
                    return start_index
                else:
                    return None
        else:
            start_index = None
            space = 0

    return None


def find_next_id(data: list[int | None], seen_ids: list[int]) -> int | None:
    current_id = None
    for i in range(len(data)):
        if data[i] != None and data[i] not in seen_ids:
            current_id = data[i]

    return current_id


def compact(data: list) -> list:
    seen_ids = []
    current_id = None

    iterations = 0
    # this has got to be soooo ineffecicient, I'm looping through this array so many times
    while True:
        iterations += 1
        print(iterations)

        current_id = find_next_id(data, seen_ids)
        if current_id == None:
            break

        seen_ids.append(current_id)

        size = data.count(current_id)

        index = find_space(data, size, data.index(current_id))
        if index == None:
            continue

        for i in range(len(data)):
            if data[i] == current_id:
                data[i] = None

        for i in range(index, index + size):
            data[i] = current_id


    return data


def get_check_sum(disk: list) -> int:
    total = 0
    for i in range(len(disk)):
        if disk[i] != None:
            total += i * disk[i]

    return total


def main():
    disk: str = ""

    with open("input.txt", "r") as file:
        for line in file:
            disk += line.strip()

    expanded_disk: list[int | None] = expand(disk)

    compacted_disk: list[int | None] = compact(expanded_disk)

    print(get_check_sum(compacted_disk))


if __name__ == "__main__":
    main()
