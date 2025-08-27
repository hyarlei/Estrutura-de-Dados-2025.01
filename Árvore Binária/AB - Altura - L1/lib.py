from typing import List

# Arvore binaria
class No:
    def __init__(self, chave, esq, dir):
        self.chave = chave
        self.esq = esq
        self.dir = dir

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None


# Retorna a altura da árvore binária
# Complexidade esperada: O(n)
def altura(arv: ArvoreBinaria) -> bool:
    pass # Implementar aqui