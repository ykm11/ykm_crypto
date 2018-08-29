#!/usr/bin/python3
from Crypto.Util.number import bytes_to_long, long_to_bytes
import random
import gmpy
from keys import flag

# 少しMisc (というかTrivia?) が強めの問題です.

f = lambda x: 1 << x
def get_seq():
    for i in range(100):
        p = f(f(i)) + 1
        if gmpy.is_prime(p) == 2:
            yield p
        else:
            yield 0

def xor(data, key):
    key = key*(len(data)//len(key) + 1)
    return bytes([x ^ y for x, y in zip(data, key)])


mul_e = 1
sum_e = 0
for e in get_seq():
    mul_e *= f(e)
    sum_e += f(e)

random.seed(mul_e)
key_length = random.randint(1, len(flag)//2)
random.seed(sum_e)
key = bytes([random.randint(0, 255) for _ in range(key_length)])

ciphertext = xor(flag, key)
print("[+] Ciphertext :", ciphertext.hex())


# [+] Ciphertext : 092e8be045f2c72a3da7c84df2f02303b8c05bd9c4210dbdc961e0ca3d0fabd361f6dd260faff857f5f07957ff9409fb

######
# hashlib.sha1(flag).hexdigest() 
#  -> 53918ccc5318c16aa79fbd8d500c7305f7030ef7
######
