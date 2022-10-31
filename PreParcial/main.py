
from Usuarios import *
from clases import *
'''
U1 = Usuarios("Sofía Fernandez","45324786", "Belgrano 3023", 2, 50)
U2 = Usuarios("Ernesto Filippa", "32345678","San Martin 9823", 1, 30)
U3 = Usuarios("Ana María Godoy", "19345632","San Lorenzo 2134", 3, 70)
U4 = U1
#U1.Muestra()

#U1.calcularImportes(450)
#U4.Muestra()
#U1.calcularImportes(600)
#U2.Muestra()
#U1.Muestra()
print("ID(U1): ", id(U1))
print("ID(U4): ", id(U4))
print(U1)
print(U2)
print(U4)
print(U1.__Nombre, "vive en", U1.__Direccion)
print(U4.__Nombre, "vive en", U4.__Direccion)
print("Atributos de la clase")
print(Usuarios.__name__)
print(Usuarios.__module__)
print(Usuarios.__doc__)
print(Usuarios.__dict__)
print("Atributos de los objetos")
print(U1.__class__)
print(U1.__dict__)
'''

P1 = Particular("Leonardo","41.500.800","Cte N Otamendi 1234",500,"30/12/1999")
P1.Muestra()
print("-"*50)
P2 = Profesional("Lucio","80.700.900","Miramar 9999",200,"Administracion","Abogacia")
P2.Muestra()
print("-"*50)
P3 = Comercial("Comercio LOLO","40.890.870","Mar del plata 4321",1200,"Ferreteria","20-40890870-2")
P3.Muestra()
print("-"*50)
P1.calcularImportes(300)
P2.calcularImportes(750)
P3.calcularImportes(1470)

