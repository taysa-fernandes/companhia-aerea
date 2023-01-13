class Aeroporto:
    def __init__(self,cidade,nome,capacidadeDecolagem):
        self.__cidade=cidade
        self.__nome=nome
        self.__capacidadeDecolagem=capacidadeDecolagem

    def get_Cidade(self):
        return self.__cidade

    def set_Cidade(self,cidade):
        self.__cidade=cidade

    def get_nome(self):
        return self.__nome

    def set_nome(self,nome):
        self.__nome=nome

    def get_capacidadeDecolagem(self):
        return self.__capacidadeDecolagem

    def set_capacidadeDecolagem(self,capacidadeDecolagem):
        self.__capacidadeDecolagem=capacidadeDecolagem
    
    def __str__(self):
        return "{}/Cidade:{}/Capacidade de decolagem".format(self.__nome,self.__cidade,self.__capacidadeDecolagem)