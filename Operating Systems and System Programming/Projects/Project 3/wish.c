// Juho Rekonen
// Student number: 441410

// Defining GNU Source to avoid "implicit declaration of getline()"
// got help from: https://stackoverflow.com/questions/59014090/warning-implicit-declaration-of-function-getline

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>

// Since we don't know the amount of given args or specified paths
#define MAX_PATHS 100
#define MAX_ARGS 100

char *paths[MAX_PATHS];
int numberOfPaths;

void parseInput(char *line);

// Initialize paths with default value
void initPath() {
    paths[0] = "/bin";
    numberOfPaths = 1;
}

// Print error message
void errorHandler() {
    char error_message[30] = "An error has occurred\n";
    write(STDERR_FILENO, error_message, strlen(error_message));
}

// Function to handle execution of commands
void executeCommand(char **args, char *redirectFile) {
    if (numberOfPaths == 0) {
        errorHandler();
        return;
    }

    char fullPath[1024];
    for (int i = 0; i < numberOfPaths; i++) {
        snprintf(fullPath, sizeof(fullPath), "%s/%s", paths[i], args[0]);
        if (access(fullPath, X_OK) == 0) {

            pid_t pid = fork();
            if (pid == 0) {
                // Child process
                if (redirectFile != NULL) {
                    // Open file for write-only, create a file if does not exist, truncate the file, octal encoding
                    int fd = open(redirectFile, O_WRONLY | O_CREAT | O_TRUNC, 0644);
                    if (fd == -1) {
                        errorHandler();
                        exit(1);
                    }
                    // Redirect stdout and stderr to the file
                    dup2(fd, STDOUT_FILENO);
                    dup2(fd, STDERR_FILENO);
                    close(fd);
                }
                // Execute the command
                execv(fullPath, args);
                // If execv fails
                errorHandler();
                return;
            } else if (pid > 0) {
                // Parent process
                wait(NULL);
                return;
            } else {
                // Otherise fork() fails
                errorHandler();
                return;
            }
        }
    }
    // If not found in any path, print error
    errorHandler();
}

// Function to handle parallel execution of commands
void executeParallel(char *line) {
    // Tokenize the input into multiple commands
    char *parallel[MAX_ARGS];
    char *token;
    int count = 0;

    // Parse the input
    token = strtok(line, "&");
    while (token != NULL) {
        parallel[count++] = token;
        token = strtok(NULL, "&");
    }
    parallel[count] = NULL;

    pid_t pids[count];
    for (int i = 0; i < count; ++i) {
        pids[i] = fork(); // Create a new process
        if (pids[i] == 0) {
            parseInput(parallel[i]); // Child process handles the command
            exit(0); // Child process exits after handling the command
        } else if (pids[i] < 0) {
            errorHandler(); // Display error if fork fails
        }
    }

    for (int i = 0; i < count; ++i) {
        waitpid(pids[i], NULL, 0); // Parent process waits for all child processes to finish
    }
}

void parseInput(char *line) {
    char *args[MAX_ARGS];
    char *redirectFile = NULL;
    int argc = 0;
    char *token;
    int redirectCount = 0;

    // Check for parallel commands
    if (strchr(line, '&') != NULL) {
        executeParallel(line);
        return;
    }

    // Parse the input
    token = strtok(line, " \t\n");
    while (token != NULL) {
        //printf("Token: %s\n", token);
        args[argc++] = token;
        token = strtok(NULL, " \t\n");
    }
    args[argc] = NULL;

    // Iterate through the tokens to handle redirection errors
    for (int i = 0; i < argc; i++) {
        if (strcmp(args[i], ">") == 0) {
            redirectCount++;

            // Error 1: if args[0] = ">"
            // Description: ">" at the beginning (no commands before it)
            if (i == 0) {
                errorHandler();
                return;
            }

            // Error 2: if redirectCount > 1
            // Description: multiple ">" symbols
            else if (redirectCount > 1) {
                errorHandler();
                return;
            }

            // Error 3: if args[i] = ">" && args[i + 1] = NULL
            // Description: ">" with no output file after it
            else if (i + 1 >= argc) {
                errorHandler();
                return;
            }

            // Error 4: if args[i] = ">" && args[i + 2] != NULL
            // Description: ">" followed by more than one command
            else if (i + 2 < argc) {
                errorHandler();
                return;
            }

            // Store the redirect file
            redirectFile = args[i + 1];
            // Set ">" to NULL and update number of arguments, because the symbol and the output file are not valid arguments for execv()
            args[i] = NULL;
            argc = i;
            break;
        }
    }

    // Check for built-in commands
    if (!(argc > 0)) {
        return; // No commands given
    } else if (strcmp(args[0], "exit") == 0) {
        // More than 1 argument after typing "exit"
        if (argc > 1) {
            errorHandler();
        } else {
            exit(0);
        }
    } else if (strcmp(args[0], "cd") == 0) {
        // If not 2 arguments
        if (argc != 2) {
            errorHandler();
        } else if (chdir(args[1]) != 0) {
            errorHandler();
        }
    } else if (strcmp(args[0], "path") == 0) {
        numberOfPaths = 0;
        // Set new paths
        for (int i = 1; i < argc; i++) {
            paths[numberOfPaths++] = strdup(args[i]);
        }
        paths[numberOfPaths] = NULL;
    } else {
        // Otherwise execute external command
        executeCommand(args, redirectFile);
    }
}

// Function to run shell in batch mode
void batchMode(char *filename) {
    FILE *file;
    if ((file = fopen(filename, "r")) == NULL) {
        errorHandler();
        exit(1);
    }

    char *line = NULL;
    size_t len = 0;

    while (getline(&line, &len, file) != -1) {
        // Remove newline character from the end
            if (line[len - 1] == '\n') {
                line[len - 1] = '\0';
            }
        parseInput(line);
    }

    free(line);
    fclose(file);
}

// Main function
int main(int argc, char *argv[]) {
    // Initialize paths
    initPath();

    if (argc == 1) {
        // Interactive mode
        char *line = NULL;
        size_t len = 0;

        while (1) {
            printf("wish> ");
            if (getline(&line, &len, stdin) == -1) {
                free(line);
                exit(0);
            }

            // Remove newline character from the end
            if (line[len - 1] == '\n') {
                line[len - 1] = '\0';
            }

            parseInput(line);
        }
    } else if (argc == 2) {
        // Batch mode
        batchMode(argv[1]);
    } else {
        // Too many arguments
        errorHandler();
        exit(1);
    }

    return 0;
}
