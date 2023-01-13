
from aeroporto import Aeroporto
from voo import Voo
from operadores import Operadores
from passageiro import Passageiro

list_aeroportos = [Aeroporto("Pau dos Ferros", "Aeroporto Internacional de Viracopos", 70), Aeroporto("Natal", "Aeroporto Internacional de Natal", 200)]
list_voos = [Voo("13:40", list_aeroportos[0], list_aeroportos[1],660,12,"nacionais")]
list_operadores = [Operadores("2022109403000")]
list_passageiros = [Passageiro("12312312345")]

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
        print("Digite respectivamente o horário(ex: 14:30), o número do aeroporto de partida, o número\ndo aeroporto de destino,o número de assentos livres, tamanho da tripulação e o tipo (internacionais ou nacionais):")
        horario = input()
        aeroportoP = int(input())
        aeroportoD = int(input())
        assentos = int(input())
        tripulacao = int(input())
        tipo = input()
        voo = Voo(horario, list_aeroportos[aeroportoP], list_aeroportos[aeroportoD], assentos,tripulacao,tipo)
        list_voos.append(voo)

    if option == 2:
        pular_linhas()
        print("============ LISTA DE VOOS: ============")
        for x in range(len(list_voos)):
            print("{}.{}".format(x, list_voos[x].get_name()))
        print("=========================================")
        print("\n" * 2)

    if option == 3:
        pular_linhas()
        print("Digite o número do Voo:")
        number = int(input())
        pular_linhas()
        print("==================================================================================")
        print(list_voos[number])

def category_passageiro():
    pular_linhas()
    print("============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n1.Criar Passageiro\n2.Ver lista de Passageiros\n3.Criar Reserva\n4.Pagar Reserva\n5.Cancelar Reserva\n6.Reservas de 1 passageiro\n7.Sair\n=================================================================")
    option = int(input())

    if option == 1:
        pular_linhas()
        print("Digite o CPF do passageiro:")
        cpf = input()
        list_passageiros.append(Passageiro(cpf))

    if option == 2:
        pular_linhas()
        print("============ LISTA DE PASSAGEIROS: ============")
        for x in range(len(list_passageiros)):
            print("{}. {}".format(x, list_passageiros[x].get_cpf()))
        print("===============================================")
        print("\n" * 2)

    if option == 3:
        pular_linhas()
        print("Digite respectivamente o número do Voo e o número do passageiro:")
        voo = int(input())
        passageiro = int(input())

        voo = list_voos[voo]
        passageiro = list_passageiros[passageiro]
        
        passageiro.criar_reserva(voo)

    if option == 4:
        pular_linhas()
        print("Digite respectivamente o número do passageiro e o código da reserva:")
        passageiro = int(input())
        code = float(input())
        passageiro= list_passageiros[passageiro]
        passageiro.pagar_reserva(code)

    if option == 5:
        pular_linhas()
        print("Digite respectivamente o número do passageiro e o código da reserva:")
        passageiro = int(input())
        code = float(input())
        passageiro= list_passageiros[passageiro]
        passageiro.cancelar_reserva(code)

    if option == 6:
        pular_linhas()
        print("Digite o número do passageiro:")
        passageiro = int(input())
        reserevas  = list_passageiros[passageiro].get_reservas()
        
        print(reserevas)
        pular_linhas()
        for x in range(len(reserevas)):
            print("{}.{}".format(x,reserevas[x]))

def category_operador():
    pular_linhas()
    print("============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n1.Criar Operador\n2.Ver lista de Operadores\n3.Criar Reserva\n4.Cancelar Reserva\n5.Sair\n=================================================================")
    option = int(input())

    if option == 1:
        pular_linhas()
        print("Digite a matricula do operador:")
        matricula = input()
        operador = Operadores(matricula)
        list_operadores.append(operador)
    
    if option == 2:
        pular_linhas()
        print("============ LISTA DE OPERADORES: ============")
        for x in range(len(list_operadores)):
            print("{}.{}".format(x, list_operadores[x].get_matricula()))
        print("==============================================")
        print("\n" * 2)
    
    if option == 3:
        pular_linhas()
        print("Digite respectivamente o número do operador, o número do voo e o número do passageiro:")
        index = int(input())
        voo = int(input())
        passageiro = int(input())
        operador = list_operadores[index]
        voo = list_voos[voo]
        passageiro = list_passageiros[passageiro]
        operador.criar_reserva(voo,passageiro)
    
    if option == 4:
        pular_linhas()
        print("Digite respectivamente o número do operador, número do passageiro e o código da reserva:")
        operador = int(input())
        passageiro = int(input())
        code = float(input())
        operador = list_operadores[operador]
        passageiro = list_passageiros[passageiro]

        operador.cancelar_reserva(code,passageiro)

    
while True:
    print("============ DIGITE O NÚMERO DA CATEGORIA DESEJADA: ============\n1.Aeroporto\n2.Voo\n3.Passageiro\n4.Operador\n5.Sair\n=================================================================")
    option = int(input())
    if option == 1:
        category_aeroporto()
    if option == 2:
        category_voo()
    if option == 3:
        category_passageiro()
    if option == 4:
        category_operador()
    if option >= 5 or  option < 1:
        break