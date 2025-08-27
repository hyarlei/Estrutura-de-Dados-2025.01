from typing import List

class No:
    def __init__(self, elemento: int, proximo):
        self.elemento = elemento
        self.proximo = proximo

class Pilha:
    def __init__(self):
        self.cabeca = None


# Retorna o elemento no topo da pilha
# Se a pilha estiver vazia, retorna None
# Complexidade esperada: O(1)
def acessar(pilha: Pilha):
    if pilha.cabeca is None:
        return None
    return pilha.cabeca.elemento


# Retorna se a pilha está vazia
# Complexidade esperada: O(1)
def vazia(pilha: Pilha) -> bool:
    return pilha.cabeca is None


# Insere o elemento no topo da pilha
# Retorna True se o elemento foi inserido, False caso contrário
# Complexidade esperada: O(1)
def inserir(pilha: Pilha, elemento) -> bool:
    novo_no = No(elemento, pilha.cabeca)
    pilha.cabeca = novo_no
    return True