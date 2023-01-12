from reserva import Reserva
from random import randint
class Operadores:
    def __init__(self,matricula):
        self.__matricula=matricula
        self.__reservas=[]
    def get_matricula(self):
        return self.__matricula
    def set_matricula(self,matricula):
        self.__matricula=matricula
    def get_reservas(self):
        return self.__reservas
    def set_reservas(self,reservas):
        self.__reservas=reservas
    def criarReserva(self,voo,passageiro):
        self.codigo=randint(0,10000)
        Reserva(self.codigo,self.Operadores(),passageiro)
        self.__reservas.append(Reserva)
        print("Reserva realizada!")
    def cancelarReserva(self,codigo):
        self.__reservas.remove(codigo)
        print("Reserva cancelada")