from signal import alarm
from Crypto.Cipher import AES
from binascii import unhexlify
from reCaptcha import reCaptcha
from secret import flag

class MyHash:
    def __init__(self):
        aes_key = b'k' * 16 # AES with a fixed key
        self.cipher = AES.new(aes_key, AES.MODE_ECB)
    
    def enc(self, m):
        return self.cipher.encrypt(m)

    def dec(self, m):
        return self.cipher.decrypt(m)

    def pad(self, m):
        m = m + b'\x00' * 33
        return m[:33]
    
    def hash(self, msg):
        msg = self.pad(msg)

        block1 = msg[ 0:11] + b'\x00' * 5
        block2 = msg[11:22] + b'\x00' * 5
        block3 = msg[22:33] + b'\x00' * 5

        state = block1

        state = self.enc(state)
        state = bytes([state[i] ^ block2[i] for i in range(16)])

        state = self.enc(state)
        state = bytes([state[i] ^ block3[i] for i in range(16)])

        return state


def main():
    alarm(2)
    if not reCaptcha():
        print('GO AWAY! I hate robot!')
        return
    alarm(10)

    PASSWD = b'this_is_a_very_secure_password'
    try:
        hash_func = MyHash()
        h1 = hash_func.hash(PASSWD)

        your_passwd = unhexlify(input("Please input your passwd (hex) : "))
        if len(your_passwd) > 33:
            print('What are you doing???')
            return

        if your_passwd != PASSWD:
            h2 = hash_func.hash(your_passwd)
            if h1 == h2:
                print(f"Coming! This is my home~ This is a flag : {flag}")
            else:
                print("GO AWAY!")
        else:
            print("Gotcha!!! Hacker!!! Now I know who stole my password!!!")
    except:
        print("Error!")

if __name__ == "__main__":
    main()
