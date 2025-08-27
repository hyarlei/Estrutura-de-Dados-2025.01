def esta_balanceado(sequencia: str) -> str:
    pilha = []
    pares = {')': '(', ']': '['}

    for char in sequencia:
        if char in '([':
            pilha.append(char)
        elif char in ')]':
            if not pilha or pilha[-1] != pares[char]:
                return "nao balanceado"
            pilha.pop()

    return "balanceado" if not pilha else "nao balanceado"


if __name__ == "__main__":
    try:
        entrada = input().strip()
        print(esta_balanceado(entrada).strip())
    except:
        print("nao balanceado")