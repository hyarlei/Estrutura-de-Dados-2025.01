from collections import Counter

n = int(input())
valores = list(map(int, input().split()))

contagem = Counter(valores)

unicos = sum(1 for v in contagem.values() if v == 1)

print(unicos)