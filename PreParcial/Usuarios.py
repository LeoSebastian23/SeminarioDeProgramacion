
class Usuarios():
#---------------------------------- CONSTRUCTOR ----------------------------------------------------------
    def __init__(self,nombre,dni,direccion,abono):
        self.__Nombre = nombre
        self.__Dni = dni
        self.__Direccion = direccion
        self.__Categoria = ""
        self.Abono = abono
        self.__Baja = True
        #self.__TotalaPagar: 0
#------------------------------- GETTERS Y SETTERS ----------------------------------------------------------        
    def getNombre(self):
        return self.__Nombre

    def setNombre(self,Nom):
        self.__Nombre = Nom
#------------------------------- GETTERS Y SETTERS ----------------------------------------------------------        
    def getDni(self):
        return self.__Dni

    def setDni(self,dni):
        self.__Dni = dni
#------------------------------- GETTERS Y SETTERS ----------------------------------------------------------        
    def getDireccion(self):
        return self.__Direccion

    def setDireccion(self,dir):
        self.__Direccion = dir
#------------------------------- GETTERS Y SETTERS ----------------------------------------------------------        
    def getCategoria(self):
        return self.__Categoria

    def setCategoria(self,cat):
        self.__Categoria = cat

#------------------------------- GETTERS Y SETTERS ----------------------------------------------------------         
    '''
    def getAbono(self):
        return self.__Abono
    '''

    def setAbono(self,abn):
        self.__Abono = abn
    
#------------------------------- GETTERS Y SETTERS ----------------------------------------------------------        
    def getBaja(self):
        return self.__Baja

#----------------------------------- MUESTRA ----------------------------------------------------------        
        
    def Muestra(self):
        print("Nombre completo: ",self.__Nombre)
        print("DNI: ",self.__Dni)
        print("Direccion: ",self.__Direccion)
        #print("Categoria: ",self.__Categoria)
        print("Abono: ",self.Abono)

#-------------------------------------- BAJA ------------------------------------------------------------        
    def Eliminar(self):
        self.__Baja = False
#-------------------------------- CALCULAR IMPORTES -----------------------------------------------------------
    '''
    def calcularImportes(self,unidades):
        totalaPagar = (unidades * 1) + self.__Abono
        print ("total a pagar", totalaPagar)
    '''
    

