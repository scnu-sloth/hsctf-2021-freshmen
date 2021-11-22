class FMC(object):
    MorseCode = { "!": "-.-.--", '"': ".-..-.", "'": ".----.", "(": "-.--.",
        ")": "-.--.-", ",": "--..--", "-": "-....-", ".": ".-.-.-",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.", ":": "---...", ";": "-.-.-.",
        "=": "-...-", "?": "..--..", "@": ".--.-.", "A": ".-",
        "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
        "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-",
        "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", 
        "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.." }
    CipherSequence = '.....-..x.-..--.-x.x..x-.xx-..-.--.x--.-----x-x.-x--xxx..x.-x.xx-.x--x-xxx.xx-'

    def createKey(self, keyphrase: str = "") -> str:
        upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ""
        for letter in keyphrase.upper():
            if letter in upper_letters and letter not in result:
                result += letter
        
        for letter in upper_letters:
            if letter not in result:
                result += letter
        
        assert len(result) == 26
        return result
    
    def fromMorse(self, mcmsg: str) -> str:
        result = ""
        token = ""
        dlim_counter = 0

        for i in range(len(mcmsg)):
            if mcmsg[i] == 'x':
                dlim_counter += 1
                if token != "":
                    for k in self.MorseCode:
                        if self.MorseCode[k] == token:
                            result += k
                    token = ""
                if dlim_counter == 2 and i != len(mcmsg) - 1:
                    result += " "
                    dlim_counter = 0
            else:
                dlim_counter = 0
                token += mcmsg[i]

        return result
    
    def keyToMorse(self, kmsg: str, key: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        result = ""
        for letter in kmsg:
            try:
                index = key.index(letter)
                result += self.CipherSequence[index * 3 : index * 3 + 3]
            except:
                pass

        if result[-2:] != 'xx':
            if result[-1] != 'x':
                result += 'xx'
            else:
                result += 'x'
        return result

    def FMCDecrypt(self, emsg: str, keyphrase: str = "") -> str:
        mcmsg = self.keyToMorse(emsg, self.createKey(keyphrase))
        msg = self.fromMorse(mcmsg)
        return msg


if __name__ == '__main__':
    dst = "BKTAOJOJRJTALTKTCBVTVHFBKTCTCTVRITVBOUVDKGARLTCHVGVTIHFHITIOITCBUFOITC"
    key = "ToverCrackRSA"
    f = FMC()
    flag = f.FMCDecrypt(dst, key)
    print("flag{" + flag.lower() + "}")