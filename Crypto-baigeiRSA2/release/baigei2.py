import libnum
from Crypto.Util import number
from functools import reduce
from secret import flag

n = 5
size = 64
while True:
    ps = [number.getPrime(size) for _ in range(n)]
    if len(set(ps)) == n:
        break

e = 65537
n = reduce(lambda x, y: x*y, ps)
m = libnum.s2n(flag)
c = pow(m, e, n)

print('n = %d' % n)
print('c = %d' % c)
