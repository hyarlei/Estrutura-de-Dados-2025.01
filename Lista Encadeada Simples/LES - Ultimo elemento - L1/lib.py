class No:
    def __init__(self, chave: int, proximo):
        self.chave = chave
        self.proximo = proximo

class ListaEncSimples:
    def __init__(self):
        self.cabeca = None

# Retorna o ultimo elmento da lista
# Retorna None se a lista estiver vazia
# Complexidade esperada: O(n)
def ultimo(lista: ListaEncSimples) -> No:
    # Implemente aqui