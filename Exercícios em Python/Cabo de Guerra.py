t = int(input())
valores = []

for _ in range(t):
    valores.append(int(input()))
    
metade = t // 2
jedi= sum(valores[:metade])
sith = sum(valores[metade:])

if jedi > sith:
    print("Jedi")
elif sith > jedi:
    print("Sith")
else:
    print("Empate")