from Crypto.Cipher import AES
from binascii import hexlify
from secret import aes_key

class MyCipher:
    def __init__(self, aes_key):
        self.cipher = AES.new(aes_key, AES.MODE_ECB)
    
    def enc(self, m):
        return self.cipher.encrypt(m)

    def dec(self, m):
        return self.cipher.decrypt(m)

    def pad(self, m):
        pad_len = 16 - len(m) % 16
        m = m + b'\x00' * pad_len
        return m
    
    def encryption(self, m):
        m = hexlify(m)
        m = self.pad(m)
        len_m = len(m)
        block_num = len_m // 16

        c = b''
        for i in range(block_num):
            c += self.enc(m[i * 16 : (i + 1) * 16])

        return c

def main():
    file_path = input('where is the file: ')

    all_passwd = []
    with open(file_path, 'r') as f:
        for line in f:
            name, passwd = line.split(':')
            passwd = passwd.replace('\n', '')
            all_passwd.append((name.encode(), passwd.encode()))

    cipher = MyCipher(aes_key)
    all_passwd_enc = []
    for name, passwd in all_passwd:
        passwd_enc = cipher.encryption(passwd)
        all_passwd_enc.append((name, passwd_enc))

    with open(file_path + '_enc', 'w+') as f:
        for name, passwd_enc in all_passwd_enc:
            name = name.decode()
            passwd_enc = hexlify(passwd_enc).decode()
            f.write('%s:%s\n' % (name, passwd_enc))
    print('finish')


if __name__ == "__main__":
    main()
