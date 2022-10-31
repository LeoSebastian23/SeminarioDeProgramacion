class vehiculo():
    def __init__(self, marca, modelo, ruedas):
        self.__ruedas = ruedas
        self.__marca = marca
        self.__modelo = modelo
        self.estado = False
        self.acelera = False
        self.frenar = True
    
     #---------------------------getters y setters -----------------------------
    def getNombre(self):
        return self.__Nombre
        
    def setNombre(self,Nom):
        self.__Nombre = Nom

    #--------------------------------------------------------------------------
    def parar (self):
        self.estado =False
    #--------------------------------------------------------------------------
    def acelerar (self):
        self.acelera =True
    #--------------------------------------------------------------------------
    def parar (self):
        self.estado =False
    #--------------------------------------------------------------------------
    
    def muestraVehiculo(self):
        print(self.__marca)
        print(self.__modelo)
        print(self.__ruedas)
        if self.estado:
            print("El vehiculo esta en Marcha.")
        else:
            print("El vehiculo esta parado.")
        if self.acelera:
            print("El vehiculo esta circulando")
        else:
            print("El vehiculo no circula")

#########################################################################################################

class pickup(vehiculo):
    def __init__(self, marca, modelo, ruedas,kg):
        super().__init__(marca, modelo, ruedas)        
        self.kg = kg
#--------------------------------------------------------------------------
    def carga(self,kg):
        if self.kg + kg > 200:
            print("Es mucha carga")
        else: 
            self.kg += kg  
#--------------------------------------------------------------------------
    def descargar(self,kg):
        if self.kg >= kg :
            print("Se descargo", kg , "Kg")
            self.kg -= kg
        else:
            print("No se puede descargar esa cantidad")

#########################################################################################################

class vehiculoJuguete():
    def __init__(self):
        self.__edad = (2,4)
    
    def getEdad(self):
        return self.__edad

    def setEdad (self,edad):
        self.__edad = edad

#########################################################################################################

class camion(vehiculo,vehiculoJuguete):
    
    def __init__(self, marca, modelo, ruedas):
        super().__init__(marca, modelo, ruedas)
    
    largo = 50
    autonomia = 30 
    def setLargo(self,L):
        self.largo = L
    def setAutonomia(self,aut):
        self.autonomia = aut
    def getAutonomia(self):
        return self.autonomia
    def getLargo(self):
        return self.largo

class moto(vehiculo):
    def __init__(self, marca, modelo, ruedas):
        super().__init__(marca, modelo, ruedas)