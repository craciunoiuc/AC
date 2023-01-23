#!/usr/bin/python3

from base64 import b64decode, b64encode
import json
import requests
from randcrack import RandCrack

MAGIC_NUMBER = 624

def xor(a: bytes, b: bytes) -> bytes:
    """ Performs the XOR operation. """
    return bytes([ai ^ bi for ai, bi in zip(a, b)])

rc = RandCrack()

pt = b'a' * MAGIC_NUMBER * 4
payload = {'payload': b64encode(pt)}
r = requests.post('http://141.85.224.119:8080/encrypt', json=payload)

ct = b64decode(r.text)

rand_ints = []
for i in range(MAGIC_NUMBER):
    rand_ints.append(int.from_bytes(ct[i * 4 : (i + 1) * 4], 'little') ^ 0x61616161)

for rand_int in rand_ints:
    rc.submit(rand_int)

prediction = int.to_bytes(rc.predict_getrandbits(8 * 44), 44, 'little')
print(xor(prediction, ct[MAGIC_NUMBER * 4:]))

