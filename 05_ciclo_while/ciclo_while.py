# factorial de un número
def factorial(numero):
    contador = 2
    resultado = 1

    while contador <= numero :
        resultado = resultado * contador
        contador = contador + 1
    
    return resultado

# num = int(input("Escribe un número: "))
# print(f"{num}! = {factorial(num)}")

def cociente_residuo(numerador, denominador):
    residuo = numerador
    cociente = 0

    while residuo >= denominador:
        residuo = residuo - denominador
        cociente = cociente + 1
    
    print(f"{numerador} / {denominador} = {cociente}\n{numerador} % {denominador} = {residuo}")

#cociente_residuo(8, 3)
#cociente_residuo(9, 2)

def pares_anteriores(numero):
    par = 2
    contador = 1

    while par <= numero:
        print(f"par {contador} = {par}")
        par = par + 2
        contador = contador + 1

pares_anteriores(13) # 2, 4, 6, 8, 10, 12