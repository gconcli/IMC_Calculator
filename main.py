print('Escreva sua altura em metros: ')
x = float(input())
print('Escreva seu peso: ')
y = float(input())

z = y / (x * x)
if z < 18.5:
    print('Seu IMC é igual a magreza')

elif z >= 18.5 and z < 25.0:
    print('Seu IMC é igual a normal')

elif z >= 25.0 and z < 30.0:
    print('Seu IMC é igual a sobrepeso')

else:
    print('Seu IMC é igual a obesidade')
