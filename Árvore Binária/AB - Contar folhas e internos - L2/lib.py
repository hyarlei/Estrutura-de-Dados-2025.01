from typing import List

class No:
    def __init__(self, chave, esq, dir):
        self.chave = chave
        self.esq = esq
        self.dir = dir

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

def _contar_folhas_rec(no: No) -> int:
    if no is None:
        return 0
    
    if no.esq is None and no.dir is None:
        return 1
    
    return _contar_folhas_rec(no.esq) + _contar_folhas_rec(no.dir)

def contar_folhas(arv: ArvoreBinaria) -> int:
    return _contar_folhas_rec(arv.raiz)

def _contar_internos_rec(no: No) -> int:
    if no is None or (no.esq is None and no.dir is None):
        return 0
    
    return 1 + _contar_internos_rec(no.esq) + _contar_internos_rec(no.dir)

def contar_internos(arv: ArvoreBinaria) -> int:
    return _contar_internos_rec(arv.raiz)