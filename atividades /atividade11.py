#leia a idade de alguém sendo expressa em  anos, meses e dias.
#mes 30 dias e ano 365
idade = int(input('digite a sua idade'))
meses = int(input('mês que nasceu'))
dias = int(input('dia que nasceu'))
idadeatual = (idade * 365) + (meses * 30) + dias
print(f' {idadeatual} dias vividos.')