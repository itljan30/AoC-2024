# NOTE not solved, I need to calculate each patch of same plant separately, woops


def calculate_area(garden: list[list[str]], plant: str) -> int:
    total = 0
    for row in garden:
        total += row.count(plant)

    return total


def calculate_perimeter(garden: list[list[str]], plant: str) -> int:
    RIGHT = ( 1,  0)
    LEFT  = (-1,  0)
    DOWN  = ( 0,  1)
    UP    = ( 0, -1)

    total = 0
    for i, row in enumerate(garden):
        for j, cell in enumerate(row):
            if cell == plant:
                for direction in [RIGHT, LEFT, DOWN, UP]:
                    if not 0 <= i + direction[1] < len(garden) or not 0 <= j + direction[0] < len(row):
                        total += 1
                        continue
                    if garden[i + direction[1]][j + direction[0]] != plant:
                        total += 1
            
    return total


def main():
    garden: list[list[str]] = []
    plants: list[str] = []

    with open("in.txt", "r") as file:
        for line in file:
            row: list[str] = []
            for char in line.strip():
                if char not in plants:
                    plants.append(char)
                row.append(char)
            garden.append(row)

    total_cost: int = 0
    for plant in plants:
        area = calculate_area(garden, plant)
        perimeter = calculate_perimeter(garden, plant)
        cost = perimeter * area
        print(f"{plant}: {area} * {perimeter} = {cost}")
        total_cost += cost

    print(total_cost)

if __name__ == "__main__":
    main()
