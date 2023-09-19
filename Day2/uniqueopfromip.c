#include <stdio.h>
#include <stdbool.h>

// Function to check if a character is a digit
bool isDigit(char c) {
    return (c >= '0' && c <= '9');
}

// Function to find unique digits in a string
void findUniqueDigits(char* str) {
    int count[10] = {0}; // Array to store the count of each digit
    int len = strlen(str);

    // Count the occurrences of each digit
    for (int i = 0; i < len; i++) {
        if (isDigit(str[i])) {
            int digit = str[i] - '0';
            count[digit]++;
        }
    }

    // Print the unique digits
    printf("Unique digits: ");
    for (int i = 0; i < 10; i++) {
        if (count[i] == 1) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main() {
    char input[100]; // Assuming a maximum input length of 100 characters

    printf("Enter a string of digits (without spaces): ");
    scanf("%s", input);

    findUniqueDigits(input);

    return 0;
}
