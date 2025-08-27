def calcular_e_mostrar_quadrado_recursivo(n_atual):
    
    if n_atual == 1:
        print("1^2 = 1")
        return 1
    
    print(f"{n_atual}^2 = {n_atual-1}^2 + 2*{n_atual-1} + 1 = ?")
    
    valor_quadrado_anterior = calcular_e_mostrar_quadrado_recursivo(n_atual - 1)
    
    resultado_atual = valor_quadrado_anterior + 2 * (n_atual - 1) + 1
    
    print(f"{n_atual}^2 = {n_atual-1}^2 + 2*{n_atual-1} + 1 = {resultado_atual}")
    
    return resultado_atual

n_input = int(input())

if n_input >= 1:
    calcular_e_mostrar_quadrado_recursivo(n_input)
else:
    
    if n_input == 0:
        print("0^2 = 0")