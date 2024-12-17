// we love C, took about 10 minutes to solve this problem ... 
// if we ignore the 1ish hour it took to set up the loading of data and proper freeing of memory

#include "dyn_arr.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int *firstPage;
    int *secondPage;
} Rule;

void Rules_free(void *data) {
    Rule *rules = (Rule*)data;
    free(rules->firstPage);
    free(rules->secondPage);
    free(rules);
}

void loadData(DynArr *rules, DynArr *updates) {
    FILE *reader = fopen("input.txt", "r");
    if (reader == NULL) {
        printf("ERROR: Unable to open 'input.txt'");
        exit(EXIT_FAILURE);
    }
    
    char line[256];
    while (fgets(line, sizeof(line), reader) != NULL) {
        // breaks out of loop on the empty string between rules and updates in input
        if (line[0] == '\n') {
            break;
        }

        int first, second;
        sscanf(line, "%d|%d", &first, &second);

        Rule *rule = malloc(sizeof(Rule));
        rule->firstPage = malloc(sizeof(int));
        rule->secondPage = malloc(sizeof(int));
        *rule->firstPage = first;
        *rule->secondPage = second;

        DynArr_append(rules, rule);
    }

    while (fgets(line, sizeof(line), reader) != NULL) {
        DynArr *update = DynArr_new(sizeof(int*));
        char *token = strtok(line, ",");
        while (token != NULL) {
            int *currentInt = malloc(sizeof(int));
            *currentInt = atoi(token);
            DynArr_append(update, currentInt);
            token = strtok(NULL, ",");
        }
        DynArr_append(updates, update);
    }

    fclose(reader);
}

void freeAll(DynArr *rules, DynArr *updates) {
    for (int i = 0; i < DynArr_len(updates); i++) {
        DynArr_destroy(DynArr_at(updates, i), free);
    }
    DynArr_free(updates);

    DynArr_destroy(rules, Rules_free);
}

bool testRule(Rule *rule, DynArr *update) {
    bool first = false;
    bool second = false;

    for (int i = 0; i < DynArr_len(update); i++) {
        int currentInt = *(int*)DynArr_at(update, i);

        if (currentInt == *rule->firstPage) {
            if (second == true) {
                return false;
            }
            first = true;
        }
        if (currentInt == *rule->secondPage) {
            second = true;
        }
    }

    return true;
}

void solveProblem(DynArr *rules, DynArr *updates) {
    // I can probably do some simplification on rules, 
    // for example if I had 15|93 and 93|16 I could simplify it to 15|93|16
    // that would be faster (probably) but also something I 
    // don't want to figure out right now (especially in C)

    int total = 0;
    for (int i = 0; i < DynArr_len(updates); i++) {
        bool valid = true;
        for (int j = 0; j < DynArr_len(rules); j++) {
            if (!testRule(DynArr_at(rules, j), DynArr_at(updates, i))) {
                valid = false;
                break;
            }
        }
        
        if (!valid) {
            continue;
        }

        // we have an update that passes all tests, now just get the middle int and add it to total
        DynArr *update = DynArr_at(updates, i);
        total += *(int*)DynArr_at(update, DynArr_len(update) / 2);
    }

    printf("%d\n", total);
}

int main() {
    DynArr *rules = DynArr_new(sizeof(Rule*));
    DynArr *updates = DynArr_new(sizeof(DynArr*));
    loadData(rules, updates);

    solveProblem(rules, updates);

    freeAll(rules, updates);
}
