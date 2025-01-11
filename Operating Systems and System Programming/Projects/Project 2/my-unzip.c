// Juho Rekonen
// Student number: 441410

#include <stdio.h>
#include <stdlib.h>

// Function to decompress files
void unzip(FILE *file) {
    int count;
    char character;

    while (fread(&count, sizeof(int), 1, file)) {
        fread(&character, sizeof(char), 1, file);
        // Print the character "count" times
        for (int i = 0; i < count; i++) {
            printf("%c", character);
        }
    }
}

// Main function
int main (int argc, char *argv[]) {
    FILE *file;

    // Check that any files were given
    if (argc < 2) {
        printf("my-unzip: file1 [file2 ...]\n");
        return 1;
    }

    // Iterate through the files
    for (int i = 1; i < argc; i++) {
        if ((file = fopen(argv[i], "r")) == NULL) {
            printf("my-unzip: cannot open file\n");
            return 1;
        }

        unzip(file);
        fclose(file);
    }
    printf("\n");
    return 0;
}
