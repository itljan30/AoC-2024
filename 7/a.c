// NOTE not solved


#include "dyn_arr.h"

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *answer;
    DynArr *terms;
} Equation;

void Equation_free(void * data) {
    Equation *equation = (Equation*)data;
    DynArr_destroy(equation->terms, free);
    free(equation->answer);
    free(equation);
}

DynArr *loadData() {
    DynArr *equations = DynArr_new(sizeof(Equation*));

    FILE *reader = fopen("input.txt", "r");
    if (reader == NULL) {
        printf("ERROR: Unable to open input.txt\n");
        exit(EXIT_FAILURE);
    }

    char line[256];
    while (fgets(line, sizeof(line), reader) != NULL) {
        int answer;
        char terms[256];
        sscanf(line, "%i: %[0-9 ]", &answer, terms);

        Equation *equation = malloc(sizeof(Equation));

        int *ans = malloc(sizeof(int));
        *ans = answer;
        equation->answer = ans;

        DynArr *termsArray = DynArr_new(sizeof(int));

        char *token = strtok(terms, " ");
        while (token != NULL) {
            int *value = malloc(sizeof(int));
            *value = atoi(token);
            DynArr_append(termsArray, value);
            token = strtok(NULL, " ");
        }

        equation->terms = termsArray;
        DynArr_append(equations, equation);
    }

    fclose(reader);
    return equations;
}

bool solve(Equation *equation, int index, int total) {
    if (index == DynArr_len(equation->terms)) {
        return (total == *equation->answer);
    }
    return solve(equation, index + 1, total + *(int*)DynArr_at(equation->terms, index)) ||
           solve(equation, index + 1, total * *(int*)DynArr_at(equation->terms, index));
}

bool isSolvable(Equation *equation) {
    return solve(equation, 1, *(int*)DynArr_at(equation->terms, 0));
}

int main() {
    DynArr *equations = loadData();
    int total = 0;
    for (int i = 0; i < DynArr_len(equations); i++) {
        Equation *equation = (Equation*)DynArr_at(equations, i);
        if (isSolvable(equation)) {
            total += *equation->answer;
        }
    }

    printf("%i\n", total);

    DynArr_destroy(equations, Equation_free);
}