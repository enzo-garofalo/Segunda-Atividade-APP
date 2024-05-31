
import os
from prettytable import PrettyTable

funcionarios = {}
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
            print('-'*50)
            break

    Nome = input("Digite o nome: ").title()


    print('\n'+'='*20,'Funções','='*21)
    print("         101 - Vendedor | 102 - Administrativo ")
    print('='*50)

    while True:
        Funcao = int(input('Digite a função: '))
        if Funcao in [101, 102]:
            break
        else:
            print("\n"+"="*12,"Digite uma opção válida","="*13)
            continue
        
    if Funcao == 101:
        salario_bruto = 1500.00
        print('-'*50)
        valor_vendas = float(input("Digite o valor total das vendas: R$ "))
        print('-'*50)

    elif Funcao == 102:
        valor_vendas = 0
        print('\n'+'='*20,'Limites','='*21)
        print('      Inferior: 2150.00 | Superior: 6950.00')
        print('='*50)
        while True:
            salario_bruto = float(input("Digite o salário bruto: "))
            if salario_bruto < 2150 or salario_bruto > 6950:
                print("\n"+"="*12,"Digite uma opção válida","="*13)
                continue
            else:
                print('-'*50)
                break
    
    while True:
        num_faltas = int(input(f"Digite o numero de faltas do funcionário {Nome}: "))
        if num_faltas > 31:
            print("\n"+"="*13,"Digite um valor válido","="*13)
            continue
        else:
            break

    print('='*50)
    funcionarios[Matricula] = [Nome, Funcao, salario_bruto, num_faltas, valor_vendas]
    
    n_cadastro = int(input("Deseja cadastrar outro funcionário?\n[1-Sim | 2-Não]: "))
    if n_cadastro == 1:
        cadastrar()
    else:
        return
    
def escolha_consultar():
    while True:
        print('='*45,'Consultar Relatórios','='*45)
        print('-'*43,'| 1- Por Funcionário |','-'*45)
        print('-'*43,'| 2- Exibir Todos    |','-'*45)
        print('-'*43,'| 3- Maior Salário   |','-'*45)
        print('-'*43,'| 4- Maior Faltas    |','-'*45)
        print('='*112)
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

    if busca == 1:
        print('-'*112)
        funcionario_buscado = int(input('Digite a Matrícula do funcionário: '))
        tabela = PrettyTable(["Matricula","Nome", "Função","Salário Bruto", "Salário Líquido", "Percentual de Imposto","Vendas Mensal", "Num. faltas", "Desconto Faltas"])
        matriculas_para_busca.append(funcionario_buscado)
    
    elif busca == 2:
        tabela = PrettyTable(["Matricula","Nome", "Função","Salário Bruto","Salário Líquido"])
        matriculas_para_busca = funcionarios.copy()
    
    elif busca == 3:
        tabela = PrettyTable(["Matricula","Nome", "Função","Salário bruto","Percentual de Imposto", "Salário Líquido"])
        matriculas_para_busca = maior_salario()
    
    elif busca == 4:
        tabela = PrettyTable(["Matricula","Nome", "Função", "Num. faltas", "Desconto Faltas"])
        matriculas_para_busca = maior_faltas()
    
    construtorTabelas(matriculas_para_busca, tabela, busca)

    escolha = int(input("\nDeseja fazer outra busca?\n[1-Sim | 2-Não]: "))
    if escolha == 1:
        consultar()
    else:
        return

def construtorTabelas(matriculas_para_busca, tabela, busca):
    
    for matricula in matriculas_para_busca:

        if matricula not in  funcionarios.keys():
            print(' '*43,"Matrícula Não encontrada")
            return
        
        nome, funcao, salario_bruto, num_faltas, valor_vendas, desconto  = ObterDados(matricula)
        salario_liquido, percentual = det_salario_liquido(salario_bruto, num_faltas, valor_vendas)

        if busca == 1:
            tabela.add_row([matricula, nome, funcao,f'R${salario_bruto:.2f}',f'R${salario_liquido:.2f}',f'{percentual}%',f'R${valor_vendas:.2f}',f'{num_faltas}',f'R${desconto:.2f}'])
        
        elif busca == 2:
            tabela.add_row([matricula, nome, funcao, f'R${salario_bruto:.2f}', f'R${salario_liquido:.2f}'])
        
        elif busca == 3:
            tabela.add_row([matricula, nome, funcao, f'R${salario_bruto:.2f}',f'{percentual}%', f'R${salario_liquido:.2f}'])
        
        elif busca == 4:
            tabela.add_row([matricula, nome, funcao, f'{num_faltas}', f'R${desconto:.2f}'])
        
    print(tabela)
    return

def ObterDados(matricula):

    nome = funcionarios[matricula][0]
    funcao = funcionarios[matricula][1]
    salario_bruto = funcionarios[matricula][2]
    num_faltas = funcionarios[matricula][3]
    valor_vendas = funcionarios[matricula][4]
    desconto = salario_bruto/30*num_faltas

    return nome, funcao, salario_bruto, num_faltas, valor_vendas, desconto

def maior_faltas():
    maior_faltas = 0
    matriculas_maior_faltas = []

    for matricula in funcionarios:
        if funcionarios[matricula][3] > maior_faltas:
            maior_faltas = funcionarios[matricula][3]
            matriculas_maior_faltas.clear()
            matriculas_maior_faltas.append(matricula)
        elif funcionarios[matricula][3] == maior_faltas:
            matriculas_maior_faltas.append(matricula)
           
    return matriculas_maior_faltas

def maior_salario():

    maior_sal_liquido = 0
    maior_sal_matricula = []

    for matricula in funcionarios:
        
        nome, funcao, salario_bruto, num_faltas, valor_vendas, desconto  = ObterDados(matricula)
        auxiliar = det_salario_liquido(salario_bruto,num_faltas,valor_vendas)

        if auxiliar[0] > maior_sal_liquido:
            maior_sal_liquido = auxiliar[0]
            maior_sal_matricula.clear()
            maior_sal_matricula.append(matricula)
        
        elif auxiliar[0] == maior_sal_liquido:
            maior_sal_matricula.append(matricula)
    
    return maior_sal_matricula

def remover():
    
    os.system('cls')        
    print('='*30, 'Remover Funcionário', '='*31)
    opcao = int(input("Deseja listar os funcionários?\n[1-Sim | 2-Não]: "))
    
    if opcao == 1:
        print('='*82)
        tabela = PrettyTable(["Matricula","Nome", "Função","Salário Bruto","Salário Líquido"])

        construtorTabelas(funcionarios.keys(), tabela, 2)
        print('='*82)

    while True:
        matricula_remover = int(input("Digite a matrícula do funcionário que deseja remover: "))
        valores = funcionarios.get(matricula_remover, False)
        if not valores:
            print('\n'+'='*30,'Matrícula Não Existe', '='*30)
            continue
        else:
            break
    
    print('-'*82)
    print(f"Deseja realmente excluir funcionário(a) {valores[0]}?")
    opcao2 = int(input("[1-Sim | 2-Não]: "))
    if opcao2 == 1:
        valor_remover = funcionarios.pop(matricula_remover, None)
        print('\n'+'='*82)
        print(' '*26,f"Funcionário {valor_remover[0]} removido!")

    print('='*82)    
    escolha = int(input(f"Deseja remover algum funcionário?\n[1-Sim | 2-Não]: "))
    if escolha == 1:
        remover()
    else:
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
