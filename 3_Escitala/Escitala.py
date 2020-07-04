# -*- coding: utf-8 -*- 
import math

class Escitala():
    
    def __init__(self):
        pass
  
    def desordenar_col(self, text, n_col, indices):
        filas = math.ceil(len(text)/n_col)  # numero de caracteres en una vuelta
        nuevo_text = ''
        for f in range(filas):
            for i in indices: 
                try:
                    nuevo_text += text[f*n_col + i]
                except:
                    nuevo_text += ' '    
        
        return nuevo_text

    def encriptar(self, text, n_col):
        text_ecriptado = ''
        # n_col = longitud de la letra
        #redondeo hacia arriba  - Clave
        pivot = math.ceil(len(text)/n_col)  # numero de caracteres en una vuelta
        for n in range(n_col):
            for p in range(pivot):
                try:
                    text_ecriptado += text[n+n_col*p]
                except:
                    text_ecriptado += ' '
        return text_ecriptado

    def encriptar_con_orden(self, text, n_col, indices):
        text_desordenado = self.desordenar_col(text,n_col,indices)
        text_encriptado = self.encriptar(text_desordenado,n_col)
        return text_encriptado

    def desencriptar(self, text, n_col):
        text_encriptado = ''
        #redondeo hacia arriba  - Clave
        pivot = math.ceil(len(text)/n_col)
        for p in range(pivot):
            for n in range(n_col):
                try:
                    text_encriptado += text[p+pivot*n]
                except:
                    text_encriptado += ' '

        return text_encriptado

    def ordenar_col(self,text,n_col,indices):
        filas = math.ceil(len(text)/n_col)  # numero de caracteres en una vuelta
        nuevo_text = ''
        for f in range(filas):
            for ind in range(len(indices)): 
                try:
                    i = indices.index(ind) 
                    nuevo_text += text[f*n_col + i] 
                except:
                    nuevo_text += ' '    
        
        return nuevo_text      
        
    def desencriptar_con_orden(self, text, n_col, indices):
        text_desencriptado = self.desencriptar(text, n_col)
        text_ordenado = self.ordenar_col(text_desencriptado,n_col,indices)
        return text_ordenado

if __name__ == "__main__":
    text = 'En un lugar de la Mancha, de cuyo nombre no quiero acordarme'
    #text = 'VAMOSALEERMUNDOINFORMATICO'
    #text = 'I AM HURT VERY BADLY HELP'
    #text = 'ASICIFRABANCONLAESCITALA'
    print(f'texto inicial: {text}')
    n_col = 10
    indices = [9,7,8,3,5,4,6,2,1,0]
    text_desordenado =Escitala().desordenar_col(text,n_col,indices)
    print(f'Cambiando los indices: {text_desordenado}')
    text_encriptado = Escitala().encriptar(text_desordenado, n_col)
    print(f'texto_encriptado: {text_encriptado}')
    text_desencriptado = Escitala().desencriptar(text_encriptado, n_col)
    print(f'texto desencriptado: {text_desencriptado}')
    text_ordenado = Escitala().ordenar_col(text_desencriptado,n_col,indices)
    print(f'texto ordenado: {text_ordenado}')

