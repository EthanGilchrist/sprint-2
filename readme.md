# Simple encrypted messaging shell

WARNING! This program assumes that the receiver will have a private key, but I haven't automated key creation, so this software is currently unusable except to me.
Allows one person (Alice) to send messages encrypted with 2048-bit RSA to another person (Bob), so long as Bob knows Alice's IP address.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Download either program.py (NOT server.py), or client.py
2. Download rsa.py
3. Servers will need to create a public-key.txt file in the same directory as program.py, clients will need to create a private-key.txt file in the same directory as client.py
4. This software is in an unfinished state, and does not automatically produce keys. Currently, I will only be able to give one person a private key.
5. All other files are superfluous/for testing, and I probably should have added them to gitignore

Instructions for using the software (server):

1. Run program.py (either using VS Code or similar software, or by navigating to the directory in the terminal and running "python program.py")
2. If you are doing this for the first time, or if your IP address has reset since the last time the other person ran client.py, you will need to open a terminal, run ```ipconfig``` and look for the line IPv4 address. It should be formatted like this: 123.45.12.89  
the person running client.py will need it.
3. The program will wait for the client to run client.py, and announce when the connection is established.
4. Type in any message. It has a character limit of roughly 500 characters, longer messages will be corrupted by the encryption process. Press enter to send.
5. "Received" will appear if the message was transmitted successfully. You can send as many messages as the other person will tolerate.
6. When you are done, sending the word 'quit' (don't include the quote marks) will close the connection.

Instructions for using the software (client):

1. Run program.py (either using VS Code or similar software, or by navigating to the directory in the terminal and running "python client.py")
2. Enter the IP address of the device running program.py exactly as it appears in ipconfig's output (see step 2 of server instructions). The program will record it to a file. If you run the program again and the other person's IP address hasn't changed, you can press enter to skip this and the program will reuse the stored IP address.
3. The program will decrypt messages as they arrive and log the plaintext in messages.txt, you don't need to create/download this file, it will be created automatically.

## Development Environment

To recreate the development environment, you need Python 3.8 or later to be installed on your computer. I used Visual Studio Code as my editor, but any other editor should work equally well.

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Python Network Programming Tutorial](https://www.youtube.com/playlist?list=PLhTjy8cBISErYuLZUvVOYsR1giva2payF)
* Various pages on StackOverflow, GeeksforGeeks, and W3 Schools
* [Wikipedia's RSA article](https://en.wikipedia.org/wiki/RSA_cryptosystem)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future, in order of priority:

* Automatically create keys when none are found, and a way to distribute public keys. This program is not usable by anyone but me until then.
* Two-way communication
* A central server to manage IP addresses
* Some kind of front-end to make this more user-friendly
* Timestamp logging
* An option to sign messages with the private key as a form of identity verification
* Support for sending files
