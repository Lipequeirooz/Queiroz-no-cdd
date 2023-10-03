duzia = 1.00
unidade = 1.30
quantidade = int(input('quantas maçãs você deseja?'))
if quantidade < 12:
    total = quantidade * unidade
else:
    total = quantidade * duzia
print(f' você vai pagar: {total:.2f}R$')