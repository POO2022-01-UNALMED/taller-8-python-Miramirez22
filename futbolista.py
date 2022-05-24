from deportista import Deportista
from persona import Persona

class Futbolista(Persona,Deportista):
    _listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,"Futbol",añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)

    def setGolesMarcados(self,goles):
        self._golesMarcados = goles
        
    def getGolesarcados(self):
        return self._golesMarcados
        
    def setTarjetasRojas(self,rojas):
        self._tarjetasRojas = rojas
        
    def getTarjetasRojas(self):
        return self._tarjetasRojas
        
    def setPiernaHabil(self,pierna):
        self._piernaHabil = pierna
        
    def getPiernaHabil(self):
        return self._piernaHabil
        
    @classmethod
    def setListaFutbolistas(cls,lista):
        cls._listaFutbolistas = lista
    
    @classmethod
    def getListaFutbolistas(cls):
        return cls._listaFutbolistas
    
    def __str__(self):
        return "Mi nombre es "+ str(self.getNombre())+" soy profesional en el deporte "+str(self.getDeporte())+" Tengo "+str(self.getEdad())+" años de edad y llevo "+str(self.getAñosPracticando())+" años en el deporte"


