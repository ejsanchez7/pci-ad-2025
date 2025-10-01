def promedio(lista_numeros):
    indice = 0
    tamanio = len(lista_numeros)
    suma = 0

    while indice < tamanio :
        suma = suma + lista_numeros[indice]
        indice += 1

    return (suma / tamanio)


cantidad_numeros = int(input("Introduce la cantidad de números a promediar: "))
contador = 0
numeros = []

while contador < cantidad_numeros :
    numero = float(input(f"Escribe el número {contador + 1}: "))
    numeros.append(numero)
    contador += 1

prom = promedio(numeros)
print(f"El promedio de {numeros} es: {prom}")