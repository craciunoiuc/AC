#!/usr/bin/env python3
from pwn import *
import base64

BLOCK_SIZE = 16
IP   = "141.85.224.119"
PORT = "1337"

def check_cbcpad(ct, c0): # check is the ciphertext is valid
    session.recv()
    session.sendline("2")
    session.recv()

    session.sendline(base64.b64encode(c0 + ct).decode('utf-8'))
    r = session.recvline().strip()

    if 'Ack.' in str(r): # check the connectivity to the server
        return True
    return False

session = remote(IP, PORT)

print("-Getting the encrypted flag-")
session.recv() # garbage stuff
session.sendline("1") # get flag encoded in base64
session.recvuntil("The message is: ") # more garbage stuff

coded_flag = session.recvline().strip() # get the encrypted flag
ct = base64.b64decode(coded_flag)
print(coded_flag) # very important

c0 = bytearray(ct[:BLOCK_SIZE]) # get the initialization vector from the ciphertext
my_ct = bytearray(ct[BLOCK_SIZE:]) # get the rest of the ciphertext
plaintext = b''

print("IV: " + bytes.hex(ct[:BLOCK_SIZE]) + " Flag: " + bytes.hex(ct[BLOCK_SIZE:]))

print("--Decrypting the flag--")
index = 0
while index < len(my_ct) // BLOCK_SIZE:
    C2 = my_ct[BLOCK_SIZE * index : BLOCK_SIZE * (index + 1)]
    if index != 0:
        C1 = my_ct[BLOCK_SIZE * (index - 1) : BLOCK_SIZE * index]
    else:
        C1 = bytearray(c0)

    Cp1 = bytearray([0] * BLOCK_SIZE)
    decrypted_block = b''
    counter = 1
    while counter <= BLOCK_SIZE:
        print(counter)
        item = 0
        while item < 256:
            Cp1[BLOCK_SIZE - counter] = item
            if check_cbcpad(C2, Cp1):
                I2 = item ^ counter
                msg_chr = C1[BLOCK_SIZE - counter] ^ I2
                decrypted_block += bytes(chr(msg_chr), 'utf-8')
                i = 0
                while i < counter:
                    Cp1[BLOCK_SIZE - counter + i] = (counter + 1) ^ Cp1[BLOCK_SIZE - counter + i] ^ counter
                    i += 1
                break
            item += 1
        counter += 1

    decrypted_block = decrypted_block[::-1]
    print(decrypted_block)

    plaintext += decrypted_block
    index += 1
    
print("The decrpyted flag is: ")
print(plaintext)

