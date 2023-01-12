from operadores import Operadores
from passageiro import Passageiro
class Reserva:
    def __init__(self,codigo,operador,passageiro):
        self.__codigo=codigo
        self.__operador=Operadores()
        self.__passageiro=Passageiro()
    def get_codigo(self):
        return self.__codigo
    def set_codigo(self,codigo):
        self.__codigo=codigo
    def cancelarReserva(self):
        pass
        