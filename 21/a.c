#include "dyn_arr.h"
#include "graph.h"
#include "linked_list.h"

#include <stdio.h>
#include <stdlib.h>

typedef enum Direction {
    UP,
    DOWN,
    RIGHT,
    LEFT,
    NONE,
} Direction;


DynArr *loadData() {
    DynArr *passcodes = DynArr_new(sizeof(DynArr));

    FILE *reader = fopen("in.txt", "r");
    if (reader == NULL) {
        printf("ERROR: Unable to open 'input.txt'");
        exit(EXIT_FAILURE);
    }
    
    char line[256];
    while (fgets(line, sizeof(line), reader) != NULL) {
        DynArr *code = DynArr_new(sizeof(char));
        for (int i = 0; i < strlen(line); i++) {
            if (line[i] == '\n' || line[i] == ' ') {
                continue;
            }
            char *digit = malloc(sizeof(char));
            *digit = line[i];
            DynArr_append(code, digit);
        }
        DynArr_append(passcodes, code);
    }

    fclose(reader);

    return passcodes;
}

int compareFunc(void *value1, void *value2) {
    return *(char*)value1 - *(char*)value2;
}

/* +---+---+---+ */
/* | 7 | 8 | 9 | */
/* +---+---+---+ */
/* | 4 | 5 | 6 | */
/* +---+---+---+ */
/* | 1 | 2 | 3 | */
/* +---+---+---+ */
/*     | 0 | A | */
/*     +---+---+ */
void connectNumPad(Graph *graph) {
    char arr[4][3] = {
        {'7', '8', '9'},
        {'4', '5', '6'},
        {'1', '2', '3'},
        {' ', '0', 'A'}
    };
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 3; j++) {
            if (arr[i][j] != ' ') {
                if (i + 1 < 4) {
                    char neighbor = arr[i+1][j];
                    if (neighbor != ' ') {
                        Graph_connect(graph, &arr[i][j], &arr[i+1][j], DOWN);
                    }
                }
                if (i - 1 >= 0) {
                    char neighbor = arr[i-1][j];
                    if (neighbor != ' ') {
                        Graph_connect(graph, &arr[i][j], &arr[i-1][j], UP);
                    }
                }
                if (j + 1 < 3) {
                    char neighbor = arr[i][j+1];
                    if (neighbor != ' ') {
                        Graph_connect(graph, &arr[i][j], &arr[i][j+1], RIGHT);
                    }
                }
                if (j - 1 >= 0) {
                    char neighbor = arr[i][j-1];
                    if (neighbor != ' ') {
                        Graph_connect(graph, &arr[i][j], &arr[i][j-1], LEFT);
                    }
                }
            }
        }
    }
}

Graph *getNumPadGraph() {
    Graph *graph = Graph_new(sizeof(char), sizeof(char), compareFunc, compareFunc);

    char valuebuffer[11] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A'};

    for (int i = 0; i < 11; i++) {
        char *key = malloc(sizeof(char));
        char *value = malloc(sizeof(char));
        *key = valuebuffer[i];
        *value = valuebuffer[i];
        Graph_add(graph, key, value);
    }

    connectNumPad(graph);

    return graph;
}

/*     +---+---+ */
/*     | ^ | A | */
/* +---+---+---+ */
/* | < | v | > | */
/* +---+---+---+ */
void connectArrowPad(Graph *graph) {
    char arr[2][3] = {
        {' ', '^', 'A'},
        {'<', 'v', '>'}
    };
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            if (arr[i][j] != ' ') {
                if (i + 1 < 2) {
                    char neighbor = arr[i+1][j];
                    if (neighbor != ' ') {
                        Graph_connect(graph, &arr[i][j], &arr[i+1][j], DOWN);
                    }
                }
                if (i - 1 >= 0) {
                    char neighbor = arr[i-1][j];
                    if (neighbor != ' ') {
                        Graph_connect(graph, &arr[i][j], &arr[i-1][j], UP);
                    }
                }
                if (j + 1 < 3) {
                    char neighbor = arr[i][j+1];
                    if (neighbor != ' ') {
                        Graph_connect(graph, &arr[i][j], &arr[i][j+1], RIGHT);
                    }
                }
                if (j - 1 >= 0) {
                    char neighbor = arr[i][j-1];
                    if (neighbor != ' ') {
                        Graph_connect(graph, &arr[i][j], &arr[i][j-1], LEFT);
                    }
                }
            }
        }
    }
}

