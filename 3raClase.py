#def nombre ([parametros si es que hubiera]):


from re import X


def saludo():
    print("Hola Mundo!")
#saludo()

def saludo1():
    nombre = input("Ingrese su nombre:")
    edad = int(input("Ingrese edad:"))
    print =("Hola ",nombre,"Tenes ", edad, "años")
#saludo1()

#Con parametros
def saludo2(nombre,edad):
    print =("Hola ",nombre,"Tenes ", edad, "años")
#saludo2("santiago",21)

#o con variables
nom=input("Ingrese su nombre:")
ed=int(input("Ingrese edad:"))
#saludo2(nom,ed) 
#############################################################################
a=5
b=4
def funcion1():
    print ("a es: ",a)
    print ("b es: ",b)
funcion1()
x=10
y=20
def funcion3():
    x += 1 #error
funcion3()

def funcion4():
    global x
    x+=3
    print ("x es:",x)
funcion4()
#############################################################################
c=10
d=20

def funcion6():
    print("f6 x e y son:",x,y)
    z=5
    def funcion7(): #phyton permite declarar una funcion dentro de otra funcion
        p=100
        nomlocal = z
        print("p es:",p "y z es:",z)
    print ("z es:",z)
    funcion7()
funcion6()

def funcion8(a,b):
    return a*b
print(funcion8(3,4)) #parametro por referencia, no existe en python parametros por valor

def funcion9(a,b):
    return b*a
x=funcion9(8,6)

def funcion10(a,b):
    return b,a
x,y=funcion10(3,5)
print("x es: ",x,"e y es:",y)

def funcion11(a,b):
    return b,a
#z= funcion11(7,8)
#print(z) #8,7

def funcion12(a,b,c=10):
    print(a,"elevado a la ",b,"es: ", a**b)
    print(a,"multiplicado por ",c,"es: ", a*c)
#funcion12(2,3)
#funcion12(2,3,4)
#funcion12(b=7,a=4,5) #c = 5

def funcion13(x,y=2,z=3):
    '''
    En esta funcion lo que deseo hacer es qu el usuario ingrese
    al menos con un valor numero obligatoriamente, los otros dos
    toman valores por defecto
    '''
    print("Potencia 1:", x**y)
    print("Potencia 2:", (x**y)**z)
#print(funcion13.__doc__)

def funcion14(args):
    for n in args:
        print("Bienvenido: ",n)
#funcion14("Santiago","Alan","Martin","Romina","Karen")
######################################################################################

from libreria1 import *#para traer todo, si quiero las funciones elegidas las escribo una por una


