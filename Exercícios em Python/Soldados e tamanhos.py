n = int(input())
alturas = list(map(float, input().split()))

media = sum(alturas) / n

print(f"{media:.2f}")

saida = []
for altura in alturas:
    if altura < media:
        saida.append("P")
    elif altura > media:
        saida.append("G")
    else:
        saida.append("M")
        
print(" ".join(saida))