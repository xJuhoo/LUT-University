// Juho Rekonen
// Student number: 441410

#include <stdio.h>
#include <stdlib.h>

// Function to compress files
void zip(FILE *file, int *counter, char *previous) {
    char current;

    // Learned more about fgetc() from https://www.geeksforgeeks.org/fgetc-fputc-c/

    // Assign the first read character to previous, and check if the file is empty
    if (*previous == '\0') {
        *previous = fgetc(file);
        // If the file is empty, return
        if (*previous == EOF) {
            return;
        }
        *counter = 1;
    }

    while ((current = fgetc(file)) != EOF) {
        // Case when multiple same characters
        if (current == *previous) {
            (*counter)++;
        } else {
            // When character changes, we write the counter + character
            fwrite(counter, sizeof(int), 1, stdout);
            fwrite(previous, sizeof(char), 1, stdout);
            *previous = current;
            *counter = 1; // Reset counter
        }
    }
}

int main(int argc, char *argv[]) {
    FILE *file;
    int counter = 0;
    char previous = '\0';

    // Check that any files were given
    if (argc < 2) {
        printf("my-zip: file1 [file2 ...]\n");
        return 1;
    }

    // Iterate through the files
    for (int i = 1; i < argc; i++) {
        if ((file = fopen(argv[i], "r")) == NULL) {
            printf("my-zip: cannot open file\n");
            return 1;
        }

        zip(file, &counter, &previous);
        fclose(file);
    }

    // Once we have reached the EOF, we write the last character seen
    if (previous != '\0') {
        fwrite(&counter, sizeof(int), 1, stdout);
        fwrite(&previous, sizeof(char), 1, stdout);
    }
    printf("\n");
    return 0;
}
