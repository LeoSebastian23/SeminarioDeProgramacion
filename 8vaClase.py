# Libreria PyQT5/6
from ast import Not
from tkinter import *
from xmlrpc.client import Boolean

ventana = Tk()
ventana.title("Ventana principal")
ventana.geometry("300x400")
ventana.resizable(False, False)
ventana.config(bg="lightblue")


lbl2 = Label(ventana, text="cartelito 2")
lbl2.grid(column=1, row=2)

lbl3 = Label(ventana, text="mensaje 3", font=("ArialBald", 18))
lbl3.grid(row=3, column=2, padx=10, pady=10)

aux = True
def mifuncion():

    global aux 

    if aux:
        print("Hiciste click en el boton 1")
        ventana.config(bg="red")
    else:
        ventana.config(bg="lightblue")
    aux = not aux


bt1 = Button(ventana, text='Boton 1', bg="orange", fg="green", command=mifuncion)
bt1.grid(row=4, column=2, pady=5, padx=5)

ventana.mainloop()
