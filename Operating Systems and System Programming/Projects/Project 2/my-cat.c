// Juho Rekonen
// Student number: 441410

// Include libraries
#include <stdio.h>
#include <stdlib.h>

// Function to read an print the files
void readFiles(FILE *file) {
    int isEmpty = 1;
    char line[1024];
    while (fgets(line, sizeof(line), file) != NULL) {
        isEmpty = 0;
        printf("%s", line);
    }

    if (!isEmpty) {
        printf("\n");
    }
}

// Main function
int main (int argc, char *argv[]) {
    FILE *file;

    // Check if any files were given
    if (argc < 2) {
        return 0;
    }

    // Iterate through the files
    for (int i = 1; i < argc; i++) {
        // Check that the file can be opened in read mode
        if ((file = fopen(argv[i], "r")) == NULL) {
            printf("my-cat: cannot open file\n");
            return 1;
        }

        readFiles(file);
        fclose(file);
    }
    return 0;
}
