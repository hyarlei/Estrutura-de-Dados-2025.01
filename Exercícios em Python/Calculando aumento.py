salario_atual = float(input())
if salario_atual <= 1000.00:
    novo_salario = salario_atual * 1.20
elif salario_atual <= 1500.00:
    novo_salario = salario_atual * 1.15
elif salario_atual <= 2000.00:
    novo_salario = salario_atual * 1.10
else:
    novo_salario = salario_atual * 1.05

print(f"{novo_salario:.2f}")