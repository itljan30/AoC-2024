// NOTE not solved, not enough memory to store all of these numbers lol. 
// program gets killed after about 1.5 minutes for me

// NOTE I can probably get by just knowing the length of each number rather
// than knowing the exact number, which would use less memory, but I don't
// know how I would go about doing that.

#include "dyn_arr.h"

#include <stdio.h>

DynArr *loadData() {
    DynArr *newArray = DynArr_new(sizeof(long));

    FILE *reader = fopen("input.txt", "r");
    if (reader == NULL) {
        printf("ERROR: Unable to open input.txt\n");
        exit(EXIT_FAILURE);
    }

    char line[256];
    while (fgets(line, sizeof(line), reader) != NULL) {
        char *token = strtok(line, " ");
        while (token != NULL) {
            long *value = malloc(sizeof(long));
            *value = atoi(token);
            DynArr_append(newArray, value);
            token = strtok(NULL, " ");
        }
    }

    fclose(reader);

    return newArray;
}

int powerTen(int power) {
    int num = 1;
    for (int i = 0; i < power; i++) {
        num *= 10;
    }
    return num;
}

void splitNumber(DynArr *currentArray, DynArr *newArray, int index, int size) {
        long num1 = *(long*)DynArr_at(currentArray, index);
        long num2 = 0;
        for (int i = 0; i < size / 2; i++) {
            num2 += num1 % 10 * powerTen(i);
            num1 /= 10;
        }
        
        long *long1 = malloc(sizeof(long));
        long *long2 = malloc(sizeof(long));

        *long1 = num1;
        *long2 = num2;

        DynArr_append(newArray, long1);
        DynArr_append(newArray, long2);
}

DynArr *update(DynArr *currentArray) {
    DynArr *newArray = DynArr_new(sizeof(long));

    for (int i = 0; i < DynArr_len(currentArray); i++) {
        long temp = *(long*)DynArr_at(currentArray, i);

        if (temp == 0) {
            long *newNum = malloc(sizeof(long));
            *newNum = 1;
            DynArr_append(newArray, newNum);
            continue;
        }

        int size = 1;
        while (temp >= 10) {
            temp /= 10;
            size++;
        }

        if (size % 2 == 0) {
            splitNumber(currentArray, newArray, i, size);
        }
        else {
            long *newNum = malloc(sizeof(long));
            *newNum = *(long*)DynArr_at(currentArray, i) * 2024;
            DynArr_append(newArray, newNum);
        }
    }

    DynArr_destroy(currentArray, free);

    return newArray;
}

int main() {
    DynArr *rocks = loadData();

    for (int i = 0; i < 75; i++) {
        rocks = update(rocks);
        printf("%i\n", (int)DynArr_len(rocks));
    }

    printf("%i\n", (int)DynArr_len(rocks));

    DynArr_destroy(rocks, free);
}
