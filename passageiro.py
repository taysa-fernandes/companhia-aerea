from random import randint
from reserva import Reserva
class Passageiro:
    def __init__(self,cpf):
        self.__cpf=cpf
        self.__reservas = []

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self,cpf):
        self.__cpf=cpf

    def get_reservas(self):
        return self.__reservas

    def set_reservas(self,reservas):
        self.__reservas = reservas
    
    def add_reserva(self,reserva):
        self.__reservas.append(reserva)

    def pagar_reserva(self,code):
        reserva = next(x for x in self.__reservas if x.get_codigo() == code )
        reserva.set_status("Pago")
        print("Reserva pago")

    def cancelar_reserva(self,code):
        reserva = next(x for x in self.__reservas if x.get_codigo() == code )
        reserva.set_status("Cancelado")
        print("Reserva cancelada")

    def criar_reserva(self,voo):
        codigo = randint(0,10000)
        Reserva(codigo, self, "Pagamento pendente", voo)
        print("Reserva realizada!")
    