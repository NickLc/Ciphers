class Alberti:
    def shift(self, shift):
        ''' (int) -> None
        Desloca o disco movel a quantidade de elementos em shift.
        '''
        shift = -shift
        self.movable_disk = self.movable_disk[shift:] + self.movable_disk[:shift]
 
    def set_fixed_disk(self, plain_alphabet):
        ''' (str) -> None
        Configura o alfabeto do disco fixo com o texto de plain_alphabet.
        '''
        self.fixed_disk = plain_alphabet.upper()
 
    def set_movable_disk(self, cipher_alphabet):
        ''' (str) -> None
        Configura o alfabeto do disco movel com o texto de cipher_alphabet.
        '''
        self.movable_disk = cipher_alphabet.lower()
 
    def set_keys(self, fixed_key, movable_key):
        ''' (char, charstr) -> None
        Configura as chaves do disco fixo e do disco movel;
        Desloca o disco movel de acordo com as chaves.
        '''
        self.set_fixed_key(fixed_key)
        self.set_movable_key(movable_key)
        fixed_id = self.fixed_disk.find(self.fixed_key)
        movable_id = self.movable_disk.find(self.movable_key)
        shift = fixed_id - movable_id
        self.shift(shift)
 
    def encrypt(self, plaintext, shift = 0, decrypt = False):
        ''' (str, [int], [bool]) -> str
        Cifra o plaintext com a cifra de Alberti.
        '''
        ciphertext = ''
        for ch in plaintext:
            if ch.isupper():
                #letra maiuscula
                self.set_keys(ch, self.movable_key)
            elif ch.isdigit():
                #numero
                movable_key = self.movable_disk[self.fixed_disk.find(ch)]
                self.set_keys(self.fixed_key, movable_key)
            else:
                #letra minuscula
                if decrypt:
                    #decifrando
                    i = self.movable_disk.find(ch)
                    ch = self.fixed_disk[i].lower()
                else:
                    #cifrando
                    i = self.fixed_disk.find(ch.upper())
                    ch = self.movable_disk[i]
                if shift:
                    #deslocamento
                    self.shift(shift)
            ciphertext += ch
        return ciphertext
 
    def decrypt(self, ciphertext, shift = 0):
        ''' (str, [int]) -> str
        Decifra utilizando a cifra de Alberti.
        '''
        #return self.encrypt(ciphertext, shift, True)
        text = ''
        plaintext = self.encrypt(ciphertext, shift, True)
        for ch in plaintext:
            if ch.islower():
                text += ch
        return text
 
    def set_fixed_key(self, fixed_key):
        ''' (char) -> None
        Configura a chave do disco fixo.
        '''
        self.fixed_key = fixed_key.upper()
 
    def set_movable_key(self, movable_key):
        ''' (char) -> None
        Configura a chave do disco movel.
        '''
        self.movable_key = movable_key.lower()