import libnum
from Crypto.Util import number
from secret import flag


size = 256
e = 65537
p = number.getPrime(size)
q = number.getPrime(size)
avg = (p+q)/2
n = p*q

m = libnum.s2n(flag)
c = pow(m, e, n)

print('n = %d' % n)
print('avg = %d' % avg)
print('c = %d' % c)
