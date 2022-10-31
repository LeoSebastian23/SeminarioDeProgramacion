#1
vNombre= input("Ingrese su nombre: ")
vApellido= input("Ingrese su apellido: ")
edad= input ("Ingrese su edad: ")

vNombreCompleto = (vNombre + ' ' + vApellido) 
print (vNombreCompleto)
print(vNombreCompleto.upper())
print('Pulse una tecla para continuar')
print(vNombreCompleto.lower())



#vNombreCompleto = vNombre[0].upper() + vApellido[0].upper()
#print(vNombre[0].upper() + vApellido[0].upper())

print (vNombreCompleto.title())
#print(dir(vNombreCompleto))#Todos los metodos para probar en string
print("Largo nombre: ",len(vNombre))
print("Largo apellido: ",len(vApellido))
print("Largo nombre completo: ",len(vNombreCompleto))

print(vNombreCompleto[:8])
print(vNombreCompleto[8:])

#vAlan = 'Alan'
print(vNombre.find("Alan"))
print(vApellido.find("Alan"))
print(vNombreCompleto.find("Alan"))