class Person():
    def __init__(self, edad, peso, altura, nombre):
        self.__edad = edad
        self.__peso = peso
        self.__altura = altura
        self.__nombre = nombre
        self.__camina = False
        self.__lee = False

    #---------------------------getters y setters -----------------------------
    '''
    
    '''
    def caminar(self):
        self.__camina = True
    #--------------------------------------------------------------------------
    def leer(self):
        self.leer = True
    #--------------------------------------------------------------------------
    def __estado(self): #Metodo encapsulado - protegido
        if self.__camina == True:
            if self.__lee == True:
                return "La persona camina y lee"
            else:
                return "La persona camina pero no lee"
        else:
            if self.__lee == True:
                return "La persona esta parada pero lee"
            else:
                return "La persona esta parada y no lee"
    #--------------------------------------------------------------------------
    def muestra(self):
        print("Nombre: ", self.__nombre)
        print("Edad: ", self.__edad)
        print("Altura :", self.__altura)
        print("Peso: ", self.__peso)
        print("Estado: ", self.__estado())

#########################################################################################################

class vehiculo():
    def __init__(self, marca, modelo, ruedas):
        self.__ruedas = ruedas
        self.__marca = marca
        self.__modelo = modelo
        self.estado = False
        self.acelera = False
        self.frenar = True
    
     #---------------------------getters y setters -----------------------------
    '''
    
    '''
    def arrancar (self):
        self.estado =True
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

   
        