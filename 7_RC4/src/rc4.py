
import math

class Rc4:
    def __init__(self):

        pass

    def encriptar(self,text, key):
        return self.trasformar(text, key)

    def desencriptar(self,text, key):
        return self.trasformar(text, key)

    def trasformar(self,text, key):
        Key_Stream = self.createStremKey(key, len(text))
        text = self.strToOrd(text)
        result = self.xor(Key_Stream, text)
        result = ''.join(chr(i) for i in result)
        return result

    def createStremKey(self, key, len_text):
        S = self.KSA(key)
        Key_Stream = self.PRGA(S, len_text)
        return Key_Stream

    def KSA(self, key):
        i=0
        S = [i for i in range(256)]
        newkey = key * int(math.ceil(256/len(key)))
        newkey = newkey[:256]

        K_ord = [ord(i) for i in newkey]

        j = 0
        for i in range(256):
            j = (j + S[i]+ K_ord[i]) % 256
            S[i], S[j] = S[j] , S[i]

        return(S)

    def PRGA(self, S, len_text):
        j = 0
        Key_Stream = []

        for m in range(len_text):
            i = (m+1) % 256
            j = (j+S[i]) % 256
            S[i], S[j] = S[j], S[i]
            t = (S[i] + S[j]) % 256
            Key_Stream.append(S[t])

        return Key_Stream

    def strToOrd(self, text):
        num = [ord(i) for i in text]
        return num
    
    def strToHex(self, text):
        text_hex = ''.join(format(ord(i), "x") for i in text)
        return str.upper(text_hex)

    def xor(self, arr_a, arr_b):
        result = [a^b for a,b in zip(arr_a, arr_b)]
        return result

if __name__ == "__main__":
    rc4 = Rc4()
    key = "Clave de 128 bit"
    text = "Un saludo"
    t_encode = rc4.encriptar(text,key)
    t_decode = rc4.desencriptar(t_encode, key)
    print(t_decode) 