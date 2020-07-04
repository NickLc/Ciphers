import tkinter as tk
from tkinter import Spinbox
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import Frame
from tkinter import Entry
from tkinter import messagebox

class Xor:
    def __init__(self):
        pass

    def encriptar(self,text):
        text_reverse = text[::-1]
        newText = ''
        for ord_text, ord_text_reverse in zip(text, text_reverse):
            newText += hex(ord(ord_text) ^ ord(ord_text_reverse)) + " "
        return newText


    def desencriptar(self, text, key):
        newText = ''      
        return newText

class App:
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("Cripto Xor")
        self.window.geometry('430x410')
        self.window.config(bg="#FFFFFF")
        self.xor = Xor()

        frameHead = Frame(self.window)
        lbl_method = tk.Label(frameHead, text='Metodo')
        lbl_method.grid(column=0, row=0, sticky='W', padx=5)
    
        frameHead.grid(column=0,row=0)
        self.frame = Frame(self.window)
        self.combo = Combobox(self.frame)
        self.combo['values'] = ("Encriptar") #, "Desencriptar")
        self.combo.grid(column=0, row=0, sticky='W',padx=10)
        
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
        typeAction = self.combo.get()

        
        # Decode string
        if typeAction == "Encriptar":
            textOutput = self.xor.encriptar(textInput)
        else:
            #textOutput = self.xor.desencriptar(textInput)
        # Put new string into of stroll 
        self.scroll_txt_end.insert(tk.INSERT, textOutput)

if __name__=='__main__':
    # Start App
    Apx = App()
    
    