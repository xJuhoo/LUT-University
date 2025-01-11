// Juho Rekonen
// Student number: 441410

#define _GNU_SOURCE
// Include libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to check for occurrences
void grep(FILE *file, char *target) {
    size_t length = 0;
    char *line;

    while (getline(&line, &length, file) != -1) {
        if (strstr(line, target) != NULL) {
            printf("%s", line);
        }
    }
    free(line);
}

// Main function
int main(int argc, char *argv[]) {
    FILE *file;

    // Check if any files were given
    if (argc < 2) {
        printf("my-grep: searchterm [file ...]\n");
        return 1;
    }

    char *target = argv[1];

    if (argc == 2) {
        grep(stdin, target);
    } else {
        // Iterate through the files
        for (int i = 2; i < argc; i++) {
            // Check that the file can be opened in read mode
            if ((file = fopen(argv[i], "r")) == NULL) {
                printf("my-grep: cannot open file\n");
                return 1;
            }

            grep(file, target);
            fclose(file);
        }
    }
    return 0;
}
