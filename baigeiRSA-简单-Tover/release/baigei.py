import libnum
from Crypto.Util import number
from secret import flag

size = 128
e = 65537
p = number.getPrime(size)
q = number.getPrime(size)
n = p*q

m = libnum.s2n(flag)
c = pow(m, e, n)

print('n = %d' % n)
print('c = %d' % c)
