#!/usr/bin/python3

import string

alphabet = string.ascii_lowercase[:16]

flag_enc = "ppbkakbjbkcpakcnbkbhbhakcebkcacnakbkccbjakbocnceclcpbknm"

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

def unshift(c, k):
    return alphabet[(ord(c) - ord("a") - ord(k) + ord("a")) % len(alphabet)]

for key in alphabet:
    unshifted_flag_enc = ''
    for i, c in enumerate(flag_enc):
        unshifted_flag_enc += unshift(c, key[i % len(key)])
    flag = ''
    for (c1, c2) in pairwise(unshifted_flag_enc):
        binary = "{0:04b}".format(ord(c1) - ord('a')) + "{0:04b}".format(ord(c2) - ord('a'))
        flag += chr(int(binary, 2))
    print(flag)
