from cgitb import text
from queue import Empty
from tkinter import *
from turtle import width

V = Tk()
V.title("Intentemos ingresar datos")
def eventoclick():
    respuesta = int(txt1.get())
    lbl1.configure(text = str(respuesta))
    txt1.config(bg="black")
    txt1.config(state="disabled")

V.geometry("400x300")
V.resizable(False,False)
V.config(bg="grey")

lbl1=Label(V,text="Hola")
lbl1.grid(row=2,column=2,padx=10,pady=10)
txt1=Entry(V,width=20)
txt1.grid(row=1,column=1,padx=10,pady=10)
btn1=Button(V,text="EventoClick",command=eventoclick)
btn1.grid(row=3,column=2,padx=10,pady=10)

V.mainloop()