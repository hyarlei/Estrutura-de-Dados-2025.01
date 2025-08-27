def calcular_pares_coelhos_fibonacci_modificado():

    linha_entrada = input().split()
    n = int(linha_entrada[0])
    k = int(linha_entrada[1])

    if n == 1:
        print(1)
        return
    if n == 2:
        print(1)
        return

    f_n_menos_2 = 1
    f_n_menos_1 = 1
    
    resultado_atual_f_n = 0
    
    for _ in range(3, n + 1):
        resultado_atual_f_n = f_n_menos_1 + (k * f_n_menos_2)
        
        f_n_menos_2 = f_n_menos_1
        f_n_menos_1 = resultado_atual_f_n
        
    print(resultado_atual_f_n)

calcular_pares_coelhos_fibonacci_modificado()