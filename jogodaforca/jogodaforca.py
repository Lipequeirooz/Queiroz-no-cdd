from biblioteca import jogodaforca

verificador = 's'
while verificador in 'sS':
    print('\n\n Jogo da forca\n'
    '1 - Jogar \n'
    '0 - encerrar jogo \n')
    opc = input('escolha um opção:')
    while opc not in '10':
        ops = input('opcao invalida, tente novamente \n'
                    'escolha uma opção acima')
    
    if opc == '1':
        jogodaforca()
    
    elif opc in '0':
        verificador = '0'
        print(' finalizand o jogo')
    
    else:
        print('opção invlaida, tente novamente')