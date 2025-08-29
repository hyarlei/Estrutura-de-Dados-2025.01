class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Conjunto:
    def __init__(self):
        self.inicio = None

def pertence(conj, elem):
    # Complexidade: O(n)
    atual = conj.inicio
    while atual is not None:
        if atual.valor == elem:
            return True
        atual = atual.proximo
    return False

def inserir(conj, elem):
    # Complexidade: O(n)
    if not pertence(conj, elem):
        novo = No(elem)
        novo.proximo = conj.inicio
        conj.inicio = novo

def remover(conj, elem):
    # Complexidade: O(n)
    atual = conj.inicio
    anterior = None
    while atual is not None:
        if atual.valor == elem:
            if anterior is None:
                conj.inicio = atual.proximo
            else:
                anterior.proximo = atual.proximo
            return
        anterior = atual
        atual = atual.proximo

def imprimir(conj):
    # Complexidade: O(n)
    elementos = []
    atual = conj.inicio
    while atual is not None:
        elementos.append(atual.valor)
        atual = atual.proximo
    print(f"Conjunto com elementos {set(elementos)}")
    
def uniao(conj1, conj2):
    # Complexidade: O(n^2) no pior caso
    novo = Conjunto()
    atual = conj1.inicio
    while atual is not None:
        inserir(novo, atual.valor)
        atual = atual.proximo
    atual = conj2.inicio
    while atual is not None:
        inserir(novo, atual.valor)
        atual = atual.proximo
    return novo

def intersecao(conj1, conj2):
    # Complexidade: O(n^2)
    novo = Conjunto()
    atual = conj1.inicio
    while atual is not None:
        if pertence(conj2, atual.valor):
            inserir(novo, atual.valor)
        atual = atual.proximo
    return novo

def diferenca(conj1, conj2):
    # Complexidade: O(n^2)
    novo = Conjunto()
    atual = conj1.inicio
    while atual is not None:
        if not pertence(conj2, atual.valor):
            inserir(novo, atual.valor)
        atual = atual.proximo
    return novo
    
A = Conjunto()
inserir(A, 1)
inserir(A, 2)
inserir(A, 3)
print("Conjunto A:")
imprimir(A)  # Conjunto com elementos {1, 2, 3}

B = Conjunto()
inserir(B, 2)
inserir(B, 4)
print("Conjunto B:")
imprimir(B)  # Conjunto com elementos {2, 4}

print("União:"); imprimir(uniao(A, B))  # Conjunto com elementos {1, 2, 3, 4}
print("Interseção:"); imprimir(intersecao(A, B))  # Conjunto com elementos {2}
print("Diferença:"); imprimir(diferenca(A, B))  # Conjunto com elementos {1, 3}