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
        
    def pagar_reserva(self,reserva):
        reserva.set_status("Pago")

    def cancelar_reserva(self,reserva):
        reserva.set_status("Cancelado")
        print("Reserva cancelada")

    def criar_reserva(self,voo):
        codigo = randint(0,10000)
        reserva = Reserva(codigo, self, "Pagamento pendente", voo)
        self.__reservas.append(reserva)
        voo.set_reservas(voo.get_reservas().append(reserva))
        print("Reserva realizada!")