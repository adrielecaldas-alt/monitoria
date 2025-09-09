
# Exercicios de Python - Lista 1
# Adriele Caldas Novaes

# 1)
print('Alo mundo')

# 2)
numero = input('O numero informado foi:')
print('O numero informado foi:', numero)

# 3) 
n1 = int(input('Digite numero 1:'))
n2 = int(input('Digite numero 2:'))
soma = n1 + n2
print('A soma entre', n1, 'e', n2, 'é igual a:', soma)


# 4)
n1 = int(input('Digite nota 1:'))
n2 = int(input('Digite nota 2:'))
n3 = int(input('Digite nota 3:'))
n4 = int(input('Digite nota 4:'))
media = (n1 + n2 + n3 + n4) / 4
print('A media entre as notas é:', media)

# 5)
m = float(input('Digite a medida em metros:'))
cm = m * 100
print('A medida em centimetros é:', cm)

# 6)
import math
r = float(input('Digite o valor do raio:'))
area = math.pi * (r ** 2)
print('A area do circulo é:', area)

# 7)
lado = float(input('Digite o valor do lado do quadrado:'))
area = lado * lado
print('O valor do lado do quadrado é:', area)
print('O valor do dobro da area do quadrado é:', area * 2)

# 8)
h = float(input('Digite quanto ganha por hora:'))
n = int(input('Digite o numero de horas trabalhadas no mes:'))
salario = h * n
print('O salario do mes é:', salario)

# 9)
f = float(input('Digite a temperatura em fahrenheit:'))
c = 5 * (f - 32) / 9
print('A temperatura em celsius é:', c)

# 10)
c = float(input('Digite a temperatura em celsius:'))
f = (c * 9 / 5) + 32
print('A temperatura em fahrenheit é:', f)

# 11)
n1 = int(input('Digite numero inteiro 1:'))
n2 = int(input('Digite numero inteiro 2:'))
n3 = float(input('Digite numero real 3:'))
operacao1 = (n1 * 2) * (n2 / 2)
operacao2 = (n1 * 3) + n3
operacao3 = (n3 ** 3)
print('O resultado da primeira operacao é:', operacao1)
print('O resultado da segunda operacao é:', operacao2)
print('O resultado da terceira operacao é:', operacao3)

# 12)
g = float(input('Digite o valor em gigabytes:'))
m = g * 1024
print('O valor em megabytes é:', m)

# 13)
g = float(input('Digite o valor em gigabytes:'))
m = float(input('Digite o valor em megabytes:'))
t = (g * 1024) + m
print('O valor em terabytes é:', t / 1024)
