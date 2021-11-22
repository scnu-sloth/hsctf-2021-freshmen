import random
import libnum
from Crypto.Util import number
from gmpy2 import gcd
from secret import flag
assert len(flag) == 43
flag = [flag[(43//3)*i:(43//3)*(i+1)] for i in range(3)]

print('--- Part. 0 ---')
x0 = libnum.s2n(flag[0][:len(flag[0])//2])
y0 = libnum.s2n(flag[0][len(flag[0])//2:])
print('Hint: %d' % gcd(x0, y0))
l0 = len(bin(y0))-2
while True:
    a0 = random.randint(2, 2**(l0*3))
    b0 = random.randint(2, 2**(l0*3))
    if a0*x0 == b0*y0:
        break
# 2000/3 years later ...
print('a0 = %d' % a0)
print('b0 = %d' % b0)

print('--- Part. 1 ---')
x1 = libnum.s2n(flag[1][:len(flag[1])//2])
y1 = libnum.s2n(flag[1][len(flag[1])//2:])
print('Hint: %d' % gcd(x1, y1))
l1 = len(bin(y1))-2
while True:
    a1 = random.randint(2, 2**(l1*3))
    b1 = random.randint(2, 2**(l1*3))
    if a1*x1 - b1*y1 == 1:
        break
# 2000/3 years later ...
print('a1 = %d' % a1)
print('b1 = %d' % b1)

print('--- Part. 2 ---')
x2 = libnum.s2n(flag[2][:len(flag[2])//2])
y2 = libnum.s2n(flag[2][len(flag[2])//2:])
print('Hint: %s' % 'nicai')
l2 = len(bin(y2))-2
while True:
    a2 = random.randint(2, 2**(l2*3))
    b2 = random.randint(2, 2**(l2*3))
    if a2*x2 - b2*y2 <= y2:
        break
# 2000/3 years later ...
print('a2 = %d' % a2)
print('b2 = %d' % b2)

