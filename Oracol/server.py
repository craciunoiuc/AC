import base64 

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad

with open('flag.txt') as f:
    flag = f.read().strip()


KEY_LENGTH = 16  # AES128
BLOCK_SIZE = AES.block_size

_random_gen = Random.new()
_key = _random_gen.read(KEY_LENGTH)
iv = _random_gen.read(AES.block_size)


def _pad(msg):
    return pad(msg,BLOCK_SIZE)


def _unpad(data):
    return unpad(data,BLOCK_SIZE)


def encrypt(msg):
    cipher = AES.new(_key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(_pad(bytes(msg,'utf-8')))


def _decrypt(data):
    data = base64.b64decode(data)
    try:
    	iv = data[:BLOCK_SIZE]
    	cipher = AES.new(_key, AES.MODE_CBC, iv)
    except:
    	print("Bad IV.")
    	exit()
    try:
        r = _unpad(cipher.decrypt(data[BLOCK_SIZE:]))
        return True
    except ValueError as v:
        return False


def is_padding_ok(data):
    return _decrypt(data) is True



def menu():
    print("All messages are encrypted with symmetric key in CBC mode.")
    cmd = '9'
    while cmd != '0':
        print("1. Receive message")
        print("2. Send message")
        cmd = input("Option: ").strip()
        if cmd == '1':
            enc = base64.b64encode(encrypt(flag))

            print('Msg:', enc.decode('utf-8'))
        elif cmd == '2':
            cipher = input('Msg:').strip()
            if is_padding_ok(cipher):
                print('Ok.')
            else:
                print('Padding seems invalid')
        else:
            exit()
        print()

if __name__ == '__main__':
    menu()
