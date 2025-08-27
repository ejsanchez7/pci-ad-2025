"""
Desarrolla el algoritmo y posteriormente un programa completo en Python que
determine el volumen de la siguiente figura geométrica (imagine que es un
medio cilindro). El radio (r) y la altura (h) son solicitadas al usuario.
"""

# 0.- Definir la constante pi
PI = 3.141592

# 1.- Pedir al usuario el valor del radio y la altura
radio = float(input("Ingrese el valor del radio: "))
altura = float(input("Ingrese el valor de la altura: "))

# 2.- Calcular el volumen del cilindro usando la fórmula y guardarla en una variable
volumen = PI * (radio ** 2) * altura

# 3.- Dividir el volumen entre 2 para obtener el volumen del medio cilindro
resultado = volumen / 2

# 4.- Mostrar el resultado
print(f"El volumen del medio cilindro con radio {radio} y altura {altura} es: {resultado:.2f}")