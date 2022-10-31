from Usuarios import *

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Particular(Usuarios):
    def __init__(self, nombre, dni, direccion, abono,fechaNacimiento):
        super().__init__(nombre, dni, direccion, abono)
        self.__FechaNacimiento = fechaNacimiento
        self.Categoria = "Particular"
        self.totalaPagar = 0
    
# GETTERS Y SETTERS ----------------------------------------------------------     
   
    def getFechaNaciemiento(self):
        return self.__FechaNacimiento

    def setNombre(self,FN):
        self.__FechaNacimiento = FN
    
# MUESTRA ---------------------------------------------------------- 

    def Muestra(self):
        super().Muestra()
        print("Categoria: ",self.Categoria)

#-------------------------------- CALCULAR IMPORTES -----------------------------------------------------------
       
    def calcularImportes(self,unidades):
        if unidades > 0 and unidades <= 200:
            self.totalaPagar = unidades * 0.05
        elif unidades > 200 and unidades <= 400:
            self.totalaPagar = unidades * 0.07
        elif unidades > 400 and unidades <= 1000:
            self.totalaPagar = unidades * 0.1
        elif unidades > 1000:
            self.totalaPagar = unidades * 0.12

        #self.totalaPagar = self.totalaPagar + self.__Abono
        print (self.totalaPagar)
        return self.totalaPagar
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
class Profesional(Usuarios):
    def __init__(self, nombre, dni, direccion, abono, area, titulo):
        super().__init__(nombre, dni, direccion, abono)
        self.Categoria = "Profesional"
        self.__Area = area
        self.__Titulo = titulo 
        self.totalaPagar = 0

# GETTERS Y SETTERS ----------------------------------------------------------        
    def getTitulo(self):
        return self.__Titulo

    def setTitulo(self,tlo):
        self.__Titulo = tlo

# GETTERS Y SETTERS ----------------------------------------------------------        
    def getArea(self):
        return self.__Area

    def setNombre(self,area):
        self.__Area = area   

# MUESTRA ----------------------------------------------------------  
      
    def Muestra(self):
        super().Muestra()
        print("Categoria: ",self.Categoria)
        print("Titulo: ",self.__Titulo)
        print("Area: ",self.__Area)

#-------------------------------- CALCULAR IMPORTES -----------------------------------------------------------
       
    def calcularImportes(self,unidades):
        if unidades > 0 and unidades <= 250:
            self.totalaPagar = unidades * 0.07
        elif unidades > 250 and unidades <= 500:
            self.totalaPagar = unidades * 0.11
        elif unidades > 500 and unidades <= 1000:
            self.totalaPagar = unidades * 0.13
        elif unidades > 1000:
            self.totalaPagar = unidades * 0.15

        #self.totalaPagar = self.totalaPagar + self.__Abono
        print (self.totalaPagar)
        return self.totalaPagar
       
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Comercial(Usuarios):
    def __init__(self, nombre, dni, direccion, abono, rubro, cuit):
        super().__init__(nombre, dni, direccion, abono)
        self.Categoria = "Comercial"
        self.__Rubro = rubro 
        self.__Cuit = cuit 
        self.totalaPagar = 0

# GETTERS Y SETTERS ----------------------------------------------------------  
      
    def getRubro(self):
        return self.__Rubro

    def setNombre(self,Rbo):
        self.__Rubro = Rbo

# GETTERS Y SETTERS ----------------------------------------------------------        
    def getCuit(self):
        return self.__Cuit

    def setNombre(self,CUIT):
        self.__Cuit = CUIT

# MUESTRA ---------------------------------------------------------- 

    def Muestra(self):
        super().Muestra()
        print("Categoria: ",self.Categoria)
        print("Rubro: ",self.__Rubro)
        print("Cuit: ",self.__Cuit)

#-------------------------------- CALCULAR IMPORTES -----------------------------------------------------------
       
    def calcularImportes(self,unidades):
        if unidades > 0 and unidades <= 300:
            self.totalaPagar = unidades * 0.09
        elif unidades > 300 and unidades <= 600:
            self.totalaPagar = unidades * 0.12
        elif unidades > 600 and unidades <= 1000:
            self.totalaPagar = unidades * 0.15
        elif unidades > 1000:
            self.totalaPagar = unidades * 0.17

        #self.totalaPagar = self.totalaPagar + self.__Abono
        print (self.totalaPagar)
        return self.totalaPagar
