"""
Desarrolla el algoritmo y posteriormente el programa completo en Python que
solicite al usuario el valor asignado a los catetos de un triángulo
rectángulo, y que calcule el valor resultante de la hipotenusa. Para la
solución de este problema se sugiere que utilices el teorema de Pitágoras.
"""
import math

# 1.- Pedir al usuario el valor de los catetos
cateto_a = float(input("Ingrese el valor del cateto a: "))
cateto_b = float(input("Ingrese el valor del cateto b: "))


# 2.- Calcular el valor de la hipotenusa usando la fórmula y guardarla en una variable
suma_cuadrados = math.pow(cateto_a, 2) + math.pow(cateto_b, 2)
hipotenusa = math.sqrt(suma_cuadrados)
# hipotenusa = math.sqrt(math.pow(cateto_a, 2) + math.pow(cateto_b, 2))

# 3.- Mostrar el resultado
print(f"La hipotenusa del triángulo con catetos {cateto_a} y {cateto_b} es: {hipotenusa:.2f}")