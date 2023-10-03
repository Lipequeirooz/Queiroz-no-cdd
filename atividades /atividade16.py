#hora de inicio e de fim de um jogo de xadrez
inicio = int(input('digite a hora do inicio:'))
fim = int(input('digite a hora de termino:'))
duracao = 0
if inicio == fim:
    duracao = 24
elif inicio < fim:
    duracao = fim - inicio
else:
    duracao = (24 - inicio) + fim
print(f'o jogo durou:{duracao} horas.')