#1) Solicitar  el usuario el ingreso de un externo entre 2 y 10, generar la tabla de multiplicar de ese nro.

#from ast import Num


def tablamult(nro):
    lista = []
    
    #if (nro <= 10) or (nro >= 2):
    for i in range(1,11):
        lista.append(nro * i)
    #print(lista)
    return lista

#nro = int(input("Ingrese un nro entre 2 y 10: "))
#print(tablamult(nro))

#2)Crear una tupla de numeros ej:1,4,8,12,16,20
#recorrer la tupla y mostrar el maximo y minimo valor



def max_min_tupla(tupla1):
    max=tupla1[0]
    min=tupla1[0]
    i=0
    while i <= len(tupla1)-1:
        if(tupla1[i] > max):
            max=tupla1[i]
        if(tupla1[i]< min):
            min=tupla1[i]
        i+=1 

    print("Max: ",max," Min: ",min)
    #return max,min

tupla1 = (1,2,3,4,5,6,7,8,9)
#max_min_tupla(tupla1)
print("Hola phyton")

#max_min_tupla(tupla1)

#3)Instertar elementos en una lista(dentro de un ciclo) y advertir al usuario si el 
# elemento esta repetido, de ser asi, informar cuantas veces se repite

#def ingresar_elementos():

#4)generar una lista de inscriptos a un examen final, luego:
#a- dado un nombre, informar si esta inscripto
#b- informar el orden de inscripcion

'''
Escribir una funcion que reciba un texto (string) y un entero que indique el largo 
maximo admidito en cada palabra.
Recortar las palabras que superen el maximo marcando @ 
Los puntos reemplazados con STOP y el punto final con STOPSTOP
Ejemplo: "Llego mañana alrededor del mediodia. Voy a almorzar!
lergo=5
"Llego mañan@ alred@ del medio@ STOP Voy a almor@ stopstop

'''

def funcion09(texto): 
    