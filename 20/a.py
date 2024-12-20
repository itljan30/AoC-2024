def get_start(maze: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "S":
                return (x, y)
    return (0, 0)


def get_neighbors(maze: list[list[str]], start: tuple[int, int]) -> list[tuple[int, int]]:
    neighbors: list[tuple[int, int]] = []
    for i in range(-1, 1):
        for j in range(-1, 1):
            if not 0 <= start[1] + i < len(maze) or not 0 <= start[0] + j < len(maze[0]):
                continue
            if maze[start[1] + i][start[1] + j] != "#":
                neighbors.append((start[0] + i, start[1] + j))

    return neighbors


# I'll take this moment to learn Dijkstra's it's not actually 
# going to be helpful, but I have been wanting to learn it so why not
#  1  function Dijkstra(Graph, source):
#  2     
#  3      for each vertex v in Graph.Vertices:
#  4          dist[v] ← INFINITY
#  5          prev[v] ← UNDEFINED
#  6          add v to Q
#  7      dist[source] ← 0
#  8     
#  9      while Q is not empty:
# 10          u ← vertex in Q with minimum dist[u]
# 11          remove u from Q
# 12         
# 13          for each neighbor v of u still in Q:
# 14              alt ← dist[u] + Graph.Edges(u, v)
# 15              if alt < dist[v]:
# 16                  dist[v] ← alt
# 17                  prev[v] ← u
# 18
# 19      return dist[], prev[]
def dijkstra(maze: list[list[str]], start_x: int, start_y: int) -> list[list[tuple]]:
    dist: list[list[int]] = []
    prev: list[list[tuple[int, int]]] = []
    queue: list[tuple[int, int]] = []

    for y in range(len(maze)):
        dist_row = []
        prev_row = []
        for x in range(len(maze[0])):
            dist_row.append(999999)
            prev_row.append(None)
            queue.append((x, y))
        dist.append(dist_row)
        prev.append(prev_row)

    dist[start_y][start_x] = 0

    while queue:
        index: tuple[int, int] = (-1, -1)
        lowest = 10000000
        for coord in queue:
            if dist[coord[1]][coord[0]] < lowest:
                index = (coord[0], coord[1])
                lowest = dist[coord[1]][coord[0]]

        if maze[index[1]][index[0]] == "E":
            return prev

        queue.remove(index)

        neighbors: list[tuple[int, int]] = get_neighbors(maze, index)

        for neighbor in neighbors:
            if neighbor not in queue:
                continue
            alt = dist[index[1]][index[0]] + 1
            if alt < dist[neighbor[1]][neighbor[0]]:
                dist[neighbor[1]][neighbor[0]] = alt
                prev[neighbor[1]][neighbor[0]] = (index[0], index[1])
    return prev


def get_all_neighbors(maze: list[list[str]], x: int, y: int) -> list[tuple[int ,int]]:
    neighbors: list[tuple[int, int]] = []
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    UP = (0, -1)

    for direction in [LEFT, RIGHT, DOWN, UP]:
        if not 0 <= y + direction[1] < len(maze) or not 0 <= x + direction[0] < len(maze[0]):
            continue
        neighbors.append((x + direction[0], y + direction[1]))

    return neighbors


# okay, side quest over, now onto the real problem
def find_solution_in_x(maze: list[list[str]], start_x: int, start_y: int, max_steps: int, depth=0, cheat=False) -> int:
    print(depth)
    if depth >= max_steps:
        return 0

    if maze[start_y][start_x] == "E":
        return 1

    total = 0
    neighbors: list[tuple[int, int]] = get_all_neighbors(maze, start_x, start_y)
    for neighbor in neighbors:
        if not cheat and maze[neighbor[1]][neighbor[0]] == "#":
            total += find_solution_in_x(maze, neighbor[0], neighbor[1], max_steps, depth + 1, True)
        total += find_solution_in_x(maze, neighbor[0], neighbor[1], max_steps, depth + 1, cheat)

    return total


def main():
    maze: list[list[str]] = []

    with open("input.txt", "r") as file:
        for line in file:
            row = []
            for char in line.strip():
                row.append(char)
            maze.append(row)

    start_x, start_y = get_start(maze)

    total = find_solution_in_x(maze, start_x, start_y, 100)

    print(total)


if __name__ == "__main__":
    main()
