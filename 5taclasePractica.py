#REALIZAR UNA APP QUE MUESTRE UN MENU DE OPCIONES
#MENU: 
'''
Selecciones una opcion del menu
1- Inscibir estudiantes a final de Pragramacion 1
2- Inscribir estudiantes a final de Seminario de Programacion
3- Mostrar los estudiantes inscriptos(union)
4- Mostrar estudiantes inscriptos a ambas materias
5- Mostrar estudiantes inscriptos a Programacion I y NO EN Seminario
6- Informar si todos los estudiantes inscriptos en seminario tambien estan en programacion I
7- Dado un nombre informar en que materia esta inscripto
0- Fin app
'''
from libreriaC5 import *

'''
n = menu()
while n != 0: #Fuerzo el ingreso al ciclo while - Hasta no ingresar 0 NO TERMINA.
    if n==1:
        print("Ingrese los estudiantes para el Final de P1")
        alumnosP1 = inscripcion()
        print("Estuidiantes inscripcion a P1: \n ",alumnosP1) 
        input("Presione una tecla para continuar...")      
    elif n==2:
        print("Ingrese los estudiantes para el Final de Seminario")
        alumnosSeminario = inscripcion()
        print("Estuidiantes inscripcion a Seminario: \n ",alumnosSeminario)   
        input("Presione una tecla para continuar...")  
    elif n==3:
        mostrartdosIns(alumnosP1,alumnosSeminario)
        input("Presione una tecla para continuar...") 
    elif n==4:
        ambasMaterias(alumnosP1,alumnosSeminario)
        input("Presione una tecla para continuar...") 
    elif n==5:
        onlyP1(alumnosP1,alumnosSeminario)
        input("Presione una tecla para continuar...") 
    elif n==6:
        siS_noP1(alumnosP1,alumnosSeminario)
        input("Presione una tecla para continuar...") 
    elif n==7:
        nombre=input("Ingrese el nombre del alumno: ")
        seEncuentra(alumnosP1,alumnosSeminario,nombre)
        input("Presione una tecla para continuar...") 
    n = menu()
'''
#REALIZAR UNA AGENDA TELEFONICA (UTILIZAR DICCIONARIO)
 
'''
1- CARGAR DICCIONARIO CON NOMBRE Y CELULAR PARA CREAR UNA AGENDA 
(Cada vez que se repita un nombre, informar)
2- Dado un nombre informar su nro 
3- Agregar un telefono
4- Elimiar un telefono
5- Mostrar la agenda con el formato:
    nombre1: cel1:
    nombre2: cel2:
    nombre3: cel3:
6- Modificar un bro de telefono a partir de nombre
7- Generar un diccionario/traductor de ingles 
    clase: palabra españos - valor: ingles
    agregar opciones a agregar
0- Fin app
'''
dic1=dict()
dic1=agenda()
