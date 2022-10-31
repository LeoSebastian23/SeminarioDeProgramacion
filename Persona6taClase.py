#Objetos 

class Persona():
                        
    cantidad = 0
    def __init__ (self,Nom,Ed):
        self.__Nombre = Nom #Colocar   || .Publico || ._ Protegido || .__ Privado
        self.__Edad = Ed
        self.__Camina = False
        Persona.cantidad += 1 #Cuento la cantidad de objetos instanciados
        self.__Agenda = {} #dic
        self.__Hijos = []  #lista

    #getters y setters

    def getNombre(self):
        return self.__Nombre

    def setNombre(self,Nom):
        self.__Nombre = Nom

    def getEdad(self):
        return self.__Edad

    def setEdad(self,Ed):
        self.__Edad = Ed
    
    ######################################################################################################

    def Caminar(self):
        self.__Camina = True
    
    def Parar(self):
        self.__Camina = False 

    ######################################################################################################
    
    def MuestraPersona(self):
        print("Nombre: ",self.__Nombre)
        print("Edad: ",self.__Edad)

        if self.__Camina == True:
            print("La persona camina")
        else:
            print("La persona NO camina")

    #getters y setters

    def agregarContacto(self,N_contacto,N_celular):
        self.__Agenda[N_contacto] = N_celular

    def obtenerContacto(self,N_contacto):
        if N_contacto in self.__Agenda:
            return self.__Agenda[N_contacto]
        else:
            return "No se encuentra"

    def nacimiento(self,n_hijo):
        self.__Hijos.__add__(n_hijo)


