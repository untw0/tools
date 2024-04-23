# Creator: @untw0
# GitHub: https://github.com/untw0

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    int number;

    printf("[1] Set User ID [SUID]\n");
    printf("Type the number: ");
    scanf("%d", &number);

    if (numero == 1) {
        system("find / -user root -perm -4000 2>/dev/null");
    } else {
        printf("Invalid Number.\n");
    }

    return 0;
}
