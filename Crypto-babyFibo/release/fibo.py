import os
import libnum
from secret import flag

def fibo(n):
    assert n >= 0
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

s = fibo(1000)
m = libnum.s2n(flag+os.urandom((len(bin(s))-2)//8-len(flag)))
c = m^s
print(c)
