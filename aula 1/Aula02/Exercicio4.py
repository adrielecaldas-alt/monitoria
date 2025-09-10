# 4)
l1 = float(input('Digite o lado 1 do triangulo:'))
l2 = float(input('Digite o lado 2 do triangulo:'))
l3 = float(input('Digite o lado 3 do triangulo:'))

if l1 == l2 == l3:
    print('O triangulo é equliatero:')
elif l1 == l2 or l1 == l3:
     print('O triangulo é isoceles:') 
else:
     print('O triangulo é escaleno:')         