import tkinter as tk
from tkinter import Spinbox
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import Frame

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
    
class App:
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("Cripto Cesar")
        self.window.geometry('430x410')
        self.window.config(bg="#FFFFFF")
        self.cesar = Cesar()

        frameHead = Frame(self.window)
        lbl_method = tk.Label(frameHead, text='Metodo')
        lbl_method.grid(column=0, row=0, sticky='W', padx=20)
        lbl_rot = tk.Label(frameHead, text='ROT')
        lbl_rot.grid(column=1, row=0, sticky='W', padx=5)
        frameHead.grid(column=0,row=0)

        self.frame = Frame(self.window)
        self.combo = Combobox(self.frame)
        self.combo['values'] = ("Encriptar", "Desencriptar")
        self.combo.grid(column=0, row=0, sticky='W',padx=10)

        maxSpin = len(self.cesar.abc)
        self.spin = Spinbox(self.frame, from_=1, to=maxSpin, width=5)
        self.spin.grid(column =1, row=0, sticky='W',padx=10)
        
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
        # Clear buffer
        self.scroll_txt_end.delete(0.0, tk.END)

        textInput = self.scroll_txt_init.get("0.0", tk.END)
        rot = self.spin.get()
        typeAction = self.combo.get()
        
        # Decode string
        if typeAction == "Encriptar":
            textOutput = self.cesar.encriptar(textInput, int(rot))
        elif typeAction == "Desencriptar":
            textOutput = self.cesar.desencriptar(textInput, int(rot))
        
        # Put new string into of stroll 
        self.scroll_txt_end.insert(tk.INSERT, textOutput)

if __name__=='__main__':
    # Start App
    Apx = App()
    
    