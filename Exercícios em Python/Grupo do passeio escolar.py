n = int(input())
idades = list(map(int, input().split()))

apto = False
for idade in idades:
    if idade >= 18:
        apto = True
        break
    
if apto:
    print("Apto")
else:
    print("Inapto")