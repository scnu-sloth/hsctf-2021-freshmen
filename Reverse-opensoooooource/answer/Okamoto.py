from Crypto.Util import number
from gmpy2 import invert
import random

def gen(bits=512):
    p = number.getPrime(bits)
    q = number.getPrime(bits)
    n = p*p*q
    while True:
        g = random.randint(2, n-1)
        if pow(g, p-1, p*p) != 1:
            h = pow(g, n, n)
            return ((n, g, h), (p, q))

# m < p
def enc(pk, m):
    n, g, h = pk
    r = random.randint(1, n-1)
    c = pow(g, m, n)*pow(h, r, n) % n
    return c

def dec(pk, sk, c):
    n, g, h = pk
    p, q = sk
    a = (pow(c, p-1, p*p) - 1) // p
    b = (pow(g, p-1, p*p) - 1) // p
    bp = invert(b, p)
    m = a*bp % p
    return m

if __name__ == '__main__':
    pk, sk = gen()
    m = 5201314
    c = enc(pk, m)
    print('c = %d' % c)
    m2 = dec(pk, sk, c)
    print('m = %d' % m2)