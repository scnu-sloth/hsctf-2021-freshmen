from Crypto.Cipher import AES

# foo3
c = "9daaac32d42434ec7427ee43187afde3e5457143377f803b17aeec7c30ee6a89"
key = b'!!!Tover_yyds!!!'
cipher = AES.new(key, AES.MODE_ECB)
flag = cipher.encrypt(bytes.fromhex(c))

# foo2
flag = list(flag)
for i in range(len(flag)):
    j = i
    i = 3 + 2*i
    flag[j] ^= i + 66

# foo1
flag = ''.join(map(chr, flag))

print("flag{" + flag + "}")