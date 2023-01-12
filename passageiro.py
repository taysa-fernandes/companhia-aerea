from random import randint
class Passageiro:
    def __init__(self,cpf):
        self.__cpf=cpf
        self.reservas=[]
    def get_Cpf(self):
        return self.__cpf
    def set_Cpf(self,cpf):
        self.__cpf=cpf
    def pagarReserva(self,codigo):
        pass
    def cancelarReserva(self,codigo):
        pass
    def criarReserva(self):
        self.codigo=randint(0,10000)