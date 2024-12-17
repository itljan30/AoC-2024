# NOTE BUG Not solved. There's a tiny bug somewhere.


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_anti_from_pair(origin: Node, other: Node) -> Node:
    # 1. pretend node is at origin
    # 2. return other's antinode found on the opposite quadrant of graph
    zeroed_x = other.x - origin.x
    zeroed_y = other.y - origin.y

    anti_x = 0
    anti_y = 0

    anti_x = zeroed_x + (2 * zeroed_x) if zeroed_x < 0 else zeroed_x - (2 * zeroed_x)
    anti_y = zeroed_y + (2 * zeroed_y) if zeroed_y < 0 else zeroed_y - (2 * zeroed_y)

    return Node(anti_x + origin.x, anti_y + origin.y)


def find_antinodes(nodes: list[Node]) -> list[Node]:
    antinodes: list[Node] = []
    for i, node in enumerate(nodes):
        for other_node in nodes[i:]:
            antinodes.append(get_anti_from_pair(node, other_node))
            antinodes.append(get_anti_from_pair(other_node, node))

    return antinodes


def clean_antinodes(nodes: list[Node]) -> list[Node]:
    cleaned_nodes: list[Node] = []
    seen_coords: list[tuple[int, int]] = []
    for node in nodes:
        if 0 <= node.x < 50 and 0 <= node.y < 50:
            if (node.x, node.y) not in seen_coords:
                seen_coords.append((node.x, node.y))
                cleaned_nodes.append(node)

    return cleaned_nodes


def main():
    nodes: dict = {}

    with open("input.txt", "r") as file:
        for y, line in enumerate(file):
            for x, cell in enumerate(line.strip()):
                if cell != '.':
                    nodes.setdefault(cell, list())
                    nodes[cell].append(Node(x, y))

    antinodes: list[Node] = []

    for node_type in nodes:
        antinodes += find_antinodes(nodes[node_type])

    antinodes = clean_antinodes(antinodes)

    print(len(antinodes))


if __name__ == "__main__":
    main()
