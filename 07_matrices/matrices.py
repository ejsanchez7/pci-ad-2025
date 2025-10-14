def imprime_matriz(matriz):
    for lista in matriz:
        for elemento in lista:
            print(elemento, end=" ")
        print("")

def imprime_matriz2(matriz):
    renglones = len(matriz)
    columnas = len(matriz[0])

    for indice_renglon in range(renglones):
        renglon = matriz[indice_renglon]
        for indice_columna in range(len(renglon)):
            print(matriz[indice_renglon][indice_columna], end = ", ")
        print("")


matriz = [
    [1, 2, 3], #0
    [4, 5, 6, 19], #1
    [7, 8, 9], #2
]

imprime_matriz(matriz)
print("********************")
imprime_matriz2(matriz)

# matriz[0] # [1, 2, 3]
# matriz[1] # [3, 4, 5]
# matriz[2] # [7, 8, 9]

# matriz[0][0] #1