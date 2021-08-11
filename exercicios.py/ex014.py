# Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Entre com o valor em Celcius\n'))

print('{}ºC é {}ºF'.format(cel, (cel * (9/5))+32))