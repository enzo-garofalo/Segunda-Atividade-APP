#Atividade Avaliativa 2
#Objetivos:

#3) Determinar a folha de pagamento de um determinado funcionário
        # Esta opção deverá imprimir todas as informações sobre o funcionário incluindo o valor do percentual do imposto

# 5. Imprimir as informações do funcionário com maior salário líquido
        # Esta opção deverá imprimir Matrícula, Nome, Código da Função, salário bruto, percentual de imposto e salário líquido

# 6. Imprimir as informações do funcionário com o maior número de faltas no mês
        # Esta opção deverá imprimir a Matrícula, Nome, Código da Função, Número de Faltas e desconto no salário do funcionário
#_______________________________________________________________________________________________________________________________

import os
from prettytable import PrettyTable

funcionarios = {1: ['Enzo', 101, 1500.0, 4, 20000.0], 2: ['Rogério', 102, 6000.0, 0, 0],  3: ['Bruno', 102, 6950.0, 0, 0] }
    
# COMPLETO
def cadastrar():
    os.system('cls')
    print('='*12,"Cadastro de Funcionário",'='*13)
    # Validação das entradas pelos laços While True
    while True:
        Matricula = int(input("Digite a matricula: "))
        if Matricula in funcionarios:
            print("\n"+"="*13,"Matrícula já existente","="*13)
            continue
        else:
            break

    Nome = input("Digite o nome: ").title()
    print('-'*20,'Funções','-'*21)
    print("-------- 101 - Vendedor | 102 - Administrativo ---")
    print('-'*50)

    while True:
        Funcao = int(input('Digite a função: '))
        if Funcao in [101, 102]:
            break
        else:
            print("\n"+"="*12,"Digite uma opção válida","="*13)
            continue
        
    if Funcao == 101:
        salario_bruto = 1500.00
        valor_vendas = float(input("Digite o valor total das vendas: R$"))
    elif Funcao == 102:
        print('-'*20,'Limites','-'*21)
        print('----- Inferior: 2150.00 | Superior: 6950.00 ------')
        print('-'*50)
        while True:
            salario_bruto = float(input("Digite o salário bruto: "))
            valor_vendas = 0
            if salario_bruto < 2150 or salario_bruto > 6950:
                print("\n"+"="*12,"Digite uma opção válida","="*13)
                continue
            else:
                break


    num_faltas = int(input(f"Digite o numero de faltas do funcionário {Nome}: "))

    
    print('='*50)
    funcionarios[Matricula] = [Nome, Funcao, salario_bruto, num_faltas, valor_vendas]
    print(funcionarios)
    n_cadastro = int(input("\nDeseja cadastrar outro funcionário?\n[1-Sim | 2-Não]: "))
    if n_cadastro == 1:
        cadastrar()
    else:
        return
# COMPLETO
def remover():
    
    os.system('cls')        
    print('='*14, 'Remover Funcionário', '='*15)
    opcao = int(input("Deseja listar os funcionários?\n[1-Sim | 2-Não]: "))
    
    if opcao == 1:
        print('='*82)
        construtorTabelas()
        print('='*82)

    while True:
        matricula_remover = int(input("Digite a matrícula do funcionário que deseja remover: "))
        valores = funcionarios.get(matricula_remover, False)
        if not valores:
            print('\n'+'='*30,'Matrícula Não Existe', '='*30)
            continue
        else:
            break

    print(f"\nDeseja realmente excluir funcionário(a) {valores[0]}")
    opcao2 = int(input("[1-Sim | 2-Não]: "))
    if opcao2 == 1:
        valor_remover = funcionarios.pop(matricula_remover, None)
        print('='*25,f"Funcionário {valor_remover[0]} removido!",'='*26)

    print('\n'+'='*82)    
    escolha = int(input(f"Deseja remover algum funcionário?\n[1-Sim | 2-Não]: "))
    if escolha == 1:
        remover()
    else:
        return    
# COMPLETO
def escolha_consultar():
    while True:
        print('='*14,'Consultar Relatórios','='*14)
        print('-'*14,'|1- Por Funcionário|','-'*14)
        print('-'*14,'|2- Exibir Todos   |','-'*14)
        print('-'*14,'|3- Maior Salário  |','-'*14)
        print('-'*14,'|4- Maior Faltas   |','-'*14)
        print('='*50)
        busca = int(input("O que deseja fazer? "))
        if busca not in [1,2,3,4]:
            os.system('cls')
            print("\n"+"="*12,"Digite uma opção válida","="*13)
            continue
        else:
            break
    return busca

def consultar():
    os.system('cls')
    busca = escolha_consultar()
    matriculas_para_busca = []
    if busca == 2:
        construtorTabelas()
    else:
        print('\nEstamos Trabalhando......')

    escolha = int(input("\nDeseja fazer outra busca?\n[1-Sim | 2-Não]: "))
    if escolha == 1:
        consultar()
    else:
        return

def construtorTabelas():

    tabela = PrettyTable(["Matricula","Nome", "Função","Vendas Mensal","Salário Líquido", "Salário Bruto"])
    tabela.align = 'l'

    for matricula in funcionarios.keys():
        nome = funcionarios[matricula][0]
        funcao = funcionarios[matricula][1]
        salario_bruto = funcionarios[matricula][2]
        num_faltas = funcionarios[matricula][3]
        desconto_falta = (salario_bruto/30)*num_faltas

        if funcao == 101:
            valor_vendas = funcionarios[matricula][4]
        else:
            valor_vendas = 0
        
        salario_liquido, percentual = det_salario_liquido(salario_bruto, num_faltas, valor_vendas)
        
            

        tabela.add_row([matricula, nome, funcao, f'R$ {valor_vendas:.2f}', f'R$ {salario_liquido:.2f}', f'R$ {salario_bruto:.2f}'])
    print(tabela)
    return 

def det_salario_liquido(salario_bruto, num_faltas, valor_vendas):

    salario_bruto_tratado  = salario_bruto - (salario_bruto / 30 * num_faltas) + (valor_vendas * 0.09)

    if salario_bruto_tratado  <= 2259.20:
        percentual_imposto = 0 
    
    elif salario_bruto_tratado  <= 2828.65:
        percentual_imposto = 7.5
    
    elif salario_bruto_tratado  <= 3751.05:
        percentual_imposto = 15

    elif salario_bruto_tratado  <= 4664.68:
        percentual_imposto = 22.5
    
    else:
        percentual_imposto = 27.5

    salario_liquido = salario_bruto_tratado - (salario_bruto_tratado * percentual_imposto/100) 
    return salario_liquido, percentual_imposto

def menu():
    while True:
        os.system('cls')
        print('='*22, 'Menu', '='*22)
        print('-'*16, '| 1- Cadastrar |', '-'*16)
        print('-'*16, '| 2- Consultar |', '-'*16)
        print('-'*16, '| 3- Remover   |', '-'*16)
        print('-'*16, '| 4- Sair      |', '-'*16)
        print('='*50)
        escolha = int(input("O que deseja fazer? "))
        if escolha == 1:
            cadastrar()
        elif escolha == 2:
            consultar()
        elif escolha == 3:
            remover()
        elif escolha == 4:
            print('='*20,'Até Logo','='*20)
            exit()
        else:
            print("Digite uma opção válida!")
            continue

menu()
