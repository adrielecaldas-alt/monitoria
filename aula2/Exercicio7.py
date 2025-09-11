# 7)
a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))
if a == 0:
    print('Não é equação de segundo grau')
else:
    delta = (b**2 - 4*a*c)
    if delta < 0:
        print('Não existem raízes reais')
    elif delta == 0:
        print('Existe uma raiz real')
    else:
        print('Existem duas raízes reais')
