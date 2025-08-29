TAMANHO_CONJ = 100

class Conjunto:
    def __init__(self):
        self.dados = [None] * TAMANHO_CONJ
        self.tamanho = 0

def pertence(conj, elem):
    # Complexidade: O(n)
    for i in range(conj.tamanho):
        if conj.dados[i] == elem:
            return True
    return False

def inserir(conj, elem):
    # Complexidade: O(n)
    if not pertence(conj, elem) and conj.tamanho < TAMANHO_CONJ:
        conj.dados[conj.tamanho] = elem
        conj.tamanho += 1

def remover(conj, elem):
    # Complexidade: O(n)
    for i in range(conj.tamanho):
        if conj.dados[i] == elem:
            for j in range(i, conj.tamanho - 1):
                conj.dados[j] = conj.dados[j + 1]
            conj.tamanho -= 1
            break

def imprimir(conj):
    # Complexidade: O(n)
    elementos = [conj.dados[i] for i in range(conj.tamanho)]
    print(f"Conjunto com elementos {set(elementos)}")

def uniao(conj1, conj2):
    novo = Conjunto()
    for i in range(conj1.tamanho):
        inserir(novo, conj1.dados[i])
    for i in range(conj2.tamanho):
        inserir(novo, conj2.dados[i])
    return novo

def intersecao(conj1, conj2):
    novo = Conjunto()
    for i in range(conj1.tamanho):
        if pertence(conj2, conj1.dados[i]):
            inserir(novo, conj1.dados[i])
    return novo

def diferenca(conj1, conj2):
    novo = Conjunto()
    for i in range(conj1.tamanho):
        if not pertence(conj2, conj1.dados[i]):
            inserir(novo, conj1.dados[i])
    return novo

A = Conjunto()
inserir(A, 1)
inserir(A, 2)
inserir(A, 3)
print("Conjunto A:")
imprimir(A)

B = Conjunto()
inserir(B, 2)
inserir(B, 4)
print("Conjunto B:")
imprimir(B)

print("União:"); imprimir(uniao(A, B))         # {1, 2, 3, 4}
print("Interseção:"); imprimir(intersecao(A, B))  # {2}
print("Diferença:"); imprimir(diferenca(A, B))    # {1, 3}