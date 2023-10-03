#votos nulos, em branc e validos em um municipio
eleitores = int(input("Digite o número total de eleitores: "))
validos = int(input('quantos votos foram validos?'))
branco = int(input('quantos votos foram em branco?'))
nulos = int(input('quantos votos foram  nulos?'))
percentualvalidos = (validos / eleitores ) * 100
percentualbranco = (branco / eleitores) * 100
percentualnulo = (nulos / eleitores) * 100
print(f' o percuntual de validos é {percentualvalidos}%')
print(f'o percentual de branco é {percentualbranco}%')
print(f'o percentual de nulo é {percentualnulo}%')
