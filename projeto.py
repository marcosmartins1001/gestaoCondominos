#FEITO POR Marcos Martins Camelo;
#Este programa é um projeto que foi desenvolvido no P1;
#Todas as informações tem que ser alteradas manualmente, pois não tem um BD;

cpfs = ['111.444.455-89', '402.899.391-72', '305.505.401-21', '690.240.112-24']
nomes = ['Marcos Martins Camelo', 'Lucas Paiva', 'Vinicius Padilha', 'Carlos Sodré']
apartamentos = ['401', '402', '403', '404']
debitos = ['Pagador', 'Devedor', 'Pagador', 'Devedor']

def linha(tam = 42):
    return '-' * tam

def menu(txt):
    print(linha())
    print(txt)
    print(linha())

menu('MENU PRINCIAL \n \n'
     '1 - Inserir um novo condômino \n'
     '2 - Consultar condôminos pelo cpf \n'
     '3 - Atualizar o débito do condôminos pelo cpf \n'
     '4 - Exibir os condôminos devedores \n'
     '5 - Exibir os condôminos quites \n'
     '6 - Remover os condôminos \n'
     '0 - Sair do programa \n')

menu_principal = int(input('Sua opção: '))

while menu_principal:
    if menu_principal == 1:
        print(linha())
        print('Insira abaixo as informações')
        print(linha())
        cpf_cond = input('CPF: ')
        cpfs.append(cpf_cond)
        nome_cond = str(input('Nome: '))
        nomes.append(nome_cond)
        ap_cond = int(input('Apartamento: '))
        apartamentos.append(ap_cond)
        debito_cond = str(input('Débito(Pagador ou Devedor): '))
        debitos.append(debito_cond)
        print('Condômino adicionado com sucesso! \n')
        while True:
            print(linha())
            print('Pressiona a tecla 1 para retornar ao menu principal.')
            print(linha())
            opcao = int(input('> '))
            if opcao == 1:
                menu_principal = int(input(menu('MENU PRINCIAL \n \n'
                                                '1 - Inserir um novo condômino \n'
                                                '2 - Consultar condôminos pelo cpf \n'
                                                '3 - Atualizar o débito do condôminos pelo cpf \n'
                                                '4 - Exibir os condôminos devedores \n'
                                                '5 - Exibir os condôminos quites \n'
                                                '6 - Remover os condôminos \n'
                                                '0 - Sair do programa \n')))
            break

    if menu_principal == 2:
        print(linha())
        print('Insira abaixo as informações')
        print(linha())
        consultacpf = str(input(' \n \nDigite o CPF: '))
        if consultacpf == '111.444.455-89':
            print('\n CPF:', cpfs[0], '\n', 'Nome: ', nomes[0], '\n', 'Apartamento:', apartamentos[0], '\n', 'Débito:',
            debitos[0], '\n')
        if consultacpf == '402.899.391-72':
            print('\n CPF:', cpfs[1], '\n', 'Nome: ', nomes[1], '\n', 'Apartamento:', apartamentos[1], '\n', 'Débito:',
            debitos[1], '\n')
        if consultacpf == '305.505.401-21':
            print('\n CPF:', cpfs[2], '\n', 'Nome: ', nomes[2], '\n', 'Apartamento:', apartamentos[2], '\n', 'Débito:',
            debitos[2], '\n')
        if consultacpf == '690.240.112-24':
            print('\n CPF:', cpfs[3], '\n', 'Nome: ', nomes[3], '\n', 'Apartamento:', apartamentos[3], '\n', 'Débito:',
            debitos[3], '\n')
        while True:
            print(linha())
            print('Pressiona a tecla 1 para retornar ao menu principal.')
            print(linha())
            opcao = int(input('> '))
            if opcao == 1:
                menu_principal = int(input(menu('MENU PRINCIAL \n \n'
                                                '1 - Inserir um novo condômino \n'
                                                '2 - Consultar condôminos pelo cpf \n'
                                                '3 - Atualizar o débito do condôminos pelo cpf \n'
                                                '4 - Exibir os condôminos devedores \n'
                                                '5 - Exibir os condôminos quites \n'
                                                '6 - Remover os condôminos \n'
                                                '0 - Sair do programa \n')))
            break

    if menu_principal == 3:
        print(linha())
        print('Insira abaixo as informações')
        print(linha())
        procurar_cpf = input('Digite o CPF: ')

        if procurar_cpf == '111.444.455-89':
            attdebito = int(input('1 - Pagador \n'
                                  '2 - Devedor \n'
                                  '> '))
            if attdebito == 1:
                debitos[0] = "Pagador"
                print('o CPF: {} foi colocado no grupo de pagadores! \n' .format(procurar_cpf))
            elif attdebito == 2:
                debitos[0] = "Devedor"
                print('o CPF: {} foi colocado no grupo de devedores! \n'.format(procurar_cpf))

        if procurar_cpf == '402.899.391-72':
            attdebito = int(input('1 - Pagador \n'
                                  '2 - Devedor \n'
                                  '> '))
            if attdebito == 1:
                debitos[1] = "Pagador"
                print('o CPF: {} foi colocado no grupo de pagadores! \n'.format(procurar_cpf))
            elif attdebito == 2:
                debitos[1] = "Devedor"
                print('o CPF: {} foi colocado no grupo de devedores! \n'.format(procurar_cpf))

        if procurar_cpf == '305.505.401-21':
            attdebito = int(input('1 - Pagador \n'
                                  '2 - Devedor \n'
                                  '> '))
            if attdebito == 1:
                debitos[2] = "Pagador"
                print('o CPF: {} foi colocado no grupo de pagadores! \n'.format(procurar_cpf))
            elif attdebito == 2:
                debitos[2] = "Devedor"
                print('o CPF: {} foi colocado no grupo de devedores! \n'.format(procurar_cpf))

        if procurar_cpf == '690.240.112-24':
            attdebito = int(input('1 - Pagador \n'
                                  '2 - Devedor \n'
                                  '>'))
            if attdebito == 1:
                debitos[3] = "Pagador"
                print('o CPF: {} foi colocado no grupo de pagadores! \n'.format(procurar_cpf))
            elif attdebito == 2:
                debitos[3] = "Devedor"
                print('o CPF: {} foi colocado no grupo de devedores! \n'.format(procurar_cpf))
        else:
            print('CPF não cadastrado!')
        while True:
            print(linha())
            print('Pressiona a tecla 1 para retornar ao menu principal.')
            print(linha())
            opcao = int(input('> '))
            if opcao == 1:
                menu_principal = int(input(menu('MENU PRINCIAL \n \n'
                                                '1 - Inserir um novo condômino \n'
                                                '2 - Consultar condôminos pelo cpf \n'
                                                '3 - Atualizar o débito do condôminos pelo cpf \n'
                                                '4 - Exibir os condôminos devedores \n'
                                                '5 - Exibir os condôminos quites \n'
                                                '6 - Remover os condôminos \n'
                                                '0 - Sair do programa \n')))
            break

    if menu_principal == 4:
        print(linha())
        print('LISTA DE DEVEDORES \n')
        print(' CPF:', cpfs[1], '\n', 'Nome: ', nomes[1], '\n', 'Apartamento:', apartamentos[1], '\n', 'Débito:',
                  debitos[1], '\n')
        print(' CPF:', cpfs[3], '\n', 'Nome: ', nomes[3], '\n', 'Apartamento:', apartamentos[3], '\n', 'Débito:',
                  debitos[3], '\n')
        while True:
            print(linha())
            print('Pressiona a tecla 1 para retornar ao menu principal.')
            print(linha())
            opcao = int(input('> '))
            if opcao == 1:
                menu_principal = int(input(menu('MENU PRINCIAL \n \n'
                                                '1 - Inserir um novo condômino \n'
                                                '2 - Consultar condôminos pelo cpf \n'
                                                '3 - Atualizar o débito do condôminos pelo cpf \n'
                                                '4 - Exibir os condôminos devedores \n'
                                                '5 - Exibir os condôminos quites \n'
                                                '6 - Remover os condôminos \n'
                                                '0 - Sair do programa \n')))
            break

    if menu_principal == 5:
        print(linha())
        print('LISTA DE PAGADORES \n')
        print(' CPF:', cpfs[0], '\n', 'Nome: ', nomes[0], '\n', 'Apartamento:', apartamentos[0], '\n', 'Débito:',
                  debitos[0], '\n')
        print(' CPF:', cpfs[2], '\n', 'Nome: ', nomes[2], '\n', 'Apartamento:', apartamentos[2], '\n', 'Débito:',
                  debitos[2], '\n')
        while True:
            print(linha())
            print('Pressiona a tecla 1 para retornar ao menu principal.')
            print(linha())
            opcao = int(input('> '))
            if opcao == 1:
                menu_principal = int(input(menu('MENU PRINCIAL \n \n'
                                                '1 - Inserir um novo condômino \n'
                                                '2 - Consultar condôminos pelo cpf \n'
                                                '3 - Atualizar o débito do condôminos pelo cpf \n'
                                                '4 - Exibir os condôminos devedores \n'
                                                '5 - Exibir os condôminos quites \n'
                                                '6 - Remover os condôminos \n'
                                                '0 - Sair do programa \n')))
            break

    if menu_principal == 6:
        procurar_cpf = input('Digite o CPF: ')

        if procurar_cpf == '111.444.455-89' or '402.899.391-72' or '305.505.401-21' or '690.240.112-24':
            attdebito = str(input('1 - Remover Condômino \n'
                                  '> '))
            if attdebito == 1:
                del(cpfs[0], nomes[0], apartamentos[0], debitos[0]) #Modificar manualmente ou usar um BD
            print('O condômino de CPF: {} foi removido com sucesso! \n' .format(procurar_cpf))
        while True:
            print(linha())
            print('Pressiona a tecla 1 para retornar ao menu principal.')
            print(linha())
            opcao = int(input('> '))
            if opcao == 1:
                menu_principal = int(input(menu('MENU PRINCIAL \n \n'
                                                '1 - Inserir um novo condômino \n'
                                                '2 - Consultar condôminos pelo cpf \n'
                                                '3 - Atualizar o débito do condôminos pelo cpf \n'
                                                '4 - Exibir os condôminos devedores \n'
                                                '5 - Exibir os condôminos quites \n'
                                                '6 - Remover os condôminos \n'
                                                '0 - Sair do programa \n')))
            break

    if menu_principal == 0:
        print(linha())
        print(' \nPROGRAMA FINALIZADO!')
        print(linha())
        exit()
