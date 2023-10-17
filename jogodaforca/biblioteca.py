import random

def jogodaforca():
    
    def escolher_palavr():
        palavras = [('lobo', 'animal que vive em alcateia'),
                    ('caminhao', 'veiculo que faz entregas'),
                    ('escola', 'local onde estudamos '),]
        palavra, dica = random.choice(palavras)
        return palavra, dica
    def mostrar_forca(erros):
        partes_forca = [" O", "/|\\", ' / \\']
        print('\n ============ FORCA ===========') 
        for i in range (erros):
            if i < len(partes_forca):
                print(partes_forca[i])
        print('==========================\n') 
        
        def ocultar_letras(palavra, letras_certas):
            resultado = ''
            for letra in palavra:
                if letra in letras_certas:
                    resultado += letra
                else:
                    resultado += '_'
            return resultado
        def jogo_da_forca():
            print('========================'
            "Bem vindo ao jogo da forca!\n"
            '==========================\n')
            
            palavra,dica = escolher_palavr()
            letras_certas = []
            letras_erradas = []
            tentativas = 0
            max_tentativas = 3
            
            print(f'diga: {dica}')
            palavra_oculta = ocultar_letras(palavra, letras_certas)
            print(f' Palavra: {palavra_oculta}')

            while True:
                letra = input('digite uma letra:').lower()
                
                if letra in letras_certas:
                    print(' voce ja tentou essa letra')
                    continue

                if letra in letras_erradas:
                    print('voce ja tentou essa letra e errou')
                    continue
                
                if letra in palavra:
                    letras_certas.append(letra)
                    palavra_oculta = ocultar_letras(palavra, letras_certas)
                    print(f'Palavra: {palavra_oculta}')

                if palavra_oculta == palavra:
                    print('\n ======================'
                              'Parabéns! Voce venceu.'
                              '==========================')

                    break
            else:
                letras_erradas.append(letra)
                tentativas += 1 
                mostrar_forca(tentativas)

                if tentativas == max_tentativas:
                    print(f' fim do jogo! voce perdeu. a palavra era {palavra}')
                       

            while True: 
                print('Jogo da forca')
                
                escolha = input('escolha o numero da palavra (1 a 3) ou 0 para sair:')
                if escolha == '0':
                    break
                elif escolha in '123':
                    jogo_da_forca()
                else:
                    print('escolha invalida tente novamente')