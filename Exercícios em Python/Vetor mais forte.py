n1 = int(input())
v1 = list(map(int, input().split()))

n2 = int(input())
v2 = list(map(int, input().split()))

soma_v1 = sum(v1)
soma_v2 = sum(v2)

if soma_v1 > soma_v2:
    print("Vetor 1 ganha")
elif soma_v1 < soma_v2:
    print("Vetor 2 ganha")
else:
    print("Empate")