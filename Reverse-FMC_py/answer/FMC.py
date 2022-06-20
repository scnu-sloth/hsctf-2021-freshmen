# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: FMC.py
# Compiled at: 1995-09-28 00:18:56
# Size of source mod 2**32: 272 bytes
Instruction context:
   
 L.  71        82  LOAD_FAST                'encrypted'
->                84  RETURN_VALUE     


class FMC(object):
    MorseCode = {'!':'-.-.--',  '"':'.-..-.',  "'":'.----.',  '(':'-.--.',  ')':'-.--.-', 
     ',':'--..--',  '-':'-....-',  '.':'.-.-.-',  '0':'-----', 
     '1':'.----',  '2':'..---',  '3':'...--',  '4':'....-', 
     '5':'.....',  '6':'-....',  '7':'--...',  '8':'---..', 
     '9':'----.',  ':':'---...',  ';':'-.-.-.',  '=':'-...-', 
     '?':'..--..',  '@':'.--.-.',  'A':'.-',  'B':'-...', 
     'C':'-.-.',  'D':'-..',  'E':'.',  'F':'..-.',  'G':'--.', 
     'H':'....',  'I':'..',  'J':'.---',  'K':'-.-',  'L':'.-..', 
     'M':'--',  'N':'-.',  'O':'---',  'P':'.--.',  'Q':'--.-', 
     'R':'.-.',  'S':'...',  'T':'-',  'U':'..-',  'V':'...-', 
     'W':'.--',  'X':'-..-',  'Y':'-.--',  'Z':'--..'}
    CipherSequence = '.....-..x.-..--.-x.x..x-.xx-..-.--.x--.-----x-x.-x--xxx..x.-x.xx-.x--x-xxx.xx-'

    def toMorse(self, src: str) -> str:
        result = ''
        preced_by_letter = False
        preced_by_space = False
        for letter in src.upper():
            if letter in self.MorseCode:
                if preced_by_letter:
                    result += 'x'
                else:
                    if preced_by_space:
                        result += 'xx'
                result += self.MorseCode[letter]
                preced_by_letter = True
                preced_by_space = False
            else:
                if letter == ' ':
                    preced_by_space = True
                    preced_by_letter = False
                if len(result) != 0:
                    result += 'xx'
                return result

    def createKey(self, keyphrase: str='') -> str:
        upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        for letter in keyphrase.upper():
            if letter in upper_letters and letter not in result:
                result += letter
            for letter in upper_letters:
                if letter not in result:
                    result += letter
                if not len(result) == 26:
                    raise AssertionError
                return result

    def morseToKey(self, mcmsg: str, key: str) -> str:
        if not len(key) == 26:
            raise AssertionError
        if len(mcmsg) >= 3:
            care_about = mcmsg[0:3]
            for index in range(len(self.CipherSequence) // 3):
                if care_about == self.CipherSequence[index * 3:index * 3 + 3]:
                    return key[index]

        return ''

    def FMCEncrypt--- This code section failed: ---

 L.  61         0  LOAD_FAST                'self'
                2  LOAD_METHOD              toMorse
                4  LOAD_FAST                'src'
                6  CALL_METHOD_1         1  ''
                8  STORE_FAST               'mcmsg'

 L.  62        10  LOAD_FAST                'self'
               12  LOAD_METHOD              createKey
               14  LOAD_FAST                'keyphrase'
               16  CALL_METHOD_1         1  ''
               18  STORE_FAST               'key'

 L.  64        20  LOAD_STR                 ''
               22  STORE_FAST               'encrypted'

 L.  65        24  LOAD_CONST               0
               26  STORE_FAST               'counter'

 L.  67        28  LOAD_FAST                'self'
               30  LOAD_METHOD              morseToKey
               32  LOAD_FAST                'mcmsg'
               34  LOAD_FAST                'counter'
               36  LOAD_CONST               3
               38  BINARY_MULTIPLY  
               40  LOAD_CONST               None
               42  BUILD_SLICE_2         2 
               44  BINARY_SUBSCR    
               46  LOAD_FAST                'key'
               48  CALL_METHOD_2         2  ''
               50  STORE_FAST               'val'

 L.  68        52  LOAD_FAST                'counter'
               54  LOAD_CONST               1
               56  INPLACE_ADD      
               58  STORE_FAST               'counter'

 L.  69        60  LOAD_FAST                'val'
               62  LOAD_STR                 ''
               64  COMPARE_OP               !=
               66  POP_JUMP_IF_FALSE    82  'to 82'

 L.  69        68  LOAD_FAST                'encrypted'
               70  LOAD_FAST                'val'
               72  INPLACE_ADD      
               74  STORE_FAST               'encrypted'
               76  JUMP_BACK            28  'to 28'

 L.  70        78  BREAK_LOOP           82  'to 82'
               80  JUMP_BACK            28  'to 28'
             82_0  COME_FROM            66  '66'

 L.  71        82  LOAD_FAST                'encrypted'
               84  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `RETURN_VALUE' instruction at offset 84


if __name__ == '__main__':
    flag = input('Give me a sentence?\n')
    key = 'ToverCrackRSA'
    f = FMC()
    dst = f.FMCEncrypt(flag, key)
    if dst == 'BKTAOJOJRJTALTKTCBVTVHFBKTCTCTVRITVBOUVDKGARLTCHVGVTIHFHITIOITCBUFOITC':
        print('Congratulations! Here is your flag: flag{' + flag.lower() + '}')
    else:
        print('Think more?')
