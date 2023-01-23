import random
from base64 import b64decode, b64encode

from fastapi import FastAPI
from pydantic import BaseModel


class Request(BaseModel):
    payload: bytes


def xor(a: bytes, b: bytes) -> bytes:
    """ Performs the XOR operation. """
    return bytes([ai ^ bi for ai, bi in zip(a, b)])


def generate_key(rnd: random.Random, length: int) -> bytes:
    """ Generates a random key of `length` bytes each call """
    return int.to_bytes(rnd.getrandbits(8 * length), length, 'little')


flag = open("flag.txt", 'rt').read().strip()
app = FastAPI()


@app.post("/encrypt")
def encrypt(request: Request) -> bytes:
    msg = b64decode(request.payload)
    msg = msg + bytes(flag, 'utf8')

    key = generate_key(random.Random(), len(msg))
    ciphertext = xor(key, msg)

    return b64encode(ciphertext)
