import random

while True:
    try:
        print("\n", "-"*10, "Menu - Viana & Moura", "-" * 10)

        opcao = int(input("""
    1 - Calculadora
    2 - Conversor de Temperatura
    3 - Média de Notas
    4 - Jogo de Adivinhação
    0 - Sair
    Escolha uma Opção: """))


        if opcao == 1:
            print("\n", "-" * 10, "Calculadora Viana e Moura", "-" * 10)

            print("""Digite 1 para somar
    Digite 2 para subtrair
    Digite 3 para multiplicar
    Digite 4 para dividir
    Digite 0 para SAIR do programa""")
            
            try:
                opcao_calc = int(input("Escolha uma opção: " ))

                if opcao_calc == 1:
                    num1 = int(input("Digite o primeiro número: "))
                    num2 = int(input("Digite o segundo número: "))
                    resultado = num1 + num2
                    print("O resultado da soma é:", resultado)

                elif opcao_calc == 2:
                    num1 = int(input("Digite o primeiro número: "))
                    num2 = int(input("Digite o segundo número: "))
                    resultado = num1 - num2
                    print("O resultado da subtração é:", resultado)

                elif opcao_calc == 3:
                    num1 = int(input("Digite o primeiro número: "))
                    num2 = int(input("Digite o segundo número: "))
                    resultado = num1 * num2
                    print("O resultado da multiplicação é:", resultado)

                elif opcao_calc == 4:
                    num1 = int(input("Digite o primeiro número: "))
                    num2 = int(input("Digite o segundo número: "))
                    if num2 == 0:
                        print("Erro: Divisão por zero não é permitida.")
                    else:
                        resultado = num1 / num2
                        print("O resultado da divisão é:", resultado)

                elif opcao_calc == 0:
                    print("Saindo da Calculadora")
                    continue
                    
                else:
                    print("-" * 10, "Digite um numero Válido!", "-" * 10)
                    continue
            except:
                print("Digite apenas Opções disponiveis no Menu Calculadora")
                continue          
            
                

            



        elif opcao == 2:
            try:
                print("\n", "-" * 10, "Conversor de Temperatura", "-" * 10)
                print("""Escolha a opção desejada: 
        Digite 1 para converter Celsius para Fahrenheit
        Digite 2 para converter Fahrenheit para Celsius""")

                opcao_temperatura = int(input("Escolha a opção desejada: "))

                if opcao_temperatura == 1:
                    c = float(input("Digite a temperatura em Celsius: "))
                    resultado = (c * 9/5) + 32
                    print("A temperatura em Fahrenheit é:", resultado)

                elif opcao_temperatura == 2:
                    f = float(input("Digite a temperatura em Fahrenheit: "))
                    resultado = (f - 32) * 5/9
                    print("A temperatura em Celsius é:", resultado)

                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
                    continue

            except:
                print("Digite apenas Opções disponiveis")
                continue



        elif opcao == 3:
            print("\n", "-" * 10, "Média das Notas Viana e Moura", "-" * 10)

            notas = []

            while True:
                nota = input("Digite Notas ou Digite 'fim' para finalizar o programa. ")

                if nota == "fim" and notas == []:
                    print("Digite pelo menos uma nota antes de finalizar o programa: ")

                elif nota == "fim":
                    print("Programa finalizado!")
                    break

                else:
                    try:
                        notas.append(float(nota))
                        print("Nota Atribuida!")
                    except:
                        print("Siga as intruções e Escolha a(s) Opção(S) Válida(S)")
                        continue

                


            print("Notas digitadas:", notas)
            media = sum(notas) / len(notas)
            print(f"A média das notas digitadas é: {media}")

            if media >= 7:
                print("Aprovado!")
            else:
                print("Reprovado!")



        elif opcao == 4:
            print("\n", "-" * 10, "Adivinhação Game - Viana e Moura", "-" * 10)
            print("Tente Adivinhar o número Sorteado!")

            numero_sorteado = random.randint(1, 100)
            tentativas = 0


            while True:
                try:
                    chute = int(input("Digite seu chute: "))
                    tentativas += 1

                    if chute < numero_sorteado:
                        print("O número sorteado é MAIOR que o seu chute!")

                    elif chute > numero_sorteado:
                        print("O número sorteado é MENOR que o seu chute!")

                    else:
                        print("Parabéns! Você acertou!")
                        print("Número sorteado:", numero_sorteado)
                        print("Tentativas:", tentativas)
                        break

                except Exception as erro:
                    print(f"erro ocorrido: {erro}")
                    print("Entrada inválida! Digite apenas um número.")


        elif opcao == 0:
            print("Saindo do Programa!")
            break

        else:
            print("Digite um número Válido do Menu!")
            continue

    except:
        print("Digite apenas Números!")
        continue