v1 = float(input('digite um valor'))
v2 = float(input('digite um valor'))
while v1 == v2:
    print('valor inválido, digite novamente')
    v2 = float(input('digite o 2 valor, diferente do primeiro'))
if v1 > v2:
    print(f'valores em ordem crescente {v2}, {v1}')
else:
    print(f'valores em ordem c  rescente {v1}, {v2}')