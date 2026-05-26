import math

cheese = 'want to go to rrg tonight? I\'m feeling the vibes and can\'t actually remember if we\'ve seen May\'s burger of the month yet'

# byte can range from 32-126 (95) in normal text, or 0-255 (256) with the full might of unicode
# a degree symbol, for example, is 194 and then 176
def strint(cheese):
    cheeseAsInt = 0
    for byte in cheese.encode():
        byte = int(byte)
        cheeseAsInt *= 256
        cheeseAsInt += byte
        # print(byte)
        # print(cheeseAsInt)
    return cheeseAsInt

# (men)
def intytes(cheese):
    return cheese.to_bytes(int(math.log(cheese) / math.log(256) + 1))

# turns an array of bytes back into an int so math can be done on it
# notice the similarity to strint, which turns a string (array of chars (bytes)) into an int
# but we can't use it here! ok maybe we could, I just get nervous about trying to interpret
# ciphertext as a string since it will be like 20% control characters
def noWaitComeBack(cBytes):
    num = 0
    for byte in cBytes:
        num *= 256
        num += int(byte)
    return num

# expecting byte array from (men) intytes, only exists as two separate functions for debugging purposes
def congeal(cheese):
    message = []
    for byte in cheese: # yum yum
        message.append(str(byte))

# I used OpenSSL instead. Python couldn't handle keys larger than about 24 bits
# def miller():
#     y = 2
#     while y != 1:
#         # pick a large odd number
#         n = random.randint(2**22, 2**23)
#         if n % 2 == 0:
#             n += 1
        
#         # count how many 2s you can factor out of n-1
#         d = n - 1
#         s = 0
#         while (d % 2 == 0):
#             d //= 2
#             s += 1
#         for j in range(5):
#             a = random.randint(2, 42)
#             x = a**d % n
#             print('---')
#             print(n)
#             print('a:' + str(a))
#             print(d)
#             print(x)
#             print('-')
#             for i in range(s):
#                 y = x**2 % n
#                 if (y == 1 and x != 1 and x != n - 1):
#                     print("Composite")
#                     #return
#                 print(x)
#                 x = y
#             print(y)
#             if y != 1:
#                 j = 777
#     print(str(n) + ' is prime!')

def gcd(a, b):
    while True:
        # assume a > b
        if a < b:
            a, b = b, a
        if a % b == 0:
            return b
        a = a - b
        #print(b)

def basicEncrypt(msg, e, n):
    return msg ** e % n

def basicDecrypt(msg, d, n):
    #return msg ** d % n
    return pow(msg, d, n) 
    # This is way faster for some reason. Like, the interpreter was optimizing
    # *something*, because msg**d should definitely overflow, even for python

# turns a string all the way into the kind of byte array that be passed to conn.send()
def superEncrypt(msg):
    pk = getPublicKey()
    n = pk[0]
    e = pk[1]
    cipherNumber = basicEncrypt(strint(msg), e, n)
    return cipherNumber.to_bytes(int(math.log(cipherNumber) / math.log(256) + 1))

# turns a 
def superDecrypt(msg):
    prvKey = getPrivateKey()
    n = prvKey[0]
    d = prvKey[1]
    cipherNum = noWaitComeBack(msg)
    # breath a sigh of relief


# p = 0
# q = 0
# with open('specific-primes.txt') as f:
#     p = int(f.readline())
#     q = int(f.readline())
#     n = p * q

# for now, this assumes you are always talking to the same person. Doing this 
# properly would need a way to identify/load individual keys from a list
def getPublicKey():
    with open('public-key.txt') as f:
        n = int(f.readline())
        e = int(f.readline())
    return (n, e)
pubKey = getPublicKey()
n = pubKey[0]
e = pubKey[1]
def getPrivateKey():
    with open('private-key.txt') as f:
        n = int(f.readline())
        d = int(f.readline())
prvKey = getPrivateKey()
n = prvKey[0]
d = prvKey[1]
# totient = (p - 1) * (q - 1) // gcd(p - 1, q - 1)
# e = 7 # part of the public key
# pow has special behavior when the second argument is -1 that calculates
# the muliplicative inverse instead of the normal behavior of a^b%c
# print('totient')
# print(totient)
# d = pow(e, -1, totient) # private key, used in decryption

# print('\n\nn')
# print(n) # n should be 4096 bits long, or 512 bytes, which is 512 characters. Not the worst character limit.
# print('\n\nd')
# print(d)

# print('\n\nplaintext')
# print(strint(cheese))
# print('\n\nencrypt')
test = basicEncrypt(strint(cheese), e, n)
# print(test)
# print('\n\ndecrypt')
testTwo = basicDecrypt(test, d, n)
testThree = intytes(testTwo)
print(str(testThree, "utf-8"))