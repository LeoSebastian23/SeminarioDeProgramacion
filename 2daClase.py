#Practica: Realizar una aplicacion que realice las siguientes preguntas
#1. Cual es la velocidad de la luz? rta: 300.000km/s
# si es correcta pregunta:
#2. Cual es la velocidad del sonido? 343 m/seg
# si es correcta
#3. Cual es la aceleracion de la gravedad?
# si es correcta: FIN todas correctas
'''
print("Preguntas a responder:")
rta1= int(input("Cual es la velocidad de la luz: \n1- 300km/s \n2- 300.000ks/s\n"))

if rta1 == 2:
    print("Bien!") 
    rta2 = int(input("Cual es la velocidad del sonido: \n1- 343km/s \n2- 20km/s\n"))
    if rta2 ==1:
        print("Bien!")
        rta3 = int(input("Cual es aceleracion de la gravedad: \n1- 100km/s \n2- 1.000km/s\n"))
        if rta3 == 1:
            print("Bien!")
            print("Todas correctas!")
        else: print("\nPregunta 3 incorrecta - La respuesta era 1")
    else: print("\nPregunta 2 incorrecta - La respuesta era 1")        
else: print("\nPregunta 1 incorrecta - La respuesta era 2")    
'''   
#Repeticiones
#Ciclo While

'''
#Ejemplo 1

contador = 0 
while contador < 10:
    print(contador)
    contador +=1        #Autoincrementa de a 1.
print("Fin app")

#Ejemplo 2

cont = 1
rta = 1

while cont < 10 and rta == 1:    
    cont +=1
    rta= int(input("Continuar?1 = Si\n"))
else:
    print("Terminaste ciclo While")
print("Fin App")

# La sentencia Break se puede utilizar en un if - while o for
'''
#Repeticiones
#Ciclo For
'''
#Ejemplo 1 

for i in [1, 2, 3, 4]:
    print(i, end=", ") # prints: 1, 2, 3, 4, #(end="") es para determinar que aparece al final de cada print


for i in range(1,10):
    print(i," ",end="")# para que el proximo print continue en el mismo renglon
input("Pulse una tecla para continuar...")  
print("Fin app")
#Ejemplo 2:
for i in range(1,10,2):
    print(i)
input("Pulse una recla para continuar")
print("Fin App")
#Ejemplo 3
for i in range(10,1,-1):
    print(i," ",end="")
input("Pulse una tecla...")
print("Fin App")
#Ejemplo 4
for _ in range (1,10):
    print("*")
print("Fin App")
#Ejemplo 5 
for i in range (0,10,2):
    print(i," ",end="")
else:
    print ("Fin del ciclo for")
'''
'''
#Funcion random
import random
print("Mostrar 5 nro aleatorios\n\n")
for _ in range(1,5):
    nro =random.randint(10,100)
    print(nro," ",end="")
print("Fin app")
'''
import os
os.system('cls') #limpia la consola
'''
#Practica: Ingresar un conjunto de numeros enteros hasta que se ingrese un 0
#calcular el producto de los pares y la suma de los impares
num = 1
mult = 1
sum = 0

while num != 0:
    num = int(input("Ingresa un conjunto de numeros a calcular. Para finalizar ingrese 0\n"))
    if num % 2 == 0 and num !=0:
        mult = mult*num
    else:  sum = sum + num
print("Pares: ",mult)
print("Impares: ",sum)
'''
#Practica: Ingresar Usuario y Contraseña y compararla con un usr y psw conocidos por la App.
#Permitir hasta 3 intentos, dar la bienvenida en el caso correcto o el mensaje "Ya realizo 3 intentos"
'''
usr = "Leo"
psw = "Sebastian"

usuario = input("Ingrese su usuario:\n")
contraseña = input("Ingrese su contraseña:\n")
i=1
while i < 3:
    if usuario != usr or contraseña != psw:
        print("El usuario NO existe!\n")
        usuario = input("Ingrese su usuario:\n")
        contraseña = input("Ingrese su contraseña:\n")
    i +=1
if usuario == usr and contraseña == psw:
        print("Fin App")
else: print("Ya realizo los 3 intentos")
'''
'''
Contar cuantas veces el usuario necesita para acertar un numero generado aleatoriamente de la siguiente manera:
1 generar un entero entre 1 y 100 (rnd)
2 usuario ingresa un valor (nro)
si nro > rnd entonces el proximo random debe estar entre min y nro
si nro < rnd entonces el proximo random debe estar entre nro y max
3 mostrar cuantos intentos se requiere
'''
import os
os.system('cls') #limpia la consola
min = 1
max = 50
import random
rnd = random.randint(1,50)
print("Ingresar un numero entre 1 y 50: ")
nro = int(input("nro: "))
intentos = 1
while nro != rnd:
    intentos += 1 
    if nro < rnd:
        max = nro
        rnd = random.randint(min,max)
        print("Ingresar un numero entre ",min,"y", max)
        nro = int(input("nro:"))
    elif nro > rnd:
        min = nro
        rnd = random.randint(min,max)
        print("Ingresar un numero entre ",min,"y ", max)
        nro = int(input("nro:"))
print("Acertaste!\n Numero de intentos: ",intentos)







