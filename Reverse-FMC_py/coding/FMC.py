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
        "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.."}
    CipherSequence = '.....-..x.-..--.-x.x..x-.xx-..-.--.x--.-----x-x.-x--xxx..x.-x.xx-.x--x-xxx.xx-'

    def toMorse(self, src: str) -> str:
        result = ""
        preced_by_letter = False
        preced_by_space = False

        for letter in src.upper():
            if letter in self.MorseCode:
                if preced_by_letter:
                    result += "x"
                elif preced_by_space:
                    result += "xx"
                result += self.MorseCode[letter]
                preced_by_letter = True
                preced_by_space = False
            elif letter == ' ':
                preced_by_space = True
                preced_by_letter = False

        if len(result) != 0:
            result += "xx"
        return result

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

    def morseToKey(self, mcmsg: str, key: str) -> str:
        assert len(key) == 26
        if len(mcmsg) >= 3:
            care_about = mcmsg[0:3]
            for index in range(len(self.CipherSequence)//3):
                if care_about == self.CipherSequence[index*3:index*3+3]:
                    return key[index]
        return ''
    
    def FMCEncrypt(self, src: str, keyphrase: str = "") -> str:
        mcmsg = self.toMorse(src)
        key = self.createKey(keyphrase)

        encrypted = ""
        counter = 0
        while True:
            val = self.morseToKey(mcmsg[counter * 3:], key)
            counter += 1
            if val != '': encrypted += val
            else: break
        return encrypted

if __name__ == '__main__':
    flag = input("Give me a sentence?\n")
    key = "ToverCrackRSA"
    f = FMC()

    dst = f.FMCEncrypt(flag, key)
    if dst == "BKTAOJOJRJTALTKTCBVTVHFBKTCTCTVRITVBOUVDKGARLTCHVGVTIHFHITIOITCBUFOITC":
        print("Congratulations! Here is your flag: flag{" + flag.lower() + "}")
    else:
        print("Think more?")