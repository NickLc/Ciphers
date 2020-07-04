import unittest

class Cesar:
    def __init__(self, abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.abc = abc

    def desencriptar(self, text,rot):
        textDesc = ''
        for i in text:
            if i in self.abc:
                textDesc += self.abc[(self.abc.index(i)+rot)%len(self.abc)] 
            else:
                textDesc += i
        return textDesc

    def encriptar(self, text, rot):
        return self.desencriptar(text,rot*-1)
    

class TestCesar(unittest.TestCase):

    def test_desencriptar(self):
        textEnc ="ATG BKXKJOZG GRKMXK IUT RAF JK RATG U JK YUR ZKTJOJG IUSU ATG IOTZG IUT YAY RGJUY"
        textDesc = "UNA VEREDITA ALEGRE CON LUZ DE LUNA O DE SOL TENDIDA COMO UNA CINTA CON SUS LADOS"

        cal = Cesar().desencriptar(textEnc, 20)
        esp = textDesc
        self.assertEqual(esp, cal)

    def test_encriptar(self):
        textEnc ="ATG BKXKJOZG GRKMXK IUT RAF JK RATG U JK YUR ZKTJOJG IUSU ATG IOTZG IUT YAY RGJUY"
        textDesc = "UNA VEREDITA ALEGRE CON LUZ DE LUNA O DE SOL TENDIDA COMO UNA CINTA CON SUS LADOS"

        cal = Cesar().encriptar(textDesc, 20)
        esp = textEnc
        self.assertEqual(esp, cal)

if __name__=='__main__':
    # Start Unit Testing
    unittest.main()