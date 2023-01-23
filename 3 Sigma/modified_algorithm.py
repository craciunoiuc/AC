import hmac
    
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def my_hash(k, m):
    k_bits = tobits(k)
    print(k_bits)
    print(len(k_bits))
    s_bits = []
    for i in xrange(len(k_bits)):
        h = hmac.new(k, m + str(i)).digest()

        if (k_bits[i] == 1 or ord(h[-1]) < 127):
            s_bits.append(ord(h[-1]) % 2)
        else:
            s_bits.append(1 - ord(h[-1]) % 2)
        
    sgn = frombits(s_bits)
    return sgn
