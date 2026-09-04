print("Calculadora Viana e Moura")

print("Digite 1 para somar")
print("Digite 2 para subtrair")
print("Digite 3 para multiplicar")
print("Digite 4 para dividir")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("O resultado da soma é:", resultado)

elif opcao == 2:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 - num2
    print("O resultado da subtração é:", resultado)

elif opcao == 3:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 * num2
    print("O resultado da multiplicação é:", resultado)

elif opcao == 4:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = num1 / num2
        print("O resultado da divisão é:", resultado)

elif opcao > 5:
    print("Opção inválida. Por favor, escolha uma opção válida.")

  