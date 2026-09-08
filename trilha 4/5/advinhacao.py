import random

print("Adivinhação Game - Viana e Moura")

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