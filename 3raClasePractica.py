
#Practica (con funciones)
# 1-Calcular y mostrar el factorial de N --> parametro
# 2-A partir de peso y altura de una persona, calcular el IMS (indice masa muscular = peso/altura2)
# 3-Realizar una funcion new() que devuelva un valor seleccionado por el usuario entre 0 y 7  
# 4-Realizar una funcion que necesite un parametro N (entre 1 y 10) y muestre esa tabla de multiplicar
# 
import os

os.system('cls') #limpia la consola

def fact(numero):
    
    if numero < 0:
        print("El numero negativo no es posible calcular.")
    elif numero == 0:
        return 1 
    else:   
        factorial = 1
        for i in range(1,numero+1):
            factorial = factorial*i
    return factorial
    
'''   
n = int(input("Ingrese el numero y se le devolvera su factorial: "))
print("El factorial del numero es: ",fact(n))
'''
def ims():
    peso=int(input("Ingrese su peso en kg: "))
    alt=int(input("Ingrese altura en cm: "))
    indice = peso * (alt**2)
    return indice
#print("Calculemos su INDICE DE MASA MUSCULAR:",ims())

def tableMult(num):
    if num == 0:
        return 0
    elif num < 0:
        print("No es posible con numeros negativos, ingrese numeroes enteros")
    else:
        m = 1
        for i in range(1,11):
            m = num*i
            print(num,"*",i," = ",m)

n= int(input("Ingrese un valor: "))
tableMult(n)
    
