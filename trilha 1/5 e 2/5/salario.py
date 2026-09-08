print("-" * 10, "Bônus de Salario PPR Viana e Moura", "-" * 10)
salario = int(input("Digite o salário: "))

if salario < 1500:
   novoSalario = salario * 1.10
   print("Seu antigo salário era:", salario)
   print("valor do aumento de 10% é:", novoSalario - salario)
   print("O novo salário com aumento de 10% é:", novoSalario)

elif salario >= 1500:
    novoSalario = salario * 1.05 
    print("Seu antigo salário era:", salario)
    print("valor do aumento de 5% é:", novoSalario - salario)
    print("O novo salário com aumento de 5% é:", novoSalario)