from Crypto.PublicKey import RSA
import base64
import gmpy
from Crypto.Util.number import *

with open('alice.pubkey','r') as f:
    alice_key_pub = RSA.importKey(f.read()) #import Alice RSA Public Key

with open('bob.pubkey','r') as f:
    bob_key_pub = RSA.importKey(f.read()) #import Bob RSA Public Key

p = gmpy.gcd(alice_key_pub.n,bob_key_pub.n) #Calculate the Greatest Common Divisor of the two n's from the keys

q1 = alice_key_pub.n/p
q2 = bob_key_pub.n/p

phi1 = (p-1)*(q1-1)
phi2 = (p-1)*(q2-1)
d1 = gmpy.invert(alice_key_pub.e,phi1)
d2 = gmpy.invert(bob_key_pub.e,phi2)

with open('for_alice.enc', 'r') as f:
    message_1 = base64.b64decode(f.read())# decode the message for Alice

with open('for_bob.enc', 'r') as f:
    message_2 = base64.b64decode(f.read()) #decode the message for Bob

print(long_to_bytes(pow(bytes_to_long(message_1),d1,alice_key_pub.n)),
      long_to_bytes(pow(bytes_to_long(message_2),d2,bob_key_pub.n)))
#convert the decrypted messages to bytes
