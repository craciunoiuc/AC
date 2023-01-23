from Crypto.PublicKey import RSA
import base64

FLAG = "-- redacted --"
alice_key = "-- redacted --"
bob_key   = "-- redacted --"

message_for_alice = FLAG[:len(FLAG)/2]
message_for_bob   = FLAG[len(FLAG)/2:]

for_alice_encrypted = alice_key.publickey().encrypt(message_for_alice, 1)[0]
for_bob_encrypted   = bob_key.publickey().encrypt(message_for_bob, 1)[0]

message_1 = base64.b64encode(for_alice_encrypted)
message_2 = base64.b64encode(for_bob_encrypted)

f = open('for_alice.enc', 'w')
f.write(message_1+'\n')
f.close()

f = open('for_bob.enc', 'w')
f.write(message_2+'\n')
f.close()

f = open('alice.pubkey', 'w')
f.write(alice_key.publickey().exportKey())
f.close()

f = open('bob.pubkey', 'w')
f.write(bob_key.publickey().exportKey())
f.close()
