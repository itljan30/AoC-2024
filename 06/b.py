# NOTE It is not efficient whatsoever and it takes about 1:40 minutes to finish


import sys
from copy import deepcopy


class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


RIGHT = Coord( 1,  0)
DOWN  = Coord( 0,  1)
LEFT  = Coord(-1,  0)
UP    = Coord( 0, -1)


def draw_line(map: list[list[str]], position: Coord, direction: Coord) -> Coord:
    while True:
        next_x = position.x + 1 * direction.x
        next_y = position.y + 1 * direction.y

        if not 0 <= next_y < len(map) or not 0 <= next_x < len(map[0]):
            return Coord(-1, -1)

        if map[next_y][next_x] == '#':
            return position

        position = Coord(next_x, next_y)
        map[position.y][position.x] = 'X'


def find_start(map: list[list[str]]) -> Coord:
    for y, row in enumerate(map):
        if '^' in row:
            x = row.index('^')
            return Coord(x, y)
    return Coord(-1, -1)


def count_traversed(map: list[list[str]]) -> int:
    total = 0
    for row in map:
        total += row.count('X')

    return total


def draw_path(map: list[list[str]], start: Coord) -> int:
    loops = 0
    before = 0
    direction = LEFT
    while True:
        # used to make sure we moved, if we didn't move then we were in a corner and not a loop
        prev_start = start
        if start.x == -1 and start.y == -1:
            return 0

        if direction == UP:
            direction = RIGHT
            start = draw_line(map, start, direction)
        elif direction == RIGHT:
            direction = DOWN
            start = draw_line(map, start, direction)
        elif direction == DOWN:
            direction = LEFT
            start = draw_line(map, start, direction)
        elif direction == LEFT:
            direction = UP
            start = draw_line(map, start, direction)

        after = count_traversed(map)
        if before == after and start != prev_start:
            loops += 1
            # NOTE
            # I tried this with 2 thinking the issue was that there is a situation where we end up with this:
            #  o              o
            # o                o
            #                 o
            # o  <
            #
            # but 2 didn't work so I increased to 10 I guess there was a longer version of this
            # I guess my method of checking if it is a loop could be improved
            if loops >= 10:
                return 1

        before = after


def cull_locations(map: list[list[str]], start: Coord) -> list[Coord]:
    draw_path(map, start)

    coords: list[Coord] = []
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == 'X':
                coords.append(Coord(x, y))

    return coords


def main():
    map: list[list[str]] = []

    with open("input.txt", "r") as file:
        for line in file:
            map.append(list(line))

    start: Coord = find_start(map)
    if start.x == -1 and start.y == -1:
        sys.exit("Couldn't find starting position")

    coords_to_check = cull_locations(deepcopy(map), start)

    loops = 0
    for coord in coords_to_check:
        if coord == start:
            continue
        map_copy = deepcopy(map)
        map_copy[coord.y][coord.x] = '#'
        loops += draw_path(map_copy, start)

    print(loops)

if __name__ == "__main__":
    main()
