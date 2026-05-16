import socket
import os
import subprocess
import requests
import io

#s = socket.socket()
#host = '104.236.209.167'
#port = 9999

#s.connect((host, port))

url = "https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json"
response = requests.get(url)

# Socket commands in Python:
#socket.socket()
#s.bind(host, port)
#s.send()
#s.listen()
#s.recv()
#s.close()