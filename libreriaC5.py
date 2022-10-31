def menu():
    i=-1
    while i < 1 or i > 7:  
        print("1- Inscibir estudiantes a final de Pragramacion 1")
        print("2- Inscribir estudiantes a final de Seminario de Programacion")
        print("3- Mostrar los estudiantes inscriptios(union)")
        print("4- Mostrar estudiantes inscriptos a ambas materias")
        print("5- Mostrar estudiantes inscriptos a Programacion I y no en Seminario")
        print("6- Informar si todos los estudiantes inscriptos en seminario tambien estan en programacion I")
        print("7- Dado un nombre informar en que materia esta inscripto")
        print("0- Fin app")
        i = int(input("Selecciones una opcion del menu: "))
        from os import system
        system("cls")
    return i


def inscripcion():
    ins = 1
    ap1 = set() #conjunto local a la funcion vacio
    
    while ins == 1:
        al = input("Ingrese nombre de estudiante:")
        ap1.add(al)
        ins = (int(input("Seguir inscribiendo = 1 - Finalizar = 0 ...")))
    return ap1

def mostrartdosIns(p,s):
    print("Total inscriptos es: \n", p|s)

def ambasMaterias(p1,s2):
    print("Inscriptos a ambas materias: ",p1&(s2))

def onlyP1(a,b):
    print("Inscriptos a SOLO a Programacion 1: ",a-b)

def siS_noP1(m,n): #Error en el algoritmo
    a = False
    for i in n:
        if i in m and  i in n:
            a = True
        else:
            a = False
    if a is True:
        print("Los alumnos inscriptos en Seminario tambien estan inscriptos a P1")
    else:
        print("Solo algunos alumnos inscriptos a Seminario tambien estan inscriptos a P1. No todos. ")


def seEncuentra(prog1,sem2,n):
    if n in prog1 and n in sem2: 
        print("El alumno esta inscripto en Programacion 1 y Seminario de programacion")
    elif n in prog1:
        print("El alumno esta inscripto a Programacion 1.")
    elif n in sem2:
        print("El alumno esta inscripto a Seminario de programacion.")






def agenda():
    agenda1=dict()
    ingreso = 1 
    while ingreso == 1:
        agenda1[input("Ingrese el nombre a agendar: ")] = int(input("Ingrese el numero de celular: "))
        ingreso = (int(input("Seguir ingresando = 1 \nFinalizar = 0 ...")))
    print (agenda1)
    return agenda1


def InfNombre(ag1):
    n = input("Ingrese el nombre y se le devolvera el nro celular: ")
    if n in ag1:
        print(ag1.values(n))

    
    

    




    
    






                 