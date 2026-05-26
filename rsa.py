import math

# This is the cleaned up version of my original rsa.py file, which has been moved to a separate file.
# Trust me when I say that this is quite the makeover.

# first step in encryption, turn plaintext into a large number, ready to be encrypted
def string_to_int(text):
    num = 0
    for byte in text.encode():
        byte = int(byte)
        num *= 256
        num += byte
    return num

# prepare encrypted number so that conn.send() can send it
def int_to_byte_array(num):
    return num.to_bytes(int(math.log(num) / math.log(256) + 1))

# converts array of bytes received from conn.recv() back into an int, ready to be decrypted
def byte_array_to_int(byte_arr):
    num = 0
    for byte in byte_arr:
        num *= 256
        num += int(byte)
    return num

def encrypt(msg):
    # load public key
    with open('public-key.txt') as f:
        n = int(f.readline())
        e = int(f.readline())
    # encode plaintext as a large integer and encrypt it
    cipherNumber = pow(string_to_int(msg), e, n)
    # convert int into array of bytes ready to pass to conn.send()
    return cipherNumber.to_bytes(int(math.log(cipherNumber) / math.log(256) + 1))

def decrypt(msg):
    # load private key
    with open('private-key.txt') as f:
        n = int(f.readline())
        d = int(f.readline())
    # turn input stream back into an int
    cipherNum = byte_array_to_int(msg)
    # decrypt
    plainNum = pow(cipherNum, d, n)
    # convert int into an array of bytes encoded in utf-8, then decode
    return str(int_to_byte_array(plainNum), "utf-8")