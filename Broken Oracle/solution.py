#!/usr/bin/python3

import requests

BLOCK_SIZE = 16

def check_cbcpad(ct, m0, c0):
    r = requests.get('http://141.85.224.119:1338/api/send_msg/{}/{}/{}'.format(ct.hex(), m0.hex(), c0.hex()))
    if 'msg' in r.json():
        return True
    return False

r = requests.get('http://141.85.224.119:1338/api/encrypt_flag')
ct = bytes.fromhex(r.json()['ciphertext'])
m0 = bytes.fromhex(r.json()['m0'])
c0 = bytes.fromhex(r.json()['c0'])

my_ct = bytearray(ct)
last_decrypted_block = m0
plaintext = b''

for index in range(len(my_ct) // BLOCK_SIZE):
    C2 = my_ct[BLOCK_SIZE * index : BLOCK_SIZE * (index + 1)]
    if index != 0:
        C1 = my_ct[BLOCK_SIZE * (index - 1) : BLOCK_SIZE * index]
    else:
        C1 = bytearray(c0)

    Cp1 = bytearray([0] * BLOCK_SIZE)
    decrypted_block = b''
    for counter in range(1, BLOCK_SIZE + 1):
        print(counter)
        for item in range(256):
            Cp1[BLOCK_SIZE - counter] = item
            if check_cbcpad(C2, last_decrypted_block, Cp1):
                I2 = item ^ counter
                msg_chr = C1[BLOCK_SIZE - counter] ^ I2
                decrypted_block += bytes(chr(msg_chr), 'utf-8')
                for i in range(counter):
                    Cp1[BLOCK_SIZE - counter + i] = (counter + 1) ^ Cp1[BLOCK_SIZE - counter + i] ^ counter
                break

    decrypted_block = decrypted_block[::-1]
    print(decrypted_block)

    last_decrypted_block = decrypted_block
    plaintext += decrypted_block

print(plaintext)

