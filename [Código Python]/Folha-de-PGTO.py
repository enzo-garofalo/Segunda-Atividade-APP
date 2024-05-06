

























def menu():
    print('='*12, 'MENU', '='*12)
    print('-'*6, '| 1- Cadastrar |', '-'*6)
    print('-'*6, '| 2- Consultar |', '-'*6)
    print('-'*6, '| 3- Remover   |', '-'*6)
    print('-'*6, '| 4- Sair      |', '-'*6)
    print('='*30)
    while True:
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