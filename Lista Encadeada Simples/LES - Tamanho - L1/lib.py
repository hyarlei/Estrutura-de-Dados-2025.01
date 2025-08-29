class No:
    def __init__(self, chave: int, proximo):
        self.chave = chave
        self.proximo = proximo

class ListaEncSimples:
    def __init__(self):
        self.cabeca = None

# Retorna o tamanho da lista
# Complexidade esperada: O(n)
def tamanho(lista: ListaEncSimples) -> int:
    # Implemente aqui