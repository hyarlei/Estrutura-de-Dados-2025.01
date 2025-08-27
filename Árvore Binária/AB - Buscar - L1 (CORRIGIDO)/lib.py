from typing import List

class No:
    def __init__(self, chave, esq, dir):
        self.chave = chave
        self.esq = esq
        self.dir = dir

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

def _altura_rec(no: No) -> int:
    if no is None:
        return 0
    
    altura_esq = _altura_rec(no.esq)
    altura_dir = _altura_rec(no.dir)
    
    return 1 + max(altura_esq, altura_dir)

def altura(arv: ArvoreBinaria) -> int:
    return _altura_rec(arv.raiz)