Graph *getArrowPad() {
    Graph *graph = Graph_new(sizeof(char), sizeof(char), compareFunc, compareFunc);
    char valuebuffer[5] = {'<', 'v', '^', '>', 'A'};

    for (int i = 0; i < 5; i++) {
        char *key = malloc(sizeof(char));
        char *value = malloc(sizeof(char));
        *key = valuebuffer[i];
        *value = valuebuffer[i];
        Graph_add(graph, key, value);
    }

    connectArrowPad(graph);

    return graph;
}

void prependDirection(DynArr *arr, Direction direction) {
    if (direction == UP) {
        char *instruction = malloc(sizeof(char));
        *instruction = '^';
        DynArr_insert(arr, 0, instruction);
    }
    else if (direction == DOWN) {
        char *instruction = malloc(sizeof(char));
        *instruction = 'v';
        DynArr_insert(arr, 0, instruction);
    }
    else if (direction == LEFT) {
        char *instruction = malloc(sizeof(char));
        *instruction = '<';
        DynArr_insert(arr, 0, instruction);
    }
    else if (direction == RIGHT) {
        char *instruction = malloc(sizeof(char));
        *instruction = '>';
        DynArr_insert(arr, 0, instruction);
    }
    else if (direction == NONE) {
        printf("Direction was NONE\n");
    }
}

void prependActivate(DynArr *arr) {
    char *instruction = malloc(sizeof(char));
    *instruction = 'A';
    DynArr_insert(arr, 0, instruction);
}

// Haven't implemented this one apparently
int getIndexFromNode(DynArr *arr, GraphNode *node) {
    for (int i = 0; i < DynArr_len(arr); i++) {
        if (memcmp(node, DynArr_at(arr, i), sizeof(GraphNode)) == 0) {
            return i;
        }
    }
    return -1;
}

// I need to implement this one too
DynArr *getAllVerticies(Graph *graph) {
    DynArr *arr = DynArr_new(sizeof(GraphNode));
    for (int i = 0; i < DynArr_len(graph->nodes->map); i++) {
        LinkedList *curList = (LinkedList*)DynArr_at(graph->nodes->map, i);
        if (curList != NULL) {
            for (int j = 0; j < LinkedList_len(curList); j++) {
                KeyValue *curPair = (KeyValue*)LinkedList_at(curList, j);
                GraphNode *curNode = curPair->value;
                DynArr_append(arr, curNode);
            }
        }
    }
    return arr;
}

int getIndexFromKey(DynArr *path, char dest) {
    for (int i = 0; i < DynArr_len(path); i++) {
        if (DynArr_at(path, i) == NULL) {
            continue;
        }
        GraphNode *curNode = (GraphNode*)DynArr_at(path, i);
        if (*(char*)curNode->data  - dest == 0) {
            return i;
        }
    }
    return -1;
}

DynArr *parsePath(DynArr *verticies, DynArr *path, DynArr *pathDirections, char dest) {
    DynArr *result = DynArr_new(sizeof(char));

    int index = getIndexFromKey(verticies, dest);
    prependActivate(result);
    while (index != -1) {
        GraphNode *curNode = (GraphNode*)DynArr_at(path, index);
        if (curNode == NULL) {
            break;
        }
        prependDirection(result, *(Direction*)DynArr_at(pathDirections, index));

        index = getIndexFromKey(verticies, *(char*)curNode->data);
    }
    return result;
}

