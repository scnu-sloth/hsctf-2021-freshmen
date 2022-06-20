# Python3

import sys
import getopt
import re
from ctypes import *
import libnum
import pycipher
from Crypto.Cipher import AES

SECRET = 'tover'

def check0(_arr, _opt):
    s = '-' + '-'.join(list(SECRET))
    keys = re.findall(r'\D{1,2}', s)
    values = [x for x in range(5)]
    dic = dict(zip(keys, values))
    if _arr != list(SECRET[:dic[_opt]]):
        return False
    else:
        return True

def check_t(_arg):
    if len(_arg) != 2:
        return False
    m = _arg.join([SECRET for _ in range(2)])[:8]
    key = (SECRET * 4)[::-1][:16]
    key = [int.from_bytes(x.encode(), byteorder = 'little') for x in re.findall(r'\D{1,4}', key)]
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
    Tea_c = v0.value.to_bytes(4, byteorder = 'little') + v1.value.to_bytes(4, byteorder = 'little')
    if Tea_c == b'l\x87\xa1\xa9\xa7+}\xc6':
        return True
    else:
        return False

def check_o(_arg):
    if len(_arg) != 4:
        return False
    for x in _arg:
        if x not in "_abcdefghijklmnopqrstuvwxyz":
            return False
    m = libnum.s2n(_arg)
    pk = (1528616880549194448420945706601072269159367149530762512566327375647880927486034128110021259979044315726550632429668598339632027482804601602403127472749317557334728257063028214617207353439820521429091372949884765149334050209897934832333515106331460550092970771112622841320399021140810416128660655466854842792150060121100023354238809598512279353342681070829602527069530742206293607227455794799797672571758661774672518315811989554711967176357426090059582555971388651, 1426167301291907286926023915605571967443114988315299166574033826450605747351312506798440886660222257698650441552306885083474365268131272868509213574099800265189286080702850161860219859172739922356469661224324652721867586240400231118063596215137027867667774198900195582428699179540812043600904756090969452851891360816130465135086887086881670519531627539814800157796473604632625409935088389987550849676207219783775254080098911935147111584778597070066073677761334477, 591674724561668755728322751926990676306758645358328397115461821209558160140628469192035947186096059207749734608197433933389385066261999421731704120794590222131330959575673087164746978939337274505748925133552369137134935602727004018950865615444138762917387300414384653374786623694607607096258261314497157365118984609656920631714450894476808119558813837477737698416802297654544754439413253078119132023091628700535438694279784328865026475446926183693354595146241902)
    n, g, h = pk
    # r = random.randint(1, n-1)
    r = libnum.s2n(SECRET)
    Okamoto_c = pow(g, m, n)*pow(h, r, n) % n
    if Okamoto_c == 359053573717528865803856591767004734466567090055207274737763778917577132985386943985817751727788015489937605490329044071764551363803097309363973422067990053916916130357209864415338778758512312415977343187186430924270774808345175971158184249001320796666415105688618795555370693020647563970778631649034843878683229100576403802181913661046922070997072175067938581927551823546206124766044351042645678934099553543680743099561583519474297394751716938708369189407822206:
        return True
    else:
        return False

def check_v(_arg):
    if len(_arg) != 8:
        return False
    if _arg[3] != '_':
        return False
    if _arg.islower() != True:
        return False
    m = _arg.replace('_', '')
    Vigenere_c = pycipher.Vigenere(SECRET).encipher(m)
    if Vigenere_c == "GCRAYTH":
        return True
    else:
        return False

def check_e(_arg):
    if len(_arg) != 16:
        return False
    arr = [1, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 1, 0]
    m = ""
    for i in range(len(_arg)):
        if arr[i] == 0:
            if _arg[i].islower() != True:
                return False
            m += _arg[i].upper()
        elif arr[i] == 1:
            if _arg[i] != '_':
                return False
        elif arr[i] == 2:
            if _arg[i].isupper() != True:
                return False
            m += _arg[i]
    Enigma_c = pycipher.Enigma(settings = ('A', 'A', 'A'), rotors = (1, 2, 3), reflector = 'B', ringstellung = ('F', 'V', 'N'), steckers = [('P', 'O'), ('M', 'L'), ('I', 'U'), ('K', 'J'), ('N', 'H'), ('Y', 'T'), ('G', 'B'), ('V', 'F'), ('R', 'E'), ('D', 'C')]).encipher(m)
    if Enigma_c == "FSAPWYKMEJYG":
        return True
    else:
        return False

def check_r(_arg):
    if len(_arg) != 16:
        return False
    m = _arg.encode()
    aes = AES.new((SECRET * 4)[:16].encode(), AES.MODE_ECB)
    Rijndael_c = aes.encrypt(m)
    if Rijndael_c == b'LqxF\xe0\xcf\xa8}4<\x83z\xc8d\xc6\xd5':
        return True
    else:
        return False

def wrong():
    print("Learn more about 'getopt' and read this python code carefully, and then you will know what's wrong~")
    sys.exit(-1)

if __name__ == '__main__':
    opt_visited = []

    try:
        opts, args = getopt.getopt(sys.argv[1:], ''.join([x + ':' for x in SECRET]))
    except getopt.GetoptError:
        wrong()
    if len(opts) != 5 or args != []:
        wrong()

    for opt, arg in opts:
        if check0(opt_visited, opt) == False:
            wrong()
        opt_visited.append(opt[1])
        check_function = eval('check_' + opt[1])
        if check_function(arg) == False:
            wrong()

    flags = [t[1] for t in opts]
    print('Congratulations~ You get the flag: flag{{{0}{1}{2}{3}{4}}} =v='.format(*flags))