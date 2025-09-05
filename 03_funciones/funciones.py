# Elevar un numero al cuadrado
# Paso 1.- Definir la función
def cuadrado():
    numero = float(input("Escribe un número: "))
    resultado = numero ** 2
    print(f"El resultado es: {resultado}")

def cuadrado_mejorado(numero):
    resultado = numero ** 2
    print(f"El resultado es: {resultado}")

# Paso 2.- Invocar la función (usar la función)
#cuadrado() # 25
#cuadrado_mejorado(10) # 100
#num = 8
#num_usuario = float(input("Escribe un número: "))
#cuadrado_mejorado(num) # 64
#cuadrado_mejorado(num_usuario)

# La función millas_kilometros que convierta la cantidad dada en millas a kilómetros.
def millas_kilometros(millas):
    kilometros = millas * 1.60934
    print(f"{millas} millas son {kilometros} kilómetros.")

def millas_kilometros_mejorado(millas):
    kilometros = millas * 1.60934
    return kilometros

# cantidad = float(input("Escribe la cantidad en millas: "))
# millas_kilometros(cantidad)

# resultado = millas_kilometros_mejorado(cantidad)
# distancia_final = 80 + resultado
# print(distancia_final)

# La función libras_kilos que convierta la cantidad dada en libras a kilos.
def libras_kilos(libras):
    kilos = libras * 0.453592
    return kilos
    print("Esta línea nunca se ejecuta")

# kilos = libras_kilos(150)
# print(f"150 libras son {kilos} kilos.")

def going_to_mexico(millas, libras):
    kilometros = millas_kilometros_mejorado(millas)
    kilos = libras_kilos(libras)
    print(f"{millas} millas son {kilometros:.2f} kilómetros.")
    print(f"{libras} libras son {kilos:.2f} kilos.")

mi = float(input("Escribe la cantidad en millas: "))
going_to_mexico(mi, 10)

print("Fin")