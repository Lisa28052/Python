
print('Calculadora')
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
operacao = int(input('Escolha sua operação, 1, 2, 3 ou 4:'))
numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input('Digite o segundo número:'))

if operacao == 1:
    print (numero1 + numero2) 
elif operacao == 2:
    print(numero1 - numero2)
elif operacao == 3:
    print(numero1 * numero2)
else:
    if numero2 != 0:
        print(numero1 / numero2)
    else:
        print('Operação inválida. Não é possível dividir por zero.')


