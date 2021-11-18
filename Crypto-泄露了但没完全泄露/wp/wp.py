from binascii import hexlify, unhexlify

def pad(m):
    pad_len = 16 - len(m) % 16
    m = m + b'\x00' * pad_len
    return m
    

def main():
    # get all passwords (in plaintext)
    all_passwd = {}
    with open('passwd_list1.txt', 'r') as f:
        for line in f:
            name, passwd = line.split(':')
            passwd = passwd.replace('\n', '')
            passwd = pad(passwd.encode())
            passwd = hexlify(passwd)
            all_passwd[name] = passwd

    # get all passwords (in ciphertext)
    cp_pairs = [] # (plaintext, ciphertext) pairs
    with open('passwd_list1.txt_enc', 'r') as f:
        for line in f:
            name, ciphertext = line.split(':')
            ciphertext = ciphertext.replace('\n', '')
            plaintext = all_passwd[name]
            cp_pairs.append((plaintext, ciphertext))

    
    # get the mapping between plaintexts and ciphertexts
    block_pairs = {}
    for p, c in cp_pairs:
        l = len(p)
        block_num = l // 16
        for i in range(block_num):
            block_pairs[c[i * 32 : (i + 1) * 32]] = p[i * 16 : (i + 1) * 16]

    # get the password of his door (in ciphertext)
    door_passwd = ''
    with open('passwd_list2.txt_enc', 'r') as f:
        for line in f:
            name, ciphertext = line.split(':')
            if name == 'door':
                ciphertext = ciphertext.replace('\n', '')
                door_passwd = ciphertext
                break

    # recover the plaintext with the mapping above
    flag = b''
    ciphertext_len = len(door_passwd)
    block_num = ciphertext_len // 32
    for i in range(block_num):
        plaintext = block_pairs[door_passwd[i * 32 : (i + 1) * 32]]
        #print(unhexlify(plaintext))
        flag += unhexlify(plaintext)
    print('flag{%s}' % flag.decode())


if __name__ == "__main__":
    main()
