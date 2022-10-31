def menu():
    n = int(input("Ingrese un valor entre 1 y 7: "))
    while n > 7 or n < 0:
        print("El numero ingresado no es valido.")
        n = int(input("Ingrese un valor entre 1 y 7: "))
    if n==1:
        print("Eligio la opcion 1")
    elif n==2:
        print("Eligio la opcion 2")
    elif n==3:
        print("Eligio la opcion 3")
    elif n==4:
        print("Eligio la opcion 4")
    elif n==5:
        print("Eligio la opcion 5")
    elif n==6:
        print("Eligio la opcion 6")
    elif n==7:
        print("Eligio la opcion 7")


def factorial(p):
    fact=p
    for i in range (0 ,p):
        mult = p-1
        aux = p*mult
        fact += aux
        i+=1
    return fact


print ("Hola",'Pepe')
print("Hola pepe")

A = None

if A is None:
    print("A es asignado:",A)
