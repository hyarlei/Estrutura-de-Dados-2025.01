n = int(input())
valores = list(map(int, input().split()))

if len(set(valores)) == n:
        print("Todos diferentes")
else:
    print ("Algum elemento repete")