// Dijkstra
void addPath(DynArr *currentPath, Graph *graph, char src, char dest) {
    DynArr *verticies = getAllVerticies(graph);

    // make path and distance same size as verticies and all in path to NULL and all in distance to infinity
    DynArr *queue = DynArr_new(sizeof(GraphNode));
    DynArr *path = DynArr_new(sizeof(GraphNode));
    DynArr *pathDirections = DynArr_new(sizeof(Direction));
    DynArr *distance = DynArr_new(sizeof(int));
    for (int i = 0; i < DynArr_len(verticies); i++) {
        int *inf = malloc(sizeof(int));
        *inf = 999999;
        DynArr_append(distance, inf);

        DynArr_append(path, NULL);

        Direction *dir = malloc(sizeof(Direction));
        *dir = NONE;
        DynArr_append(pathDirections, dir);

        DynArr_append(queue, DynArr_at(verticies, i));
    }

    // set distance[sourceIndex] = 0
    int sourceIndex = getIndexFromKey(verticies, src);
    int *num = malloc(sizeof(int));
    *num = 0;
    DynArr_set(distance, sourceIndex, num);

    while (DynArr_len(queue) != 0) {
        GraphNode *closestNode = NULL;
        int closestIndex = -1;
        int lowestDist = 999999;

        for (int i = 0; i < DynArr_len(queue); i++) {
            GraphNode *curNode = (GraphNode*)DynArr_at(queue, i);
            int index = getIndexFromNode(verticies, curNode);
            int dist = *(int*)DynArr_at(distance, index);
            if (dist < lowestDist) {
                lowestDist = dist;
                closestNode = curNode;
                closestIndex = i;
            }
        }

        if (*(char*)closestNode->data == dest) {
            break;
        }

        DynArr_remove(queue, closestIndex);

        for (int i = 0; i < DynArr_len(closestNode->edges); i++) {
            Edge *currentEdge = DynArr_at(closestNode->edges, i);
            if (DynArr_contains(queue, currentEdge->dest)) {
                int neighborIndex = getIndexFromNode(verticies, currentEdge->dest);
                int parentIndex = getIndexFromNode(verticies, closestNode);

                int alt = *(int*)DynArr_at(distance, parentIndex) + 1;
                if (alt < *(int*)DynArr_at(distance, neighborIndex)) {
                    int *newSpot = malloc(sizeof(int));
                    *newSpot = alt;
                    DynArr_set(distance, neighborIndex, newSpot);

                    DynArr_set(path, neighborIndex, closestNode);

                    Direction *dir = malloc(sizeof(Direction));
                    *dir = (int)currentEdge->weight;
                    DynArr_set(pathDirections, neighborIndex, dir);
                }
            }
        }
    }

    DynArr *parsedPath = parsePath(verticies, path, pathDirections, dest);
    for (int i = 0; i < DynArr_len(parsedPath); i++) {
        DynArr_append(currentPath, DynArr_at(parsedPath, i));
    }

    DynArr_free(parsedPath);
    DynArr_free(verticies);
    DynArr_free(queue);
    DynArr_free(path);
    DynArr_destroy(distance, free);
    DynArr_destroy(pathDirections, free);
}

DynArr *findNumPadInput(DynArr *output) {
    DynArr *input = DynArr_new(sizeof(char));
    Graph *numPad = getNumPadGraph();

    char start = 'A';
    
    for (int i = 0; i < DynArr_len(output); i++) {
        addPath(input, numPad, start, *(char*)DynArr_at(output, i));
        start = *(char*)DynArr_at(output, i);
    }

    DynArr_destroy(output, free);
    Graph_destroy(numPad, free, free);

    return input;
}

DynArr *findArrowPadInput(DynArr *output) {
    DynArr *input = DynArr_new(sizeof(char));
    Graph *arrowPad = getArrowPad();
    char start = 'A';
    
    for (int i = 0; i < DynArr_len(output); i++) {
        addPath(input, arrowPad, start, *(char*)DynArr_at(output, i));
        start = *(char*)DynArr_at(output, i);
    }

    DynArr_destroy(output, free);
    Graph_destroy(arrowPad, free, free);

    return input;
}

int main() {
    DynArr *passcodes = loadData();

    for (int i = 0; i < DynArr_len(passcodes); i++) {
        DynArr *output = DynArr_at(passcodes, i);
        DynArr *output1 = findNumPadInput(output);
        DynArr *output2 = findArrowPadInput(output1);
        DynArr *output3 = findArrowPadInput(output2);
        for (int i = 0; i < DynArr_len(output3); i++) {
            printf("%c", *(char*)DynArr_at(output3, i));
        }
        printf(": %i\n", (int)DynArr_len(output3));
        DynArr_destroy(output3, free);
    }
}
