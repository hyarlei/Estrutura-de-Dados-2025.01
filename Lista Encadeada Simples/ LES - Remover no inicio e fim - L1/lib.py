class No:
    def __init__(self, chave: int, proximo):
        self.chave = chave
        self.proximo = proximo

class ListaEncSimples:
    def __init__(self):
        self.cabeca = None

# Remove o primeiro elemento da lista
# Retorna True se a remoção for bem sucedida
# Retorna False se a lista estiver vazia
# Complexidade esperada: O(1)
def remover_inicio(lista: ListaEncSimples) -> bool:
    # Implemente aqui

# Remove o último elemento da lista
# Retorna True se a remoção for bem sucedida
# Retorna False caso contrário
# Complexidade esperada: O(n)
def remover_fim(lista: ListaEncSimples) -> bool:
    # Implemente aqui