from gmpy2 import invert
from functools import reduce
import libnum

e = 65537
n = 175797137276517400024170861198192089021253920489351812147043687817076482376379806063372376015921
c = 144009221781172353636339988896910912047726260759108847257566019412382083853598735817869933202168

# from yafu
ps = [
    9401433281508038261,
    10252499084912054759,
    11855687732085186571,
    13716847112310466417,
    11215197893925590897
]
phi = reduce(lambda x, y: (x)*(y-1), [1]+ps)
d = invert(e, phi)
m = pow(c, d, n)
flag = libnum.n2s(int(m))
print(flag)