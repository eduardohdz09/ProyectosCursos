def imprimir_piramide_forma1(n = 10):
    """Imprime una piramide de tamaño n
    Parámetros:
    n - Tamaño de la piramide
    nota: si no se ingresa el valor de n toma 10 por default """
    i=1
    while i <= n:
        j = 1
        while j <= i:
            print("*", end="") # imprime * sin salto de línea
            j = j + 1
        i = i + 1
        print("\n")
