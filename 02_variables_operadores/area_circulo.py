# Un algoritmo que calcule el área de un círculo.
import math

# 1.- Pedir al usuario el valor del radio
radio = float(input("Ingrese el valor del radio: "))
# 2.- Calcular el área usando la fórmula y guardarla en una variable
# Operador de exponente en python: **
area = math.pi * (radio ** 2)
# area = math.pi * math.pow(radio, 2)
# 3.- Mostrar el resultado
# {area:.2f} = el valor de área con precisión de dos decimales
print(f"El área del círculo con radio {radio} es: {area:.2f}")