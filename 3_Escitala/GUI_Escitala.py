import tkinter as tk
from tkinter import Spinbox
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import Frame
from tkinter import Entry
from tkinter import messagebox
from Escitala import Escitala

class App:
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("Cripto Escitala")
        self.window.geometry('430x410')
        self.window.config(bg="#FFFFFF")
        self.escitala = Escitala()

        frameHead = Frame(self.window)
        lbl_method = tk.Label(frameHead, text='Metodo')
        lbl_method.grid(column=0, row=0, sticky='W', padx=5)
        lbl_n_col = tk.Label(frameHead, text='Nro Columnas')
        lbl_n_col.grid(column=2, row=0, sticky='W', padx=10)
        lbl_ord_col = tk.Label(frameHead, text='Orden Col: ejm {1,3,2}')
        lbl_ord_col.grid(column=3, row=0, sticky='W', padx=5)
        frameHead.grid(column=0,row=0)

        self.frame = Frame(self.window)
        self.combo = Combobox(self.frame)
        self.combo['values'] = ("Encriptar", "Desencriptar")
        self.combo.grid(column=0, row=0, sticky='W',padx=10)
    
        self.spin = Spinbox(self.frame, from_=2,to=500, width=5)
        self.spin.grid(column =1, row=0, sticky='W',padx=10)

        self.input_ord_col = Entry(self.frame)
        self.input_ord_col.grid(column =2, row=0, sticky='W',padx=10)
        
        buton = tk.Button(self.frame, text='Start', command = self.clicked)
        buton.grid(column=3, row=0, sticky='W',padx=10)
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
        indices = self.convertir_indices(self.input_ord_col.get())
        n_col = int(self.spin.get())
        self.verificar_ind_col(indices,n_col)
        typeAction = self.combo.get()

        textInput = self.scroll_txt_init.get("0.0", tk.END)[:-1]   # Eliminamos el ultimo caracter '\n'

        if textInput == "":
            messagebox.showerror('Mensaje Error', 'Input vacio, Ingrese el texto a encriptar/desencriptar')

        if typeAction == "":
            messagebox.showerror('Mensaje Error', 'Seleccione el metodo')

        elif typeAction == "Encriptar":
            textOutput = self.escitala.encriptar_con_orden(textInput,n_col,indices)
        else:
            textOutput = self.escitala.desencriptar_con_orden(textInput,n_col,indices)
        # Put new string into of stroll 
        self.scroll_txt_end.insert(tk.INSERT, textOutput)
    
    def convertir_indices(self, text_indices):
        try:
            indices = text_indices[text_indices.index('{')+1:text_indices.index('}')]
            indices = [int(l)-1 for l in indices.split(',')]
            return indices
        except:
            messagebox.showerror('Mensaje Error', 'Error al ingresar el orden de las columnas') 

        

    def verificar_ind_col(self,indices,n_col):
        if (n_col != len(indices)):
            messagebox.showerror('Mensaje Error', 'Error en la cantidad de los ordenes de las columnas') 
        for i in range(n_col):
            if (not (i in indices)):
                messagebox.showerror('Mesaje Error', f'Error, el orden {i+1} no se encuentra en los ordenes de las columnas')

if __name__=='__main__':
    # Start App
    Apx = App()
    
    