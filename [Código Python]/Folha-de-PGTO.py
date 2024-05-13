#Atividade Avaliativa 2 - Testes
import os
from prettytable import PrettyTable

funcionarios = {}

def cadastrar():
    os.system('cls')
    while True:
        print('='*35)
        Matricula = int(input("Qual a matricula do funcionário? "))
        if Matricula in funcionarios:
            print("Matrícula já existente. Digite uma matrícula válida.")
            continue
        Nome = input("Digite o nome do funcionário: ")
        Funcao = int(input("101 - vendedor | 102 Administrativo\nQual a função? "))

        if Funcao == 101:
            salario_bruto = 1500.00
        elif Funcao == 102:
            while True:
                salario_bruto = float(input("Digite o salário bruto: (Limite inferior: 2150.00 | Limite superior: 6950.00). Salário: "))
                if salario_bruto < 2150 or salario_bruto > 6950:
                    print("Digite uma opção válida. (Limite inferior: 2150.00 | Limite superior: 6950.00)")
                    continue
                else:
                    break
        else:
            print("Digite uma opção válida. 101 - vendedor | 102 Administrativo")
            continue
        num_faltas = int(input(f"Digite o numero de faltas do funcionário {Nome}: "))
        
        funcionarios[Matricula] = [Nome, Funcao, salario_bruto, num_faltas ]

        print(funcionarios)
        n_cadastro = int(input("Deseja cadastrar outro funcionário? 1 (sim) | 2 (não). R: "))
        if n_cadastro == 1:
            continue
        else:
            return

def remover():
    #uma vez removido, as matriculas não atualizam




    return()

def consultar():




    return

def relatorio_financeiro():

    vendas_mensal = 0 #como será adicionada a venda mensal / deve ser venda por func ou por mês
    
    return()




def menu():
    while True:
        os.system('cls')
        print('='*12, 'MENU', '='*12)
        print('-'*6, '| 1- Cadastrar |', '-'*6)
        print('-'*6, '| 2- Consultar |', '-'*6)
        print('-'*6, '| 3- Remover   |', '-'*6)
        print('-'*6, '| 4- Sair      |', '-'*6)
        print('='*30)
        escolha = int(input("O que deseja fazer? "))
        if escolha == 1:
            cadastrar()
        elif escolha == 2:
            consultar()
        elif escolha == 3:
            remover()
        elif escolha == 4:
            print('='*12,'ATÉ LOGO!','='*12)
            exit()
        else:
            print("Digite uma opção válida!")
            continue

menu()