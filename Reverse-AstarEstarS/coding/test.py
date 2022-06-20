from Crypto.Cipher import AES

secret = b"Tover"
key = b"th1s_is_a_key_YO"
arr = []
for i in range(16):
    arr.append(key[i] ^ secret[i%5])
print(arr)

def padding_pkcs5(value):
    BS = AES.block_size
    return str.encode(value + (BS - len(value) % BS) * chr(BS - len(value) % BS), encoding='utf-8')

flag = 'flag{OH!It_s33ms_th4t_y0u_kn0w_A*E*S!}'
p = AES.new(key, AES.MODE_ECB)
cipher = p.encrypt(padding_pkcs5(flag))
print(cipher)
print(list(cipher))