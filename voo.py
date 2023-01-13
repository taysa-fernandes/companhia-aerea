import datetime
from random import randint
class Voo:
    def __init__(self,horario,aeroportoS,aeroportoD,assentosLivres,tripulacao,tipo):

        self.__codigo=randint(0,10000)
        self.__horario=horario
        self.__data = datetime.date.today()
        self.__aeroportoS=aeroportoS
        self.__aeroportoD=aeroportoD
        self.__assentosLivres=assentosLivres
        self.__tripulacao=tripulacao
        self.__tipo=tipo
        self.__reservas=[]

    def get_name(self):
        return "{} => {} ({} | {})".format(self.__aeroportoS.get_nome(), self.__aeroportoD.get_nome(), self.__horario,self.__data)

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self,codigo):
        self.__codigo=codigo

    def get_horario(self):
        return self.__horario

    def set_horario(self,horario):
        self.__horario=horario

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_aeroportoS(self):
        return self.__aeroportoS

    def set_aeroportoS(self,aeroportoS):
        self.__aeroportoS=aeroportoS

    def get_aeroportoD(self):
        return self.__aeroportoD

    def set_aeroportoD(self,aeroportoD):
        self.__aeroportoD=aeroportoD    

    def get_assentosLivres(self):
        return self.__assentosLivres

    def set_assentosLivres(self,assentosLivres):
        self.__assentosLivres=assentosLivres

    def get_tripulacao(self):
        return self.__tripulacao

    def set_tripulacao(self,tripulacao):
        self.__tripulacao=tripulacao

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self,tipo):
        self.__tipo=tipo
    
    def get_reservas(self):
        return self.__reservas

    def set_reservas(self, reservas):
        self.__reservas = reservas

    def __str__(self):
        return "{}\nTipo: {}\nQtd.Assentos Vagos: {}\nTripulação\n: {}\nReservas:{}".format(self.get_name(),self.__tipo,self.__assentosLivres - len(self.__reservas),self.__tripulacao,self.__reservas)