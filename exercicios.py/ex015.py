km = float(input('Quantidade de KM percorrido: '))
dia = int(input('Quantidade de dias: '))
diaria = dia * 60
kmValor = km * 0.15
cotacao = diaria + kmValor

print('Valor total a ser pago R${}'.format(cotacao))
