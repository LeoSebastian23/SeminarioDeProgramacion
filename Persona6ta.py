
class Persona:
    def __init__ (self,Nom,Ed,Fec):
        self.__Nombre = Nom
        self.__Edad = Ed
        self.__Fecha_Nto = Fec
        self.__Agenda = {}  #Diccionaro Vacio
        self.__Hijos = []   #Lista Vacia 
   
    def getNombre(self):
        return self.__Nombre

    def setNombre(self,Nom):
        self.__Nombre = Nom

    def getEdad(self):
        return self.__Edad

    def setEdad(self,Ed):
        self.__Edad = Ed

    def getFechaNacimiento(self):
        return self.__Fecha_Nto

    def setFechaNacimiento(self,Fec):
        self.__Fecha_Nto = Fec

#////////////////////////////////////////////////////////////////////////////
    
    def MuestraPersona(self):
        print("Nombre: ",self.__Nombre)
        print("Edad: ",self.__Edad)
        print("Nacimiento: ",self.__Fecha_Nto)
        print("Hijos: ",self.__Hijos)
        print("Agenda: ",self.__Agenda)
    
#////////////////////////////////////////////////////////////////////////////
    
    def MuestraSoloContactos(self):
        print("Agenda: ",self.__Agenda)

#////////////////////////////////////////////////////////////////////////////

    def nacimiento(self,n_hijo):
        self.__Hijos.append(n_hijo)

#//////////////////////////////////////////////////////////////////////////// 
    
    def agregarContacto(self,N_contacto,N_celular):
        self.__Agenda[N_contacto] = N_celular

#////////////////////////////////////////////////////////////////////////////

    def modificarContacto(self,N_contac):
        if N_contac in self.__Agenda:
            nro = input("Ingrese el nuevo numero: ")
            self.__Agenda[N_contac] = nro

#////////////////////////////////////////////////////////////////////////////

    def eliminarContacto(self,E_contac):
        del self.__Agenda[E_contac]
        print("Contacto eliminado.")

#////////////////////////////////////////////////////////////////////////////

    def buscarContacto(self,Nro_contacto,Busq):
        if Nro_contacto == Busq:
            print("El contacto se encuentra en la agenda.")
        else:
            print("El contacto NO se encuentra")

#////////////////////////////////////////////////////////////////////////////

    def obtenerContacto(self,N_contacto):
        if N_contacto in self.__Agenda:
            return self.__Agenda[N_contacto]
        else:
            return "No se encuentra"
        
#////////////////////////////////////////////////////////////////////////////




#////////////////////////////////////////////////////////////////////////////

def menu():
    i=7
    while i < 0 or i > 5:  
        print("1- Instanciar a una persona.")
        print("2- Agregar hijos a la persona.")
        print("3- Ir al menu de contactos.")
        print("4- Mostrar la persona.")
        print("5- Mostrar lista de las personas instanciadas")
        print("0- Fin app")
        i = int(input("Selecciones una opcion del menu: "))
        from os import system
        system("cls")
    return i

def agenda():
    i=5
    while i < 0 or i > 4:  
        print("1- Agregar contacto.")
        print("2- Modificar contacto.")
        print("3- Eliminar contacto.")
        print("4- Buscar contacto.")
        print("0- Volver al menu.")
        i = int(input("Selecciones una opciones: "))
        from os import system
        system("cls")
    return i
