def imprimir_sufixos_recursivo(palavra):
    
    if not palavra:
        return
    
    imprimir_sufixos_recursivo(palavra[1:])
    
    print(palavra)

palavra_entrada = input()

imprimir_sufixos_recursivo(palavra_entrada)