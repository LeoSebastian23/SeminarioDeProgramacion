'''
Practica:
1- Declarar la clase persona con atributos Nombre, Edad, Fecha_nac
    una lista que indiqie nombre de c/n hijos
    un diccionario que indique una agenda de contactos (clase = nombre, valor = nro celular)
2- Todos los getters y setters que necesite
3- Metodos: 
    Nacimiento: agrega un hijo a su lista de Hijos
    agregarContacto:    agrega un contacto a la agenda
    modificarContacto:  modifica un contacto a la agenda
    eliminarContacto:   elimina un contacto a la agenda
    buscarContacto:  busca y muestra si un nombre esta en la agenda y muestra su nro
    MOSTRAR PERSONA
4- menu de opciones para manejar la agenda
5- menu de opciones para crear una lista de personas c/u con su agenda
6- Mostrar lista de personas.
'''

from Persona6ta import *
from os import system




n = 1
lista = []
while n:
    n = menu()
    if n == 1:
        nn = input("Ingrese el nombre de la persona: ")
        ent = input("Ingrese la edad de la persona: ")
        nto = input("Ingrese la fecha de nacimiento. Ej: 30/03/1999\n")
        p1 = Persona(nn,ent,nto)
        lista.append(p1)
    elif n == 2:
#preguntar al usuario a que persona se le agrega un hijo y buscarla en la lista, si existe
#se agrega, sino, informar

        nhijo = input("En caso de tener hijos\nIngrese el nombre del mismo: ")
        lista[pos].nacimiento(nhijo)
    elif n == 3:
        a = agenda()
        while a > 0 and a < 6:
            if a == 1:
                nombreContacto = input("Ingrese el nombre del contacto: ")
                nroCel = int(input("Ingrese el numero del contacto: "))
                lista[0].agregarContacto(nombreContacto,nroCel)
                input("Pulse una tecla para continuar...")
                
                system("cls")
            elif a == 2:
                p1.MuestraSoloContactos()
                m = input("Eliga el contacto a MODIFICAR\n Ingreselo tal cual esta escrito: ")
                lista[0].modificarContacto(m)
                input("Pulse una tecla para continuar...")
            elif a == 3:
                lista[0].MuestraSoloContactos()
                e = input("Eliga el contacto a ELIMINAR\n Ingreselo tal cual esta escrito: ")
                lista[0].eliminarContacto(e)
                input("Pulse una tecla para continuar...")
            elif a == 4:   
                o = input("Ingrese el contacto que desea buscar: ")
                lista[0].obtenerContacto(o) 
                input("Pulse una tecla para continuar...")
           
            system("cls")
            a = agenda()   
    elif n == 4:
        lista[0].MuestraPersona()
        input("Pulse una tecla para continuar...")
    elif n == 5:
        for i in lista:
            i.MuestraPersona()
        
        

