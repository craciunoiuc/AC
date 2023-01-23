import string

alphabet = string.ascii_lowercase[:16]

flag = "redacted"
key = "redacted" # key is a character from alphabet

def shift(c, k):
	return alphabet[(ord(c) - ord("a") + ord(k) - ord("a")) % len(alphabet)]

def encode(plaintext):
	enc = ""
	for c in plaintext:
		binary = "{0:08b}".format(ord(c))
		enc += alphabet[int(binary[:4], 2)]
		enc += alphabet[int(binary[4:], 2)]
	return enc

flag_enc = ""
for i, c in enumerate(encode(flag)):
	flag_enc += shift(c, key[i % len(key)])
print(flag_enc)