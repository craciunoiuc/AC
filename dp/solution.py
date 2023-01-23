#!/usr/bin/python3

from Crypto.PublicKey import RSA
from Crypto.Util.number import *

dp = 110994758548722324483657994563964656305785502786367319736582084247408222943577135331157032007077240724782230130503004614185668489500737553661726585497201927503761178109990874060764818429576943932718401199776056068046838186110680106052046316193952149356896460992110239899724832291779649120485582739156757125385

key = RSA.import_key(open('public.pem', 'r').read())
ciphertext = int(open('c.txt', 'r').read())

for k in range(2, key.e):
    test_p = (key.e * dp - 1 + k) // k
    if key.n % test_p == 0:
        p = test_p
        break

q = key.n // p

th = (p - 1) * (q - 1)

d = pow(key.e, -1, th)

plaintext = pow(ciphertext, d, key.n)

print(long_to_bytes(plaintext))

