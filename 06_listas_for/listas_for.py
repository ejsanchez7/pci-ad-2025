import math

def promedio(lista):
    suma = 0

    for numero in lista :
        suma = suma + numero

    return suma / len(lista)

def promedio_indices(lista) :
    suma = 0
    tamanio = len(lista)

    for indice in range(tamanio) :
        suma = suma + lista[indice]
    
    return suma / tamanio

def menor(lista_numeros):
    min = lista_numeros[0]

    for indice in range(1, len(lista_numeros)):
        if lista_numeros[indice] < min :
            min = lista_numeros[indice]
    
    return min

def menor2(lista_numeros):
    min = lista_numeros[0]

    for numero in lista_numeros:
        if numero < min :
            min = numero
    
    return min

def varianza(lista_numeros):
    prom = promedio(lista_numeros)
    print("promedio: ", prom)
    suma = 0

    for numero in lista_numeros:
        diferencia = numero - prom
        suma = suma + diferencia
        print("diferencia", diferencia)
        print("suma", suma)
    
    return math.sqrt(suma / len(lista_numeros))

def pares_menores(max) :
    pares = []

    for numero in range(2, (max + 1), 2):
        pares.append(numero)
    
    return pares

numeros = [10, 30, 20, 5]
#prom = promedio(numeros)
# print(f"lista: {numeros}")
# print(f"El promedio es: {prom}")
# print(f"El menor es {menor(numeros)}")
# print(f"El menor2 es {menor(numeros)}")
#print(f"la varianza es {varianza([10, 20, 30, 5])}")

#max = int(input("Introduce un número: "))
#print(f"Los pares menores o iguales a {max} son: {pares_menores(max)}")

def decremento(inicio):

    for numero in range(inicio, -1, -1):
        print(numero)

decremento(5)