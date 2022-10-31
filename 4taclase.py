#Mostrar del 1 a 10 en forma recursiva

from itertools import count
from pickle import APPEND


a = int(input("Ingresar el nro: "))

def ascendente (n):
    if(n > 0):
        print(n,end=" ")
        ascendente(n-1)
ascendente(10)

def descendente (n):
    if(n > 0):
        print(n,end="")
        ascendente(n-1)
descendente(10)

'''
Colecciones en Python
Tuplas: Coleccion de objetos INMODIFICABLES ordenados e indexados
ej:
'''
mitupla = (1,2,5,7)
print(mitupla)
print(mitupla[0])
print(mitupla[-1])

#constructor
#t1= tuple(unalista)
t2= tuple(10,11,12,13,15,18,22)

#subrangos de una tupla

t3 = t2[1:3] 
print (t2[3:])

#Diferentes tipos

t4=(1,"Romina","ISFT",7,8)
print(t4)

#Recorrido de una tupla
for x in t4:
    print(x)

#Funciones/metodos de tuplas
#(ver en bibliografia)

print("Longitud de t4:", len(t4))
print("ISFT aparece:", t4.count("ISFT"),"veces")

#Si existe un elemento
if "Romina" in t4:
    print("Esta")

#Anidamento de tuplas
t1=(1234)
t2=("Martin","Romina","Belen",456)
t3=(7,t1,t2,"Fin")
print(t3)

#dir = lista de elementos que se  puede hacer con las tuplas

# desempaquetado
t9=(10,12,2022)
dd,mm,aa = t1  

#########################################################################################################################
'''
Listas: Ordenadas, Indexadas, Modificables(Modificar, agregar, eliminar), Acepta duplicados
'''
#EJ: 
l1=["Alan","Fernando","Santiago","Jorge"]
#      0        1          2        3

#Anidamientos:
l2=["Romina",("Juan",4,7,82),True]
l3=["Limones",["Azucar",'Harina','Manteca'],'Manzana','Pera']
#       0                   1                   2        3  

# Constructores:
list(...)
vocales =('a','e','i','o','u')
l4 = list(vocales)
print(l4)
print(l4[1])#e
print(l4[-2])#0

#Metodos
#append
l4.append('y','z')
print(l4)#a,e,i,o,u,y,z
l4+=['m','p']
print(l4)#a,e,i,o,u,y,z,m,p
l4.insert(1,'j')    
print(l4)#a,j,e,i,o,u,y,z,m,p

#Contatenaciones
l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)

#Remove
l3.remove(4)#elimina el elemento 4

#pop
l3.pop(2)#Devuelve el elemento en posicion y lo elimina ("extrae")
l3.pop()#devuleve y elimina el ultimo

#del - elimina un elemento o un subrango ej: l3[1:4]

l3.sort()#ordena la lista
