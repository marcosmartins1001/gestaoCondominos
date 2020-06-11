#FEITO POR Marcos Martins Camelo

cpfs = ['111.444.433-85', '402.899.391-72', '305.505.401-21', '690.240.112-24']
nomes = ['Marcos Martins Camelo', 'Lucas Paiva', 'Vinicius Padilha', 'Carlos Sodré']
apartamentos = ['401', '402', '403', '404']
debitos = ['Pagador', 'Devedor', 'Pagador', 'Devedor']

menu_principal = int(input('MENU PRINCIAL \n'
                           '1 - Inserir um novo condômino \n'
                           '2 - Consultar condôminos pelo cpf \n' 
                           '3 - Atualizar o débito do condôminos pelo cpf \n' 
                           '4 - Exibir os condôminos devedores \n'
                           '5 - Exibir os condôminos quites \n'
                           '6 - Remover os condôminos \n'
                           '0 - Sair do programa \n'
                           'Digite aqui: '))

if menu_principal == 1:
    cpf_cond = input('CPF: ')
    cpfs.append(cpf_cond)
    nome_cond = str(input('Nome: '))
    nomes.append(nome_cond)
    ap_cond = int(input('Apartamento: '))
    apartamentos.append(ap_cond)
    debito_cond = str(input('Débito: '))
    debitos.append(debito_cond)
    print('Condômino adicionado com sucesso! \n')
    while True:
        print('Pressiona a tecla 1 para retornar ao menu principal.')
        opcao = int(input('> '))
        if opcao == 1:
            menu_principal = int(input('MENU PRINCIAL \n'
                                       '1 - Inserir um novo condômino \n'
                                       '2 - Consultar condôminos pelo cpf \n'
                                       '3 - Atualizar o débito do condôminos pelo cpf \n'
                                       '4 - Exibir os condôminos devedores \n'
                                       '5 - Exibir os condôminos quites \n'
                                       '6 - Remover os condôminos \n'
                                       '0 - Sair do programa \n'
                                       'Digite aqui: '))
        break

if menu_principal == 2:
    consultacpf = str(input(' \n \nDigite o CPF: '))
    if consultacpf == '111.444.433-85':
        print(' CPF:', cpfs[0], '\n', 'Nome: ', nomes[0], '\n', 'Apartamento:', apartamentos[0], '\n', 'Débito:',
              debitos[0], '\n')
    elif consultacpf == '402.899.391-72':
        print(' CPF:', cpfs[1], '\n', 'Nome: ', nomes[1], '\n', 'Apartamento:', apartamentos[1], '\n', 'Débito:',
              debitos[1], '\n')
    elif consultacpf == '305.505.401-21':
        print(' CPF:', cpfs[2], '\n', 'Nome: ', nomes[2], '\n', 'Apartamento:', apartamentos[2], '\n', 'Débito:',
              debitos[2], '\n')
    elif consultacpf == '690.240.112-24':
        print(' CPF:', cpfs[3], '\n', 'Nome: ', nomes[3], '\n', 'Apartamento:', apartamentos[3], '\n', 'Débito:',
              debitos[3], '\n')
    else:
        print('CPF não cadastrado! \n')
    while True:
        print('Pressiona a tecla 1 para retornar ao menu principal.')
        opcao = int(input('> '))
        if opcao == 1:
            menu_principal = int(input('MENU PRINCIAL \n'
                                       '1 - Inserir um novo condômino \n'
                                       '2 - Consultar condôminos pelo cpf \n'
                                       '3 - Atualizar o débito do condôminos pelo cpf \n'
                                       '4 - Exibir os condôminos devedores \n'
                                       '5 - Exibir os condôminos quites \n'
                                       '6 - Remover os condôminos \n'
                                       '0 - Sair do programa \n'
                                       'Digite aqui: '))
            break

