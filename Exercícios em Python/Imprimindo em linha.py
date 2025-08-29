a, b = map(int, input().split())
numeros = [str(i) for i in range(a, b)]
print("[", " ".join(numeros), "]")