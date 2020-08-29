def imprimir_piramide_forma2 (n = 10):
    """ Imprime una piramide de tamaño n
    Parámetros:
    n - Tamaño de la piramide
    nota: si no se ingresa el valor de n toma 10 por default """
    i = 1
    while i <= n:
        print("*" * i) #Concatena * n veces y lo imprime
        i = i + 1


imprimir_piramide_forma2()