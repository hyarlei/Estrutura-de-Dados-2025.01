def calcular_dinheiro_inicial(num_igrejas, valor_doacao):
    dinheiro_atual = 0.0

    for _ in range(num_igrejas):
        dinheiro_antes_de_doar = dinheiro_atual + valor_doacao
        dinheiro_ao_entrar_nesta_igreja = dinheiro_antes_de_doar / 2.0
        dinheiro_atual = dinheiro_ao_entrar_nesta_igreja
    
    return dinheiro_atual

entrada = input().split()
N = int(entrada[0])
C = float(entrada[1])

dinheiro_inicial = calcular_dinheiro_inicial(N, C)

print(f"{dinheiro_inicial:.2f}")