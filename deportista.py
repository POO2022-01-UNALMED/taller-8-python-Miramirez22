class Deportista:
    def __init__(self,deporte,añosPracticando):
        self._deporte = deporte
        self._añosPraticando = añosPracticando
    
    def setDeporte(self,deporte):
        self._deporte = deporte
    
    def getDeporte(self):
        return self._deporte
    
    def setAñosPracticando(self,años):
        self._añosPraticando = años
    
    def getAñosPracticando(self):
        return self._añosPraticando