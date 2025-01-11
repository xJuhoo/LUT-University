// Juho Rekonen
// Student number: 441410

// Defining GNU Source to avoid "implicit declaration of getline()"
// got help from: https://stackoverflow.com/questions/59014090/warning-implicit-declaration-of-function-getline
#define _GNU_SOURCE

// Include libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>

// Linked list structure to store each line
typedef struct Node {
    char *line;
    struct Node *next;
} Node;

// Function to handle most of the errors
void errorHandler(const char *message) {
    fprintf(stderr, "%s\n", message);
    exit(1);
}

// Function to check if two files are hardlinked (test case 5 from project's GitHub)
int areIdentical(const char *input, const char *output) {
    // Learned about this from: https://stackoverflow.com/questions/15717221/how-to-determine-if-two-file-are-identical-in-c-using-system-call
    struct stat statInput, statOutput;

    // So, to determine whether two files are identical (a.k.a literally the same file), one must use system calls to acquire the devide ID and the inode number, and compare them for both files
    if (stat(input, &statInput) != 0) {
        errorHandler("Error retrieving file information for input.");
    }

    if (stat(output, &statOutput) != 0) {
        errorHandler("Error retrieving file information for output.");
    }

    // Comparison
    if (statInput.st_ino == statOutput.st_ino && statInput.st_dev == statOutput.st_dev) {
        // Files are the same
        return 1;
    }

    // Otherwise they are different
    return 0;
}

// Function to empty all the memory used for the linked list
void emptyList(Node *head) {
    Node *current = head;
    while (current) {
        Node *nextNode = current->next;
        free(current->line);
        free(current);
        current = nextNode;
    }
}

// Function to create a new node from given line
Node *createNode(char *line) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    // Check if memory allocation was a success
    if (!newNode) {
        errorHandler("malloc failed");
    }

    // Copy the line using a temporary variable
    char *temp = malloc(strlen(line) + 1);
    if (!temp) {
        free(newNode);
        errorHandler("malloc failed");
    }
    strcpy(temp, line);
    newNode->line = temp;
    newNode->next = NULL;

    return newNode;
}

// Function to add a new node to the linked list
void addNode(Node **head, char *line) {
    Node *newNode = createNode(line);
    // To achieve the reversed order we add a new node to the head of the list
    newNode->next = *head; // Insert new node
    *head = newNode; // Update the head
}

// Function to reverse the lines from an input file and write them to an output file
void reverseFiles(FILE *input, FILE *output) {
    Node *head = NULL;
    char *line = NULL;
    size_t len = 0; // Using a size_t variable because the length of each line is unknown

    // Learned how to use getLine() from https://c-for-dummies.com/blog/?p=1112 and
    // https://stackoverflow.com/questions/74556614/how-to-correctly-use-getline
    while ((getline(&line, &len, input)) != -1) {
        // First we check if the line ends with a newline character
        size_t length = strlen(line);
        if (line[length - 1] == '\n') {
            // If it does, we remove it
            line[length - 1] = '\0';
        }
        addNode(&head, line);
    }

    free(line);

    // Flag to check whether the output is a file or stdout
    int is_stdout = (output == stdout);

    // Traverse the list
    Node *current = head;
    while (current) {
        // If the output is stdout (=terminal), print the line with a newline at the end
        if (is_stdout) {
            fprintf(output, "%s\n", current->line);
        // If it's a file, print all lines except the last one with a newline
        } else if (current->next == NULL) {
            fprintf(output, "%s", current->line);
        } else {
            fprintf(output, "%s\n", current->line);
        }
        current = current->next;
    }

    // Free the linked list after printing
    emptyList(head);
}

// Main function
int main(int argc, char *argv[]){
    FILE *input = NULL;
    FILE *output = NULL;

    // Handle too many arguments
    if (argc > 3) {
        errorHandler("usage: reverse <input> <output>");
        exit(1);
    }

    // Check if an input file was given
    if (argc >= 2) {

        // Open input file if possible - otherwise set to stdin
        input = fopen(argv[1], "r");
        if (!input) {
            fprintf(stderr, "error: cannot open file '%s'\n", argv[1]);
            exit(1);
        }
    } else {
        input = stdin;
    }

    // Same thing with the output file
    if (argc == 3) {

        // Here we first check whether the files are different or not
        if (strcmp(argv[1], argv[2]) == 0) {
            errorHandler("Input and output file must differ");
        }
        // Open output file if possible
        output = fopen(argv[2], "w");
        if (!output) {
            fprintf(stderr, "error: cannot open file '%s'\n", argv[2]);
            exit(1);
        }
        // Then we check if the files are hardlinked
        if (areIdentical(argv[1], argv[2]) == 1) {
            errorHandler("Input and output file must differ");
        }

    // In case of no output file, set to stdout
    } else {
        output = stdout;
    }

    // Reverse the files
    reverseFiles(input, output);

    // Finally close both files if not stdin and stdout
    if (input != stdin) {
        fclose(input);
    }

    if (output != stdout) {
        fclose(output);
    }

    return 0;
}