if menu_principal == 3:
    procurar_cpf = input('Digite o CPF: ')

    if procurar_cpf == '111.444.433-85':
        attdebito = str(input('1 - Pagador \n'
                              '2 - Devedor \n'
                              '>'))
        if attdebito == 1:
            debitos[0] = "Pagador"
            print('o CPF: {} foi colocado no grupo de pagadores! \n' .format(procurar_cpf))
        elif attdebito == 2:
            debitos[0] = "Devedor"
            print('o CPF: {} foi colocado no grupo de devedores! \n'.format(procurar_cpf))
    while True:
        print('Pressiona a tecla 1 para retornar ao menu principal.')
        opcao = int(input('> '))
        if opcao == 1:
            menu_principal = int(input('MENU PRINCIAL \n'
                                       '1 - Inserir um novo condômino \n'
                                       '2 - Consultar condôminos pelo cpf \n'
                                       '3 - Atualizar o débito do condôminos pelo cpf \n'
                                       '4 - Exibir os condôminos devedores \n'
                                       '5 - Exibir os condôminos quites \n'
                                       '6 - Remover os condôminos \n'
                                       '0 - Sair do programa \n'
                                       'Digite aqui: '))
        break

if menu_principal == 4:
    print('LISTA DE DEVEDORES \n')
    print(' CPF:', cpfs[1], '\n', 'Nome: ', nomes[1], '\n', 'Apartamento:', apartamentos[1], '\n', 'Débito:',
              debitos[1], '\n')
    print(' CPF:', cpfs[3], '\n', 'Nome: ', nomes[3], '\n', 'Apartamento:', apartamentos[3], '\n', 'Débito:',
              debitos[3], '\n')
    while True:
        print('Pressiona a tecla 1 para retornar ao menu principal.')
        opcao = int(input('> '))
        if opcao == 1:
            menu_principal = int(input('MENU PRINCIAL \n'
                                       '1 - Inserir um novo condômino \n'
                                       '2 - Consultar condôminos pelo cpf \n'
                                       '3 - Atualizar o débito do condôminos pelo cpf \n'
                                       '4 - Exibir os condôminos devedores \n'
                                       '5 - Exibir os condôminos quites \n'
                                       '6 - Remover os condôminos \n'
                                       '0 - Sair do programa \n'
                                       'Digite aqui: '))
        break

if menu_principal == 5:
    print('LISTA DE PAGADORES \n')
    print(' CPF:', cpfs[0], '\n', 'Nome: ', nomes[0], '\n', 'Apartamento:', apartamentos[0], '\n', 'Débito:',
              debitos[0], '\n')
    print(' CPF:', cpfs[2], '\n', 'Nome: ', nomes[2], '\n', 'Apartamento:', apartamentos[2], '\n', 'Débito:',
              debitos[2], '\n')
    while True:
        print('Pressiona a tecla 1 para retornar ao menu principal.')
        opcao = int(input('> '))
        if opcao == 1:
            menu_principal = int(input('MENU PRINCIAL \n'
                                       '1 - Inserir um novo condômino \n'
                                       '2 - Consultar condôminos pelo cpf \n'
                                       '3 - Atualizar o débito do condôminos pelo cpf \n'
                                       '4 - Exibir os condôminos devedores \n'
                                       '5 - Exibir os condôminos quites \n'
                                       '6 - Remover os condôminos \n'
                                       '0 - Sair do programa \n'
                                       'Digite aqui: '))
        break

if menu_principal == 6:
    procurar_cpf = input('Digite o CPF: ')

    if procurar_cpf == '111.444.433-85' or '402.899.391-72' or '305.505.401-21' or '690.240.112-24':
        attdebito = str(input('1 - Remover Condômino \n'
                              '> '))
        if attdebito == 1:
            del(cpfs[0], nomes[0], apartamentos[0], debitos[0])
        print('O condômino de CPF: {} foi removido com sucesso! \n'.format(procurar_cpf))
    while True:
        print('Pressiona a tecla 1 para retornar ao menu principal.')
        opcao = int(input('> '))
        if opcao == 1:
            menu_principal = int(input('MENU PRINCIAL \n'
                                       '1 - Inserir um novo condômino \n'
                                       '2 - Consultar condôminos pelo cpf \n'
                                       '3 - Atualizar o débito do condôminos pelo cpf \n'
                                       '4 - Exibir os condôminos devedores \n'
                                       '5 - Exibir os condôminos quites \n'
                                       '6 - Remover os condôminos \n'
                                       '0 - Sair do programa \n'
                                       'Digite aqui: '))
        break

if menu_principal == 0:
    print(' \nPROGRAMA FINALIZADO!')
    exit()
