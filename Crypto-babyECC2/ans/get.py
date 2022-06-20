
c = 'ac73a774a25bd512d543dc468542c9428141800dd041d043c918d112850dd515d6128214d1138211d71599'
c = bytes.fromhex(c)
# assume HSCTF{... ...}
key = [c[0]^ord('H'), c[1]^ord('S')]
flag = ''
for i in range(len(c)):
    flag += chr(c[i] ^ key[i%2])
print(flag)
