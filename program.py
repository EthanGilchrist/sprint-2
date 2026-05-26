# server side of the tutorial (https://www.youtube.com/watch?v=WitopEiN3IQ&list=PLhTjy8cBISErYuLZUvVOYsR1giva2payF&index=9)
# it actually works!!!1!11!
import socket
import sys
import os
import subprocess
import requests
import io
import rsa

# Create a socket (connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        print('Creating socket')
        s = socket.socket()
    except socket.error as msg:
        print('Socket creation error: ' + str(msg))

# Binding the socket and listening for connections
def bind_socket(n = 0):
    try:
        global host
        global port
        global s
        print('Binding the port: ' + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print('Socket binding error: ' + str(msg) + '\nRetrying')
        if (n < 10):
            bind_socket(n + 1)

# Establish connection with a client (socket must be listening)
def accept_socket():
    print("Waiting for client...")
    conn,address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            #conn.send(str.encode(cmd))
            conn.send(rsa.encrypt(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response)
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            #conn.send(str.encode(cmd))
            conn.send(rsa.encrypt(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response)

def main():
    create_socket()
    bind_socket()
    accept_socket()

main()


#s = socket.socket()
#host = '104.236.209.167'
#port = 9999

#s.connect((host, port))

#url = "https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json"
#response = requests.get(url)

# Socket commands in Python:
#socket.socket()
#s.bind(host, port)
#s.send()
#s.listen()
#s.recv()
#s.close()