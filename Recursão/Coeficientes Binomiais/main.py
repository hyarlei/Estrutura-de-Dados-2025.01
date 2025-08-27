def calcular_c(n, k):
    
    if k < 0 or k > n:
        return 0
    
    if k == 0 or k == n:
        return 1
    
    return calcular_c(n - 1, k - 1) + calcular_c(n - 1, k)

entrada = input().split()
n_val = int(entrada[0])
k_val = int(entrada[1])

resultado = calcular_c(n_val, k_val)
print(resultado)