from Persona6taClase import *

#p1 = Persona() #Constructor por defecto, reserva en memoria

cod = input("Ingrese el nombre de la persona: ")
ent = input("Ingrese la edad de la persona: ")

p1 = Persona(cod,ent)
p1.Caminar()
p1.MuestraPersona()

p3=p1
p3.MuestraPersona()

p3.__Nombre = "Miguel"
p3.setNombre("Adrian")
p3.MuestraPersona

print(Persona.cantidad)
