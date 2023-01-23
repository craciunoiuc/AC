import statistics
from binascii import unhexlify
from Crypto.Cipher import AES

from secret_algorithm import frombits

NUM_HASHES = 500000.0
NUM_INDEXES = 128

refs = [0] * NUM_INDEXES

with open('password_hashes.txt') as file:
    for line in file:
        bits = ''.join('{0:0128b}'.format(int(line.rstrip(), 16)))
        for index in range(NUM_INDEXES):
            if (bits[index] == '1'):
                refs[index] += 1

for index in range(len(refs)):
    refs[index] /= NUM_HASHES
    refs[index] *= 100

mean = statistics.mean(refs) - 0.25
stdev = statistics.stdev(refs)

print('Mean:\t' + str(mean))
print('Stdev:\t' + str(stdev))

key = ''
for index in range(len(refs)):
    if (abs(refs[index] - mean) < stdev):
        key += '0'
    else:
        key += '1'

key = frombits(key)

hex_key = ''.join('{:02x}'.format(ord(c)) for c in key)
print('Key:\t' + str(hex_key))

with open('top_secret.txt') as f:
    ct = unhexlify(f.read().rstrip())

cipher = AES.new(key, AES.MODE_ECB)

print(cipher.decrypt(ct))

