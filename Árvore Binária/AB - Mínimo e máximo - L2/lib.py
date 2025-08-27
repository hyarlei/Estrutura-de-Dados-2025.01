from typing import List

class No:
    def __init__(self, chave, esq, dir):
        self.chave = chave
        self.esq = esq
        self.dir = dir

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

def _minimo_rec(no: No) -> int:
    if no is None:
        return float('inf')
    
    min_esq = _minimo_rec(no.esq)
    min_dir = _minimo_rec(no.dir)
    
    return min(no.chave, min_esq, min_dir)

def minimo(arv: ArvoreBinaria) -> int:
    if arv.raiz is None:
        return None
    
    return _minimo_rec(arv.raiz)

def _maximo_rec(no: No) -> int:
    if no is None:
        return float('-inf')

    max_esq = _maximo_rec(no.esq)
    max_dir = _maximo_rec(no.dir)
    
    return max(no.chave, max_esq, max_dir)

def maximo(arv: ArvoreBinaria) -> int:
    if arv.raiz is None:
        return None
        
    return _maximo_rec(arv.raiz)