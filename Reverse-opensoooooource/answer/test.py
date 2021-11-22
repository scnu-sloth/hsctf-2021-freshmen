from ctypes import *
import re
from Crypto.Util import number
from gmpy2 import invert
import libnum
import pycipher
from Crypto.Cipher import AES

SECRET = 'tover'
flag = 'd0_u_know_what_the_SECRET_is_ju5t_534rch_tha7!'
size_t = 2
size_o = 4
size_v = 8
size_e = 16
size_r = 16
assert size_t + size_o + size_v + size_e + size_r == len(flag)

tmp = 0
ttt = flag[tmp:tmp+size_t]
tmp += size_t
ooo = flag[tmp:tmp+size_o]
tmp += size_o
vvv = flag[tmp:tmp+size_v]
tmp += size_v
eee = flag[tmp:tmp+size_e]
tmp += size_e
rrr = flag[tmp:tmp+size_r]

s = '-' + '-'.join(list(SECRET))
keys = re.findall(r'\D{1,2}', s)
arr = [ttt, ooo, vvv, eee, rrr]
for i in range(5):
    print(keys[i], arr[i], end = ' ')

## t: tea
print(ttt)
m = ttt.join([SECRET for _ in range(2)])[:8]
print(m)
key = (SECRET * 4)[::-1][:16]
key = [int.from_bytes(x.encode(), byteorder = 'little') for x in re.findall(r'\D{1,4}', key)]
print(key)
v0 = int.from_bytes(m[:4].encode(), byteorder = 'big')
v1 = int.from_bytes(m[4:].encode(), byteorder = 'big')
v0, v1 = c_uint32(v0), c_uint32(v1)
delta = 0x9e3779b9
k0, k1, k2, k3 = key
total = c_uint32(0)
for i in range(32):
    total.value += delta 
    v0.value += ((v1.value<<4) + k0) ^ (v1.value + total.value) ^ ((v1.value>>5) + k1)  
    v1.value += ((v0.value<<4) + k2) ^ (v0.value + total.value) ^ ((v0.value>>5) + k3)
c = v0.value.to_bytes(4, byteorder = 'little') + v1.value.to_bytes(4, byteorder = 'little')
print(c)
v0, v1 = c_uint32(int.from_bytes(c[:4], byteorder = 'little')), c_uint32(int.from_bytes(c[4:], byteorder = 'little'))
total = c_uint32(delta * 32)
for i in range(32):                       
    v1.value -= ((v0.value<<4) + k2) ^ (v0.value + total.value) ^ ((v0.value>>5) + k3) 
    v0.value -= ((v1.value<<4) + k0) ^ (v1.value + total.value) ^ ((v1.value>>5) + k1)  
    total.value -= delta
m2 = v0.value.to_bytes(4, byteorder = 'big') + v1.value.to_bytes(4, byteorder = 'big')
m2 = m2[5:7]
print(m2)


## o: Okamoto
# m < p
print(ooo)
def enc(pk, m):
    n, g, h = pk
    # r = random.randint(1, n-1)
    r = libnum.s2n(SECRET)
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
pk = (1528616880549194448420945706601072269159367149530762512566327375647880927486034128110021259979044315726550632429668598339632027482804601602403127472749317557334728257063028214617207353439820521429091372949884765149334050209897934832333515106331460550092970771112622841320399021140810416128660655466854842792150060121100023354238809598512279353342681070829602527069530742206293607227455794799797672571758661774672518315811989554711967176357426090059582555971388651, 1426167301291907286926023915605571967443114988315299166574033826450605747351312506798440886660222257698650441552306885083474365268131272868509213574099800265189286080702850161860219859172739922356469661224324652721867586240400231118063596215137027867667774198900195582428699179540812043600904756090969452851891360816130465135086887086881670519531627539814800157796473604632625409935088389987550849676207219783775254080098911935147111584778597070066073677761334477, 591674724561668755728322751926990676306758645358328397115461821209558160140628469192035947186096059207749734608197433933389385066261999421731704120794590222131330959575673087164746978939337274505748925133552369137134935602727004018950865615444138762917387300414384653374786623694607607096258261314497157365118984609656920631714450894476808119558813837477737698416802297654544754439413253078119132023091628700535438694279784328865026475446926183693354595146241902)
sk = (12178097339658641075368188346022998650287779140999521579165105915910795676456937126848325610738044087399551744452607283454696252942896490992555018202998827, 10307177832113861502562727844451845929289336425492576317503412473645191326275018045703968479629363802507521314766693905761016588167913895518567145596574019)
m = libnum.s2n(ooo)
# charset = "_abcdefghijklmnopqrstuvwxyz"
# for x1 in charset:
#     for x2 in charset:
#         for x3 in charset:
#             for x4 in charset:
#                 m = libnum.s2n(x1 + x2 + x3 + x4)
#                 if enc(pk, m) == 359053573717528865803856591767004734466567090055207274737763778917577132985386943985817751727788015489937605490329044071764551363803097309363973422067990053916916130357209864415338778758512312415977343187186430924270774808345175971158184249001320796666415105688618795555370693020647563970778631649034843878683229100576403802181913661046922070997072175067938581927551823546206124766044351042645678934099553543680743099561583519474297394751716938708369189407822206:
#                     print(x1 + x2 + x3 + x4)
c = enc(pk, m)
print('c = %d' % c)
m2 = dec(pk, sk, c)
print('m = %d' % m2)

## v: Vigenere
print(vvv)
m = vvv.replace('_', '')
print(m)
c = pycipher.Vigenere(SECRET).encipher(m)
print(c)
m2 = pycipher.Vigenere(SECRET).decipher(c)
print(m2)

## e: Enigma
print(eee)
m = eee.replace('_', '').replace('?', '').upper()
print(m)
c = pycipher.Enigma(settings = ('A', 'A', 'A'), rotors = (1, 2, 3), reflector = 'B', ringstellung = ('F', 'V', 'N'), steckers = [('P', 'O'), ('M', 'L'), ('I', 'U'), ('K', 'J'), ('N', 'H'), ('Y', 'T'), ('G', 'B'), ('V', 'F'), ('R', 'E'), ('D', 'C')]).encipher(m)
print(c)
m2 = pycipher.Enigma(settings = ('A', 'A', 'A'), rotors = (1, 2, 3), reflector = 'B', ringstellung = ('F', 'V', 'N'), steckers = [('P', 'O'), ('M', 'L'), ('I', 'U'), ('K', 'J'), ('N', 'H'), ('Y', 'T'), ('G', 'B'), ('V', 'F'), ('R', 'E'), ('D', 'C')]).decipher(c)
print(m2)

## r: AES(Rijndael)
print(rrr)
m = rrr.encode()
aes = AES.new((SECRET * 4)[:16].encode(), AES.MODE_ECB)
rijndael_c = aes.encrypt(m)
print(rijndael_c)
m2 = aes.decrypt(rijndael_c)
print(m2)