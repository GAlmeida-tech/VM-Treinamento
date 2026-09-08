print("-" * 10, "Conversor de Temperatura", "-" * 10)
print("Escolha a opção desejada:")

print("Digite 1 para converter Celsius para Fahrenheit")
print("Digite 2 para converter Fahrenheit para Celsius")
opcao = int(input("Escolha a opção desejada: "))

if opcao == 1:
    c = float(input("Digite a temperatura em Celsius: "))
    resultado = (c * 9/5) + 32
    print("A temperatura em Fahrenheit é:", resultado)

elif opcao == 2:
    f = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = (f - 32) * 5/9
    print("A temperatura em Celsius é:", resultado)

else:
    print("Opção inválida. Por favor, escolha uma opção válida.")