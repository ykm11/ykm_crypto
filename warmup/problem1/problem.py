from Crypto.Util.number import getPrime
from Crypto.Util.number import long_to_bytes, bytes_to_long
from keys import flag

f = lambda x : 1 << x
def gen_n():
    n = 1
    for _ in range(10):
        n *= getPrime(32)
    return n

m = bytes_to_long(flag)
e = f(f(4)) + 1
n = gen_n()
assert m < n

c = pow(m, e, n)
print("[+] PubKey n :", n)
print("[+] Ciphertext :", c)


# [+] PubKey n : 124701204772866527839947419275988972781214251222197960024452995699915038677583513397635137564841
# [+] Ciphertext : 86095122501042082938111072789119002457347809374924931685221769488126539342236861320400009092453
