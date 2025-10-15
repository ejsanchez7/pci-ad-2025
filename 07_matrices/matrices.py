def imprime_matriz(matriz):
    for lista in matriz:
        for elemento in lista:
            print(elemento, end=" ")
        print("")

def imprime_matriz2(matriz):
    renglones = len(matriz)

    for indice_renglon in range(renglones):
        renglon = matriz[indice_renglon]
        for indice_columna in range(len(renglon)):
            print(matriz[indice_renglon][indice_columna], end = ", ")
        print("")

def obtener_columna(matriz, indice):
    renglones = len(matriz)
    columna = []

    for indice_renglon in range(renglones):
        renglon = matriz[indice_renglon]
        for indice_columna in range(len(renglon)):
            if indice_columna == indice:
                columna.append(renglon[indice_columna])
                break
    return columna

def crea_matriz(num_renglones, num_columnas, valor):
    matriz = []

    for n_ren in range(num_renglones):
        renglon = []
        for n_col in range(num_columnas):
            renglon.append(valor)
        matriz.append(renglon)
    
    return matriz

def crea_matriz2(num_renglones, num_columnas, valor):
    matriz = []

    for n_ren in range(num_renglones):
        renglon = [valor] * num_columnas
        matriz.append(renglon)
    
    return matriz

# matriz = crea_matriz(2, 3, "hola")
# print(matriz)
# print(crea_matriz2(2, 2, "hello"))

# [
#     ["hola", "hola", "hola"],
#     ["hola", "hola", "hola"],
# ]

def suma_matrices(matriz_a, matriz_b):
    if (len(matriz_a) == len(matriz_b)) and (len(matriz_a[0]) == len(matriz_b[0])):
        resultado = []

        for n_ren in range(len(matriz_a)):
            renglon = []
            
            for n_col in range(len(matriz_a[n_ren])):
                suma = matriz_a[n_ren][n_col] + matriz_b[n_ren][n_col]
                renglon.append(suma)
            
            resultado.append(renglon)

        return resultado
    
    print("No se pueden sumar las matrices")
            
def transponer_matriz(matriz):
    return []

def clonar_matriz(matriz):
    return []

digitos = [
    #0  1  2
    [1, 2, 3], #0
    [4, 5, 6], #1
    [7, 8, 9], #2
]

imprime_matriz(suma_matrices(digitos, digitos))



# columna = obtener_columna(digitos, 1) # [2, 5, 8]
# print(columna)
# imprime_matriz(matriz)
# print("********************")
# imprime_matriz2(matriz)

# matriz[0] # [1, 2, 3]
# matriz[1] # [3, 4, 5]
# matriz[2] # [7, 8, 9]

# matriz[0][0] #1
