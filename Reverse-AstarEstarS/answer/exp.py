from Crypto.Cipher import AES

secret = "Tover"
arr = [32, 7, 71, 22, 45, 61, 28, 41, 4, 45, 63, 10, 15, 58, 43, 27]
key = ''
for i in range(16):
    key += chr(arr[i] ^ ord(secret[i%5]))
key = key.encode()
print(key)

p = AES.new(key, AES.MODE_ECB)
c = bytes([211, 93, 222, 166, 164, 157, 25, 242, 217, 199, 50, 240, 62, 64, 120, 233, 16, 140, 140, 180, 83, 119, 49, 193, 191, 63, 108, 93, 127, 129, 140, 205, 85, 147, 50, 53, 34, 172, 61, 55, 115, 44, 74, 69, 210, 197, 108, 175])
print(p.decrypt(c))