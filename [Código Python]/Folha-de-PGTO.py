#Atividade Avaliativa 2

import os
from prettytable import PrettyTable

funcionarios = {}

def cadastrar():
    os.system('cls')
    print('='*12,"Cadastro de Funcionário",'='*13)
    while True:
        Matricula = int(input("Digite a matricula: "))
        if Matricula in funcionarios:
            print("Matrícula já existente. Digite uma matrícula válida.")
            continue
        Nome = input("Digite o nome: ")
        print('-'*20,'Funções','-'*21)
        print("-------- 101 - Vendedor | 102 - Administrativo ---")
        print('-'*50)
        Funcao = int(input('Digite a função: '))
        if Funcao == 101:
            salario_bruto = 1500.00
            valor_vendas = float(input("Digite o valor total das vendas: R$"))
        elif Funcao == 102:
            while True:
                print('-'*20,'Limites','-'*21)
                print('----- Inferior: 2150.00 | Superior: 6950.00 ------')
                print('-'*50)
                salario_bruto = float(input("Digite o salário bruto: "))
                valor_vendas = 0
                if salario_bruto < 2150 or salario_bruto > 6950:
                    print("Digite uma opção válida. (Limite inferior: 2150.00 | Limite superior: 6950.00)")
                    continue
                else:
                    break
        else:
            os.system('cls')
            print('='*6,"Digite uma opção válida para a função!",'='*6)
            print('='*15,"Reiniciando Cadastro",'='*15)
            continue

        num_faltas = int(input(f"Digite o numero de faltas do funcionário {Nome}: "))
        break
    
    print('='*50)
    funcionarios[Matricula] = [Nome, Funcao, salario_bruto, num_faltas, valor_vendas]
    # print(funcionarios)
    n_cadastro = int(input("\nDeseja cadastrar outro funcionário?\n[1-Sim | 2-Não]: "))
    if n_cadastro == 1:
        cadastrar()
    else:
        return

def remover():
    #uma vez removido, as matriculas não atualizam




    return()

def consultar():




    return

def relatorio_financeiro():

    while True:

        Matricula = int(input("Qual maltrícula do funionário que deseja fazer o cálculo: "))

        nome = funcionarios[Matricula][0]
        funcao = funcionarios[Matricula][1]
        salario_bruto = funcionarios[Matricula][2]
        num_faltas = funcionarios[Matricula][3]
        vendas_mensal = funcionarios[Matricula][4]
        
        desconto_falta = (salario_bruto/30)*num_faltas

        

        if funcao == 101:
            salario_liquido = salario_bruto - desconto_falta + (vendas_mensal*0.09)
        elif funcao == 102:
            salario_liquido = salario_bruto - desconto_falta

        tabela = PrettyTable(["Matrícula", "Nome", "Função", "Salário Bruto", "Salario Líquido", "Número de faltas", "Percentual imposto", "Desconto"])

        tabela.add_row([Matricula, nome, funcao, f"R$ {salario_bruto:.2f}", f"R$ {salario_liquido:.2f}", num_faltas, f"{percentual_imposto}%", f"{desconto_falta:.2f}"])
        
        print(tabela)

        nova_consulta = int(input("Deseja fazer nova consulta? 1 (sim) | 2 (não). R: "))
        
        if nova_consulta == 1:
            continue
        else:
            return

    

def menu():
    while True:
        os.system('cls')
        print('='*12, 'MENU', '='*12)
        print('-'*6, '| 1- Cadastrar |', '-'*6)
        print('-'*6, '| 2- Consultar |', '-'*6)
        print('-'*6, '| 3- Remover   |', '-'*6)
        print('-'*6, '| 4- Relatório |', '-'*6)
        print('-'*6, '| 5- Sair      |', '-'*6)
        print('='*30)
        escolha = int(input("O que deseja fazer? "))
        if escolha == 1:
            cadastrar()
        elif escolha == 2:
            consultar()
        elif escolha == 3:
            remover()
        elif escolha == 4:
            relatorio_financeiro()
        elif escolha == 5:
            print('='*12,'ATÉ LOGO!','='*12)
            exit()
        else:
            print("Digite uma opção válida!")
            continue

menu()