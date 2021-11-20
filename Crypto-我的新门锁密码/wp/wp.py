from Crypto.Cipher import AES
from binascii import unhexlify, hexlify

class MyHash:
    def __init__(self):
        aes_key = b'k' * 16
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

    def find_collision(self, h):
        state = h

        collision_msg1 = b''
        collision_msg2 = b''
        collision_msg3 = b''
        cSet = {}

        for i in range(2**20):
            msg1 = b'\xff' * 11 + str(i).encode()
            msg1 = msg1[-11:]
            m = msg1 + b'\x00' * 5

            c = self.enc(m)
            index = c[-5:]
            cSet[index] = msg1

        isFound = False
        for i in range(2**20):
            c = b'\x00' * 11 + str(i).encode() + state[-5:]
            c = c[-16:]
            m = self.dec(c)

            index = m[-5:]
            if cSet.get(index, None) != None:
                collision_msg1 = cSet[index]
                collision_msg3 = b'\x00' * 11
                collision_msg3 = bytes([state[j] ^ c[j] for j in range(11)])

                collision_msg2 = b'\x00' * 11
                collision_msg1_enc = self.enc(collision_msg1 + b'\x00' * 5)
                collision_msg2 = bytes([collision_msg1_enc[j] ^ m[j] for j in range(11)])

                isFound = True
                break
        if isFound == False:
            print('not found')
            return b''


        return collision_msg1 + collision_msg2 + collision_msg3


def main():
    PASSWD = b'this_is_a_very_secure_password'
    hash_func = MyHash()
    h1 = hash_func.hash(PASSWD)

    msg = hash_func.find_collision(h1)
    print(hexlify(msg))

    h2 = hash_func.hash(msg)

    if h1 == h2:
        print('right')

if __name__ == "__main__":
    main()
