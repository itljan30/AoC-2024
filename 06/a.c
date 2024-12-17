#include "dyn_arr.h"

#include <stdlib.h>
#include <stdio.h>

typedef struct {
    int x;
    int y;
} Coord;

const Coord UP    = {0, -1};
const Coord RIGHT = {1,  0};
const Coord DOWN  = {0,  1};
const Coord LEFT  = {-1, 0};

void loadData(DynArr *map) {
    FILE *reader = fopen("input.txt", "r");
    if (reader == NULL) {
        printf("ERROR: Unable to open 'input.txt'");
        exit(EXIT_FAILURE);
    }
    
    char line[256];
    while (fgets(line, sizeof(line), reader) != NULL) {
        DynArr_append(map, strdup(line));
    }
}

Coord findStart(DynArr *map) {
    for (int i = 0; i < DynArr_len(map); i++) {
        char *currentString = DynArr_at(map, i);
        for (int j = 0; j < strlen(currentString); j++) {
            if (currentString[j] == '^') {
                Coord coord = {j, i};
                return coord;
            }
        }
    }
    Coord coord = {-1, -1};
    return coord;
}

Coord markLine(DynArr *map, Coord position, Coord direction) {
    while (true) {
        int nx = position.x + (1 * direction.x);
        int ny = position.y + (1* direction.y);

        if (nx < 0 || nx >= strlen(DynArr_at(map, 0)) || ny < 0 || ny >= DynArr_len(map)) {
            position.x = -1;
            break;
        }

        char *row = (char*)DynArr_at(map, ny);
        if (row[nx] == '#') {
            break;
        }

        row[nx] = 'X';

        position.x = nx;
        position.y = ny;
    }
    return position;
}

void markPath(DynArr *map, Coord start) {
    Coord currentDirection = UP;
    while (true) {
        start = markLine(map, start, currentDirection);
        if (start.x == -1) {
            break;
        }

        if (currentDirection.x == UP.x && currentDirection.y == UP.y) {
            currentDirection = RIGHT;
        }
        else if (currentDirection.x == RIGHT.x && currentDirection.y == RIGHT.y) {
            currentDirection = DOWN;
        }
        else if (currentDirection.x == DOWN.x && currentDirection.y == DOWN.y) {
            currentDirection = LEFT;
        }
        else if (currentDirection.x == LEFT.x && currentDirection.y == LEFT.y) {
            currentDirection = UP;
        }
    }
}


int countTraversed(DynArr *map) {
    int total = 0;
    for (int i = 0; i < DynArr_len(map); i++) {
        char *currentString = DynArr_at(map, i);
        for (int j = 0; j < strlen(currentString); j++) {
            if (currentString[j] == 'X') {
                total++;
            }
        }
    }
    return total;
}

int main() {
    DynArr *map = DynArr_new(sizeof(char*));
    loadData(map);

    Coord start = findStart(map);
    markPath(map, start);
    printf("%i\n", countTraversed(map));

    DynArr_destroy(map, free);
}
