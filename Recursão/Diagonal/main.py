def imprimir_diagonal_recursivo(palavra, espacos):

    if not palavra:
        return
    
    print(" " * espacos + palavra[0])
    
    imprimir_diagonal_recursivo(palavra[1:], espacos + 1)

palavra_entrada = input()

imprimir_diagonal_recursivo(palavra_entrada, 0)