from typing import List

class No:
    def __init__(self, chave, esq, dir):
        self.chave = chave
        self.esq = esq
        self.dir = dir

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

def vazia(arv: ArvoreBinaria) -> bool:
    return arv.raiz is None

def _tamanho_rec(no: No) -> int:

    if no is None:
        return 0
    return 1 + _tamanho_rec(no.esq) + _tamanho_rec(no.dir)

def tamanho(arv: ArvoreBinaria) -> int:
    return _tamanho_rec(arv.raiz)