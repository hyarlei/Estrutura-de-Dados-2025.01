class No:
    def __init__(self, chave: int, proximo):
        self.chave = chave
        self.proximo = proximo

class ListaEncSimples:
    def __init__(self):
        self.cabeca = None

# Compara duas listas encadeadas simples
# As listas são equivalentes se tiverem o mesmo número de elementos
# e os mesmos elementos na mesma ordem
# Retorna True se as listas forem equivalentes
# Retorna False se as listas não forem equivalentes
# Complexidade esperada: O(n + m) ou O(min(n, m))
def equivalentes(lista1: ListaEncSimples, lista2: ListaEncSimples) -> bool: