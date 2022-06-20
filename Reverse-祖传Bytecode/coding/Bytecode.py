def foo3(b):
    from Crypto.Cipher import AES
    key = b'!!!Tover_yyds!!!'
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(b).hex()

def foo2(l):
    for i in range(len(l)):
        j = i
        i = 3 + 2*i
        l[j] ^= i + 66
    return bytes(l)

def foo1(s):
    l = []
    for x in s:
        l.append(ord(x))
    return l

def main():
    flag0 = input("input a flag: ")
    if len(flag0) != 38:
        print("Check your length?")
        exit(-1)
    if flag0[:5] != "flag{":
        print("Check more!")
        exit(-1)
    if flag0[-1] != "}":
        print("Check more!")
        exit(-1)
    flag0 = flag0[5:-1]
    flag1 = foo1(flag0)
    flag2 = foo2(flag1)
    flag3 = foo3(flag2)
    if flag3 == "9daaac32d42434ec7427ee43187afde3e5457143377f803b17aeec7c30ee6a89":
        print("Ohhhhhhhh! You get the flag~")
    else:
        print("Sorry~")
    return

if __name__ == "__main__":
    main()