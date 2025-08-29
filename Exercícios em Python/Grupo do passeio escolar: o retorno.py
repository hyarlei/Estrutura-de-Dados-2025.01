n = int(input())
idades = list(map(int, input().split()))

nao_adultos = sum(1 for idade in idades if idade < 18)

print(nao_adultos)