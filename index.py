
from aeroporto import Aeroporto
from voo import Voo

list_aeroportos = [Aeroporto("Pau dos Ferros", "Aeroporto Internacional de Viracopos", 70), Aeroporto("Natal", "Aeroporto Internacional de Natal", 200)]
list_voos = [Voo("13:40", list_aeroportos[0], list_aeroportos[1],660,12,"nacionais")]

def pular_linhas():
    print("\n" * 130)

def category_aeroporto():
    pular_linhas()
    print("============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n1.Criar Aeroporto\n2.Ver lista de Aeroportos\n3.Sair\n=================================================================")
    option = int(input())

    if option == 1:
        pular_linhas()
        print("Digite respectivamente o nome da cidade, nome do aeroporto e a capacidade de decolagem:")
        city = input()
        name = input()
        capacity = int(input())
        aeroporto = Aeroporto(city,name,capacity)
        list_aeroportos.append(aeroporto)

    if option == 2:
        pular_linhas()
        print("============ LISTA DE AEROPORTOS: ============")
        for x in range(len(list_aeroportos)):
            print("{}.{}".format(x, list_aeroportos[x]))
        print("==============================================")
        print("\n" * 2)
    
def category_voo():
    pular_linhas()
    print("============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n1.Criar Voo\n2.Ver lista de Voos\n3.Ver dados de um Voo\n4.Sair\n=================================================================")
    option = int(input())
    if option == 1:
        pular_linhas()
        print("Digite respectivamente o horário(ex: 14:30), o número do aeroporto de partida,o número do aeroporto de destino,o número de assentos livres e tamanho da tripulação:")
        horario = input()
        aeroportoP = int(input())
        aeroportoD = int(input())
        assentos = int(input())
        tripulacao = int(input())
        voo = Voo(horario, list_aeroportos[aeroportoP], list_aeroportos[aeroportoD], assentos,tripulacao)
        list_voos.append(voo)

    if option == 2:
        pular_linhas()
        print("============ LISTA DE VOOS: ============")
        for x in range(len(list_voos)):
            print("{}.{}".format(x, list_voos[x].get))
        print("=========================================")
        print("\n" * 2)

while True:
    print("============ DIGITE O NÚMERO DA CATEGORIA DESEJADA: ============\n1.Aeroporto\n2.Voo\n3.Passageiro\n4.Operador\n5.Sair\n=================================================================")
    option = int(input())
    if option == 1:
        category_aeroporto()
    if option >= 5 or  option < 1:
        break