import tkinter as tk
from tkinter import Spinbox
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import Frame
from tkinter import Entry
from tkinter import messagebox

class Vigenere:
    def __init__(self, abc="ABCDEFGHIJKLMNOPQRSTUVWXYZÑÁÉÍÓÚ"):
        self.abc = abc

    def encriptar(self,text,key):
        newText = ''
        keyIndex = 0
        for i in text:
            num = self.abc.find(i)
            if num != -1:
                num += self.abc.find(key[keyIndex])
                num %= len(self.abc)
                newText += self.abc[num]
                keyIndex +=1
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                newText += i
        return newText


    def desencriptar(self, text, key):
        newText = ''
        keyIndex = 0
        for i in text:
            num = self.abc.find(i)
            if num != -1:
                num -= self.abc.find(key[keyIndex])
                num %= len(self.abc)
                newText += self.abc[num]
                keyIndex +=1
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                newText += i       
        return newText

class App:
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("Cripto Vigenere")
        self.window.geometry('430x410')
        self.window.config(bg="#FFFFFF")
        self.vigenere = Vigenere()

        frameHead = Frame(self.window)
        lbl_method = tk.Label(frameHead, text='Metodo')
        lbl_method.grid(column=0, row=0, sticky='W', padx=5)
        lbl_key = tk.Label(frameHead, text='Clave')
        lbl_key.grid(column=1, row=0, sticky='W', padx=5)
        frameHead.grid(column=0,row=0)

        self.frame = Frame(self.window)
        self.combo = Combobox(self.frame)
        self.combo['values'] = ("Encriptar", "Desencriptar")
        self.combo.grid(column=0, row=0, sticky='W',padx=10)

        self.keyInput = Entry(self.frame)
        self.keyInput.grid(column =1, row=0, sticky='W',padx=10)
        
        buton = tk.Button(self.frame, text='Start', command = self.clicked)
        buton.grid(column=2, row=0, sticky='W',padx=10)
        self.frame.grid(column=0, row=1)

        lbl_txt_init = tk.Label(self.window, text='Input')
        lbl_txt_init.grid(column =0, row=3, sticky='W',padx=10)

        self.scroll_txt_init = tk.scrolledtext.ScrolledText(self.window,width=50,height=10)
        self.scroll_txt_init.grid(column=0,row=4, sticky='W',padx=10)

        lbl_txt_end = tk.Label(self.window, text='Output')
        lbl_txt_end.grid(column =0, row=5, sticky='W',padx=10)

        self.scroll_txt_end = scrolledtext.ScrolledText(self.window,width=50,height=10)
        self.scroll_txt_end.grid(column=0,row=6, sticky='W',padx=10)
        
        self.window.mainloop()
        
    def clicked(self):
        # Clear buffer f
        self.scroll_txt_end.delete(0.0, tk.END)

        textInput = self.scroll_txt_init.get("0.0", tk.END)
        key = self.keyInput.get()
        typeAction = self.combo.get()

        if(len(key)>len(textInput)):
            messagebox.showerror('Mensaje Error', 'La longitud de la clave debe ser menor que del input') 
        else:
            # Decode string
            if typeAction == "Encriptar":
                textOutput = self.vigenere.encriptar(textInput, key)
            else:
                textOutput = self.vigenere.desencriptar(textInput, key)
            # Put new string into of stroll 
            self.scroll_txt_end.insert(tk.INSERT, textOutput)

if __name__=='__main__':
    # Start App
    Apx = App()
    
    