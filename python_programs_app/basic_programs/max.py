num1 = int(input('Indique um número.\n> '))
num2 = int(input('Indique outro número.\n> '))

maximum = max(num1, num2)

if maximum == num1:
    print('O primeiro número é maior.')
else:
    print('O segundo número é maior.')