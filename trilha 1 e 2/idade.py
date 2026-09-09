print("Verificador de idade")

AnoNascimento = int(input("Digite o ano de seu Nascimento: "))

idade = 2026 - AnoNascimento

if idade >= 18:
    print("Você é maior de idade, sua idade é:", idade)
else: 
    print("Você é menor de idade, sua idade é:", idade)