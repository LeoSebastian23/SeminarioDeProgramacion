
'''
from readline import append_history_file
from socket import TIPC_CONN_TIMEOUT

print("Hola mundo!") # Imprime por pantalla

print("Hola \n mundo!") # Cambia de renglon

print ("Valor: ", aux) #Imprime texto + variable

print ("Hola",'Pepe') #"Hola Pepe" 

print (42) # Muestra el numero

print (41.35) # Muestra tal cual el numero

'''
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
aux = input ("Ingrese su nombre") # Ingreso por teclado. Se guarda en la variable asignada
print("Su nombre es: ", aux)

mi_var = input("Ingrese su nombre") #Leo
mi_var1 = input("Ingrese su apellido") #Gauto
mi_var2 = mi_var + mi_var1 # Concatena variables del mismo tipo 
print (mi_var2) # Leo Gauto

# Tipo de dato dinamico va tomando el valor en funcion de la append_history_file

my_var = 125
my_var1 = 33
my_var2 = mi_var + mi_var1 #Se va a ejectutar una suma porque son variables tipo entero
print (my_var2) # 158
'''
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
#Tipo de dato: String

mi_String = '' #Cadena vacia

print(type(mi_String)) #<class str> Consulta para saber que tipo de dato es la variable

print(len(mi_String))  #Largo de la cadena de texto

my_String = input ('Ingrese texto') #Leo

print ('largo de texto',len(my_String)) #3
print ('Primera letra', mi_String[0]) #L
print ('Ultima letra', mi_String[len(mi_String)-1]) #O. Le restamos uno ya que el ultimo string es "vacio"

mi_String ='Hola mundo'
print (mi_String [1:4]) #muestra ola_ 
print (mi_String [:5])  #muestra Hola_
print (mi_String [3:])  #muestra a_mundo

print('_'*25)       #Multiplica el string "*******************************************"
print('#'*50)       ##########################################################################....
print('Hola'*10)    #Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola

titulo = 'lo lindo y lo feo'

print(titulo) #lo lindo y lo feo

print('Separado por espacios')

print(titulo.split(' ')) #['lo', 'lindo', 'y', 'lo', 'feo']

print(titulo.split('o')) #['l', ' lind', ' y l', ' fe', '']

print(titulo.count('lo'))#Contador del objeto seleccionado #2

n = 21
print(titulo + n) #Error. No se puede concatenar string + int
print(titulo + str(n)) #str---> convierte a string.

a = '21'
b = '42'
c = a + b
print(c) # 2142

print(int(a)+int(b)) #63. int---> convierte a entero.

aux = 'hola'
aux1 = 'Hola'
print(aux == aux1) #False. Imprime booleano

print(aux.startswith('h')) #True. Se usa para verificar si una oración determinada comienza con una cadena en particular. Los parámetros de inicio y fin son opcionales. Podemos usarlos cuando queremos que solo se considere para la búsqueda alguna subcadena particular de la cadena original.
print(aux.endswith('a')) #True. Se usa para verificar si una oracion determinada finaliza con una cadena en particular.

print(aux.upper()) #Convierte todo a mayuscula
print(aux1.lower()) #Convierte todo a minuscula
print(aux.isalpha()) #True. Comprueba si una cadena está formada solo por letras o no. Si encuentra cualquier otro carácter, como un número o un carácter especial, devuelve False 

dir(str) #Muestra todos los metodos disponible de la clase <str>
dir(int) #Muestra todos los metodos disponible de la clase <int>

#Datos numerios:    Enteros - Reales - Complejos
#Booleanos:         True - False
#None:              Ausencia de dato ---> is - is not

A = None

if A is None:
    print("A es asignado: ",A) #A es asignado: None

#Operadores Aritmeticos: 
# +     suma  
# -     resta  
# *     multiplicacion   
# /     division real  
# //    division entera 
# %     resto entero  
# **    potencia

#Operadores Asignacion:
#  += 
# *= 
# /= 
# //= 
# %= 
# **=

#Operadores Logicos: 
# ==    Comparacion 
# !=    Distinto 
# >     Mayor 
# <     Menor 
# >=    MayorIgual 
# <=    MenorIgual

#Logicos: 
# and           y   v y v = v   v y f = f 
# or            o   v o v = v   v o f = v
# not           no  not v = f
'''
'''
#//////////////////////////////////////////////////////////////////////////////////////////////////
Ciclo for in Python

n1 = int(input("Ingrese un numero\n"))
if n1 > 0:
    print('Positivo')
elif n1 < 0:
    print('Negativo')
else:
    print('Cero')
print('Fin app')

#La estructura  if/elif/else es una forma común de controlar el flujo de un programa 
#lo que te permite ejecutar bloques de código específicos según el valor de algunos datos.

ahorros = int(ahorro=input('Ingrese ahorros en $:'))
if ahorros > 0:
    print('Tenes ahorros')
    if ahorros > 1.000 and ahorros < 10.000:
        print('Pocos ahorros')
    else:
        print('Muchos ahorros')
print('Fin app')

#También podemos crear if anidados para la toma de decisiones.
#Tomemos un ejemplo de cómo encontrar un número que sea par y también mayor que 10

x = 34
if x %  2 == 0:  # Ahora comprueba número par.
  if x > 10:
    print("Este número es par y es mayor que 10")
  else:
    print("Este número es par, pero no mayor 10")
else:
  print ("El número no es par. Así que punto de verificación más.")
'''
