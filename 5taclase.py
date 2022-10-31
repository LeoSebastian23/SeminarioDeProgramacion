# Conjuntos 
'''
#No tienen posicion 
#no aceptan repetidos
#No tienen orden 

Definicion: set()

#Ejemplo: 
Colores = set
colores ={ "Rojo", "Verde", "Azul"}
#print(type(colores)) #class (set)
#print(Colores) # { "Rojo", "Verde", "Azul"}

colores.add("Violeta")

#if "azul" in colores:
#    print("Esta")

#Ejemplos
frutas = {"Banana","Manzana","Pera","Melones","Sandia"}
print(frutas)

t2= ("Lunes","Martes","Miercoles","Jueves","Viernes")
dias = set(t2)

for f in frutas:
    print(f)
#consulta
if "Manzana" in frutas:
    print("Hay manzanas")

#agregar 
frutas.add("kiwi")

#agregar mas de un elemento
frutas.update(["Mango"],["Uva"],["Moras"])
print(frutas)

print("Cuantas frutas tiene?")
print(len(frutas))

#maximos y minimos
print(max(frutas))
print(min(frutas))

#Eliminar 
frutas.discard("Kiwi") #no da error si no existe
#frutas.remove("Arandanos") #error si no existe

ff=frutas # ff apunta a frutas
print(ff)
ff.clear()
print(frutas)
#realizar print de ff y print de frutas, que paso

# LISTAS (MODIFICABLES - ACEPTAN DATOS REPETIDOS - INDEXADOS ) 
# TUPLAS (NO MODIFICABLES - ACEPTAN DATOS REPETIDOS - INDEXADOS )
# CONJUNTOS (NO TIENE ORDEN - NO ACEPTA DATOS REPETIDOS ) las llaves que indican que es un conjunto

'''

#OPERACIONES CON CONJUNTOS 
#EJEMPLO:

#UNION
c1={1,2,3,4}
c2={3,4,5,6,7}
print = ("C1 union C2 es: ", c1|c2)
print("Otra forma ---> ", c1.union(c2))

#INTERSECCION 
print ("Elementos comunes de c1 y c2: ",c1&c2)
print("Otra forma ---> ", c1.intersection(c2))

#DIFERENCIA 
print ("Elementos de c1 y NO c2: ",c1-c2)
print("Otra forma ---> ", c1.difference(c2))

#DIFERENCIA SIMETRICA
#print ("Elementos NO comunes de c1 y c2: ",c1 c2)
print("Otra forma ---> ", c1.symmetric_difference(c2))

#DICCIONARIOS 
#PARES DE ELEMENTOS CLAVE: VALOR
#LA CLASE NOP SE PUEDE REPETIR, EL VALOR SI
#DEFINICION:

a={
    "Nombre:":"Santiago",
    "Apellido":"Alfredo",
    "Apode":"Amigo"
}

b={
    "Longitud:":"10 56 90",
    "Latitud":"40 08 35"
}

capitales={
    "Argentina":"Buenos Aires",
    "Uruguay":"Montevideo",
    "Brasil":"Brasilia"
}
print("Capital de Argentina: ",capitales["Argentina"])
capitales["Chile"]="Santiago" #agrega al elemento
capitales["Chile"]="Santiago e chile"#modificable

print("Todas las capitales:", capitales)

del capitales["Brasil"] #Borra un elemento

#Puede ser de distinto tipo

#Ejemplo:
equipo= {"El mejor":"River plate",
            1:"Armani",
            2:"Rojas",
            3:"Angeleri"
}
#Se puede anidar diccionarios
#Sus valores peden ser tuplas o listas
print(capitales.values())
print(capitales.keys())