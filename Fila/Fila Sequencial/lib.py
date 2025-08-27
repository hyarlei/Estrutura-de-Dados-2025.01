from typing import List

class Fila:
    def __init__(self):
        self.capacidade = 8
        self.inicio = 0
        self.tamanho = 0
        self.elementos = [None] * self.capacidade


# Retorna o elemento no início da fila
# Se a fila estiver vazia, retorna None
# Complexidade esperada: O(1)
def acessar(fila: Fila):
    if fila.tamanho == 0:
	    return None
    return fila.elementos[fila.inicio]


# Retorna se a fila está vazia
# Complexidade esperada: O(1)
def vazia(fila: Fila) -> bool:
    return fila.tamanho == 0


# Insere o elemento no topo da fila
# Retorna True se o elemento foi inserido, False caso contrário
# Complexidade esperada: O(1)
def inserir(fila: Fila, elemento) -> bool:
    if fila.tamanho == fila.capacidade:
	    return False
    pos_ins = (fila.inicio + fila.tamanho) % fila.capacidade
    fila.elementos[pos_ins] = elemento
    fila.tamanho += 1
    return True


# Remove o elemento do topo da fila
# Retorna True se o elemento foi removido, False caso contrário
# Complexidade esperada: O(1)
def remover(fila: Fila) -> bool:
    if fila.tamanho == 0:
        return False
    fila.inicio = (fila.inicio + 1) % fila.capacidade
    fila.tamanho -= 1
    return True


# Exibe os elementos da fila
# Complexidade: O(n)
def imprimir(fila: Fila) -> None:
    print("Inicio: ", end="")
    for i in range(fila.tamanho):
        pos = (fila.inicio + i) % fila.capacidade
        if i == fila.tamanho - 1:
            print(fila.elementos[pos], end="")
        else:
            print(fila.elementos[pos], end=", ")
    print(" final")