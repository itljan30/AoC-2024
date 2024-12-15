// NOTE Not solved, there is a bug somewhere. Python version is solved though.

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

void swapValues(Rule *rule, DynArr *update) {
    // I haven't implemented a find method for my DynArr yet :(
    int index1 = -1;
    for (int i = 0; i < DynArr_len(update); i++) {
        if (*(int*)DynArr_at(update, i) == *rule->firstPage) {
            index1 = i;
            break;
        }
    }

    int index2 = -1;
    for (int i = 0; i < DynArr_len(update); i++) {
        if (*(int*)DynArr_at(update, i) == *rule->secondPage) {
            index2 = i;
            break;
        }
    }

    if (index1 != -1 && index2 != -1) {
        int *temp = (int*)DynArr_at(update, index1);
        DynArr_set(update, index1, (int*)DynArr_at(update, index2));
        DynArr_set(update, index2, temp);
    }
}

bool testRule(Rule *rule, DynArr *update) {
    bool first = false;
    bool second = false;

    for (int i = 0; i < DynArr_len(update); i++) {
        int currentInt = *(int*)DynArr_at(update, i);

        if (currentInt == *rule->firstPage) {
            if (second == true) {
                swapValues(rule, update);
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

bool alreadyInvalid(DynArr *update, DynArr *invalidUpdates) {
    for (int i = 0; i < DynArr_len(invalidUpdates); i++) {
        if (update == (DynArr*)DynArr_at(invalidUpdates, i)) {
            return true;
        }
    }
    return false;
}

bool doSwaps(DynArr *rules, DynArr *updates, DynArr *invalidUpdates) {
    int noSwaps = true;
    for (int i = 0; i < DynArr_len(updates); i++) {
        for (int j = 0; j < DynArr_len(rules); j++) {
            if (!testRule(DynArr_at(rules, j), DynArr_at(updates, i))) {
                if (!alreadyInvalid(DynArr_at(updates, i), invalidUpdates)) {
                    DynArr_append(invalidUpdates, DynArr_at(updates, i));
                    noSwaps = false;
                }
            }
        }
    }

    return noSwaps;
}

// BUG Currently getting an answer too high (needs to be 5723)
void solveProblem(DynArr *rules, DynArr *updates) {
    DynArr *invalidUpdates = DynArr_new(sizeof(DynArr*));
    bool finished = false;
    while (!finished) {
        finished = doSwaps(rules, updates, invalidUpdates);
    }

    int total = 0; 
    for (int i = 0; i < DynArr_len(invalidUpdates); i++) {
        DynArr *update = DynArr_at(invalidUpdates, i);
        total += *(int*)DynArr_at(update, DynArr_len(update) / 2);
    }

    printf("%d\n", total);

    DynArr_free(invalidUpdates);
}

int main() {
    DynArr *rules = DynArr_new(sizeof(Rule*));
    DynArr *updates = DynArr_new(sizeof(DynArr*));
    loadData(rules, updates);

    solveProblem(rules, updates);

    freeAll(rules, updates);
}
