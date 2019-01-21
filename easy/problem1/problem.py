from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.number import getPrime
from keys import flag
import hashlib

#print(hashlib.sha256(flag).hexdigest())
# -> f0bb7f1e352f649bb06e8e65154ea213e486586751b44669b526ec2b124e14fb


def gen_keys(kbits):
    e = 3
    p = getPrime(kbits//2)
    q = getPrime(kbits//2)
    n = p*q 

    return e, n

e, n = gen_keys(2048)
m = bytes_to_long(flag)
while pow(m, e) < n:
    m = (m << 1) + 1

c = pow(m, e, n)
print("e =", e)
print("n =", n)
print("c =", c)
