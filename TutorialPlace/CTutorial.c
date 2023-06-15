#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[50];
    int age;
    char job[50];
} Personel;

void addPersonel(Personel personels[], int count) {
    printf("Name: ");
    fgets(personels[count].name, sizeof(personels[count].name), stdin);
    personels[count].name[strcspn(personels[count].name, "\n")] = '\0'; // Remove newline character

    printf("Job: ");
    fgets(personels[count].job, sizeof(personels[count].job), stdin);
    personels[count].job[strcspn(personels[count].job, "\n")] = '\0'; // Remove newline character

    printf("Age: ");
    scanf("%d", &personels[count].age);
    getchar(); // Consume newline character from previous scanf
}

void displayPersonels(Personel personels[], int count) {
    if (count == 0) {
        printf("No personels to display.\n");
        return;
    }

    printf("Personels:\n");
    for (int i = 0; i < count; i++) {
        printf("%d: Name: %s, Age: %d, Job: %s\n", i + 1, personels[i].name, personels[i].age, personels[i].job);
    }
}

void saveToFile(Personel personels[], int count) {
    if (count == 0) {
        printf("No personels to save.\n");
        return;
    }

    FILE* file = fopen("test.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return;
    }

    for (int i = 0; i < count; i++) {
        fprintf(file, "%d: Name: %s, Age: %d, Job: %s\n", i + 1, personels[i].name, personels[i].age, personels[i].job);
    }

    fclose(file);
    printf("Personels saved to file.\n");
}

int main() {
    Personel personels[100];
    int count = 0;

    while (1) {
        printf(":> ");
        char command[20];
        fgets(command, sizeof(command), stdin);
        command[strcspn(command, "\n")] = '\0'; // Remove newline character

        if (strcmp(command, "add user") == 0) {
            addPersonel(personels, count);
            count++;
        }
        else if (strcmp(command, "info") == 0) {
            displayPersonels(personels, count);
        }
        else if (strcmp(command, "save") == 0) {
            saveToFile(personels, count);
        }
    }

    return 0;
}
