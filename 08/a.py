width: int = 50
height: int = 50


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def find_antinodes(nodes: list[Node]) -> list[Node]:
    for i, node in enumerate(nodes):
        for j, other_node in enumerate(nodes[i:]):
            ...


def clean_antinodes(nodes: list[Node]) -> list[Node]:
    ...


def main():
    nodes: dict = {}

    with open("input.txt", "r") as file:
        for y, line in enumerate(file):
            for x, cell in enumerate(line):
                if cell != '.':
                    nodes.setdefault(cell, [])
                    nodes[cell].append(Node(x, y))

    antinodes: list[Node] = []

    for node_type in nodes:
        antinodes += find_antinodes(nodes[node_type])

    antinodes = clean_antinodes(antinodes)

    print(len(antinodes))


if __name__ == "__main__":
    main()
