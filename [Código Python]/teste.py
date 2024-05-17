#Atividade Avaliativa 2
#Objetivos:
#1) Inserir funcionários

#2) Remover funcionários

#3) Determinar a folha de pagamento de um determinado funcionário
        # Esta opção deverá imprimir todas as informações sobre o funcionário incluindo o valor do percentual do imposto

# 4. Determinar um relatório com o salário bruto e líquido de todos os funcionários
        # Esta opção deverá imprimir uma tabela contendo a Matrícula, Nome, Código da Função, 
        # Salário Bruto e Salário Líquido de cada funcionário

# 5. Imprimir as informações do funcionário com maior salário líquido
        # Esta opção deverá imprimir Matrícula, Nome, Código da Função, salário bruto, percentual de imposto e salário líquido

# 6. Imprimir as informações do funcionário com o maior número de faltas no mês
        # Esta opção deverá imprimir a Matrícula, Nome, Código da Função, Número de Faltas e desconto no salário do funcionário
#_______________________________________________________________________________________________________________________________

import os
from prettytable import PrettyTable

funcionarios = {1: ['Enzo', 101, 1500.0, 4, 20000.0], 2: ['Rogério', 102, 6000.0, 0, 0] }
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
# COMPLETO - (AJUSTAR ESTILO)
def remover():
    
    os.system('cls')        
    print('='*50)
    opcao = int(input("Deseja listar os funcionários? 1-SIM | 2-NÃO R: "))
    if opcao == 1:
        tabela = PrettyTable(["Matricula", "Funcionário"])
        for Matricula, nome in funcionarios.items():
            nome = funcionarios[Matricula][0]
            tabela.add_row([Matricula, nome])
        print(tabela)

    matricula_remover = int(input("Qual a matricula do funcionário que deseja remover? R: "))
    valores = funcionarios.get(matricula_remover, "Matrícula não encontrada")
    print(f"Deseja realmente excluir este funcionário ", end= " ")
    print(valores)
    opcao2 = int(input("1 (sim) | 2 (não). R: "))
    if opcao2 == 1:
        valor_remover = funcionarios.pop(matricula_remover, None)
        print(f"Funcionário {valor_remover} removido!")
        
    opcao3 = int(input(f"Desesja nova remoção? 1 (sim) | 2 (não). R: "))
    if opcao3 == 1:
        remover()
    else:
        return    

def escolha_consultar():
    while True:
        print('='*14,'Consultar Relatórios','='*14)
        print('-'*14,'|1- Por Funcionário|','-'*14)
        print('-'*14,'|2- Exibir Todos   |','-'*14)
        print('-'*14,'|3- Maior Salário  |','-'*14)
        print('-'*14,'|4- Maior Faltas   |','-'*14)
        print('='*50)
        escolha = int(input("O que deseja fazer? "))
        if escolha not in [1,2,3,4]:
            os.system('cls')
            print("\n"+"="*12,"Digite uma opção válida","="*13)
            continue
        else:
            break
    return escolha

def consultar():
  os.system('cls')
  escolha = escolha_consultar()
  matriculas = []
  if escolha != 2:
      print('\nEstamos Trabalhando......')
      
  if escolha == 2:
      for matricula, informacoes in funcionarios.items():
        construtorTabelas(matricula, informacoes)
  

def construtorTabelas(matricula, informacoes):

    nome = informacoes[0]
    funcao = informacoes[1]
    salario_bruto = informacoes[2]
    num_faltas = informacoes[3]
    desconto_falta = (salario_bruto/30)*num_faltas
    salario_liquido = salario_bruto - desconto_falta

    tabela = PrettyTable(["Descrição","Valor"])
    
    tabela.align = 'l'
    tabela.title = f'Matrícula: {matricula}'

    tabela.add_row(['Nome:', nome])
    tabela.add_row(['Função:', funcao])

    if funcao == 101:
      vendas_mensal = funcionarios[matricula][4]
      salario_liquido += (vendas_mensal*0.09)
      tabela.add_row(['Vendas No Mês: ', f'R$ {vendas_mensal:.2f}'])

    tabela.add_row(['Sálario Líquido:', f'R$ {salario_liquido:.2f}'])
    tabela.add_row(['Salário Bruto:', f'R$ {salario_bruto:.2f}'])

    print(tabela)
    return 

def relatorio_financeiro():
    while True:

        Matricula = int(input("Qual maltrícula do funionário que deseja fazer o cálculo: "))

        


        tabela = PrettyTable(["Matrícula", "Nome", "Função", "Salário Bruto", "Salario Líquido", "Número de faltas", "Percentual imposto", "Desconto"])

        
        print(tabela)

        nova_consulta = int(input("Deseja fazer nova consulta? 1 (sim) | 2 (não). R: "))
        
        if nova_consulta == 1:
            continue
        else:
            return

def menu():
    while True:
        os.system('cls')
        print('='*22, 'Menu', '='*22)
        print('-'*16, '| 1- Cadastrar |', '-'*16)
        print('-'*16, '| 2- Consultar |', '-'*16)
        print('-'*16, '| 3- Remover   |', '-'*16)
        print('-'*16, '| 4- Relatório |', '-'*16)
        print('-'*16, '| 5- Sair      |', '-'*16)
        print('='*50)
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
            print('='*12,'Até Logo','='*12)
            exit()
        else:
            print("Digite uma opção válida!")
            continue
        break

menu()