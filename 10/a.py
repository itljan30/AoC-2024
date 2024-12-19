class Cell:
    def __init__(self, value: int, x: int, y: int):
        self.value = value
        self.x = x
        self.y = y


def get_neighbors(cells: list[Cell], current_cell: Cell) -> list[Cell]:
    neighbors: list[Cell] = []

    for cell in cells:
        if cell.x == current_cell.x - 1 and cell.y == current_cell.y:
            neighbors.append(cell)
        elif cell.x == current_cell.x + 1 and cell.y == current_cell.y:
            neighbors.append(cell)
        elif cell.x == current_cell.x and cell.y == current_cell.y - 1:
            neighbors.append(cell)
        elif cell.x == current_cell.x and cell.y == current_cell.y + 1:
            neighbors.append(cell)

    return neighbors


def find_paths(cells: list[Cell], current_cell: Cell, visited_cells: list[Cell]) -> int:
    if current_cell.value == 9:
        if current_cell not in visited_cells:
            visited_cells.append(current_cell)
            return 1
        else:
            return 0

    total = 0
    neighbors: list[Cell] = get_neighbors(cells, current_cell)
    for neighbor in neighbors:
        if neighbor.value == current_cell.value + 1:
            total += find_paths(cells, neighbor, visited_cells)

    return total


def main():
    cells: list[Cell] = []

    with open("input.txt", "r") as file:
        for y, line in enumerate(file):
            for x, cell in enumerate(line.strip()):
                cells.append(Cell(int(cell), x, y))

    total = 0
    for cell in cells:
        if cell.value == 0:
            total += find_paths(cells, cell, [])

    print(total)


if __name__ == "__main__":
    main()
