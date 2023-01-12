from datetime import datetime
class Voo:
    def __init__(self,codigo,horario,aeroportoS,aeroportoD,assentosLivres,tripulacao,tipo):
        self.__codigo=codigo
        self.__horario=horario
        self.__data=datetime.today()
        self.__aeroportoS=aeroportoS
        self.__aeroportoD=aeroportoD
        self.__assentosLivres=assentosLivres
        self.__tripulacao=tripulacao
        self.__tipo=tipo
        self.reservas=[]
    def get_Codigo(self):
        return self.__codigo
    def set_Codigo(self,codigo):
        self.__codigo=codigo
    def get_horario(self):
        return self.__horario
    def set_horario(self,horario):
        self.__horario=horario
    def get_AeroportoS(self):
        return self.__aeroportoS
    def set_AeroportoS(self,aeroportoS):
        self.__aeroportoS=aeroportoS
    def get_AeroportoD(self):
        return self.__aeroportoD
    def set_AeroportoD(self,aeroportoD):
        self.__aeroportoD=aeroportoD    
    def get_assentosLivres(self):
        return self.__assentosLivres
    def set_AssentosLivres(self,assentosLivres):
        self.__assentosLivres=assentosLivres
    def get_tripulacao(self):
        return self.__tripulacao
    def set_tripulacao(self,tripulacao):
        self.__tripulacao=tripulacao
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self,tipo):
        self.__tipo=tipo