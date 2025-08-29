a = int(input())
b = int(input())

if a > b:
    print("invalido")
else:
    soma = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            soma += i
    print(soma)