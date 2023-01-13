from reserva import Reserva
from random import randint
class Operadores:
    def __init__(self,matricula):
        self.__matricula= matricula
    
    def get_matricula(self):
        return self.__matricula

    def set_matricula(self,matricula):
        self.__matricula=matricula

    def criar_reserva(self,voo,passageiro):
        codigo = randint(0,10000)
        reserva = Reserva(codigo, passageiro, "Pagamento pendente", voo)
        passageiro.set_voo(passageiro.get_)
        voo.set_reservas(voo.get_reservas().append(reserva))
        print("Reserva realizada!")


    def cancelar_reserva(self,reserva):
        reserva.set_status("Cancelado")
        print("Reserva cancelada")