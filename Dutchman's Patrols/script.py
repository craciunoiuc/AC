#!/usr/bin/python3

from base64 import b64encode, b64decode
from pwn import *

# This script attempts to brute-force a 16-byte key used
# for a cipher by sending 8192 requests containing 16-byte blocks
# of 0x00 bytes and recording the response from the server.


TRIES = 8192 # Set the number of requests
BLOCK_LEN = 16 # Set the length of the blocks in bytes

payload = {'plaintext': b64encode(b'\x00' * BLOCK_LEN * TRIES)}
# Generating a payload of 8192 blocks of 0x00 bytes encoded in base64.
r = remote('141.85.224.119', 31338).post('/', json=payload)
response = b64decode(r.text)

my_dicts = []
for i in range(BLOCK_LEN):
    my_dicts.append({})

i = 0
while i < TRIES:
    ct = response[i * 16 : (i + 1) * 16] # Extracting a 16 bytes block from the response    
    for pos in range(BLOCK_LEN):
        char = chr(ct[pos]) # Converting a byte into a character 
        if 0x21 <= ord(char) and ord(char) <= 0x7a: # Check if the character is in the range of ascii characters
            if char not in my_dicts[pos]:
                my_dicts[pos][char] = 0
            else:
                my_dicts[pos][char] += 1
    i += 1

key = ''
i = 0
while i < BLOCK_LEN:
    # Sort the dictionary based on the frequency of the characters
    key += sorted(my_dicts[i].items(), key=lambda item: item[1], reverse=True)[0][0]
    i += 1

print(key)
