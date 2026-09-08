print("Contador Viana e Moura")

direcao = int(input("1 para iniciar a contagem crescente ou 0 para iniciar a contagem decrescente: "))
if direcao != 1 and direcao != 0:
    print("Opção inválida. Por favor, digite 1 para contagem crescente ou 0 para contagem decrescente.")
    exit()

passo_contagem = int(input("Digite o passo da contagem (Ex: 1 em 1 ou 2 em 2): "))

inicio = int(input("Digite um número para iniciar a contagem: "))
fim = int(input("Digite um número para finalizar a contagem: "))


if direcao == 1:
    while inicio <= fim:
        print(inicio)
        inicio += passo_contagem

elif direcao == 0:
    while inicio >= fim:
        print(inicio)
        inicio -= passo_contagem


