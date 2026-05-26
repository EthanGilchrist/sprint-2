# I'm splitting this off into a seperate file because I can't yet tell if I want this functionality or not.
import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
que = Queue()
all_connections = []
all_addresses = []

# Create a socket (connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
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

# Handling connections from multiple clients and saving to a list
# Closing previous connections when server.py is restarted

def accepting_connections():
    for c in all_connections:
        c.close()
    
    del all_connections[:]
    del all_addresses[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1) # prevents timeout

            all_connections.append(conn)
            all_addresses.append(address)
            print("Connection established: " + address[0])

        except:
            print("Error accepting connections")

# 2nd thread functions - 1) See all the clients 2) Select a client 3) Send commands to the connected client
# Interactive prompt for sending commands
# turtle> list
# 1 Friend-A
# 2 Friend-B
# 3 Friend-C

def start_turtle():
    cmd = input('turtle> ')

    if cmd == 'list':
        list_connections()
    
    elif 'select' in cmd:
        def get_target(cmd):
            pass
        conn = get_target(cmd) # Not yet implemented
        if conn is not None:
            def send_target_commands(conn):
                pass
            send_target_commands(conn) # Not yet implemented
    else:
        print('Command not recognized')


# Display all current active connections with the client

def list_connections():
    results = ''

    for i,conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(201480)
        except:
            del all_connections[i]
            del all_addresses[i]
            continue

        results = str(i) + "  " + str(all_addresses[i][0]) + "  " + str(all_addresses[i][1]) + '\n'
    
    print("---- Clients ----" + "\n" + results)




















































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
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

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

# off-topic testing, you can run this in the blink of an eye:
#import sys
#sys.set_int_max_str_digits(1000000000)
#3**1000000
# this produces a number that I do not believe can be pronounced in English except to read off the digits.