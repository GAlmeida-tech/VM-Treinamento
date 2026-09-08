print("Média das Notas Viana e Moura")
print("Programa iniciado! Digite 'fim' para finalizar o programa.")

notas = []

while True:
    nota = input("Digite uma nota (ou 'fim' para finalizar): ")
    if nota == "fim" and notas == []:
        print("Digite pelo menos uma nota antes de finalizar o programa.")
    elif nota == "fim":
        print("Programa finalizado!")
        break
    else:
        notas.append(float(nota))


print("Notas digitadas:", notas)
media = sum(notas) / len(notas)
print(f"A média das notas digitadas é: {media}")

if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")