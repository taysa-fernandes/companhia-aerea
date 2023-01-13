class Reserva:

    def __init__(self,codigo,passageiro,status,voo):
        self.__codigo=codigo
        self.__passageiro=passageiro
        self.__status = status
        self.__voo = voo

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self,codigo):
        self.__codigo=codigo

    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = status
    
    def get_passageiro(self):
        return self.__passageiro
    
    def get_passageiro(self, passageiro):
        self.__passageiro = passageiro

    def get_voo(self):
        return self.__voo
    
    def get_voo(self, voo):
        self.__voo = voo