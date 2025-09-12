def calcular_mayor(num_a, num_b):
    if num_a > num_b:
        return num_a
    else:
        return num_b

def calcular_mayor2(num_a, num_b):
    if num_a > num_b:
        return num_a
    return num_b

# print(calcular_mayor2(10, 5)) # 10
# print(calcular_mayor2(5, 5)) # 5
# print(calcular_mayor2(1, 15)) # 15

def calcular_corriente(voltaje, resistencia):
    corriente = 0
    if resistencia > 0:
        corriente = voltaje / resistencia
    return corriente

def comprobar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def comprobar_triangulo2(a, b, c):
    return ( a + b > c and a + c > b and b + c > a )
        
def tipo_triangulo(a, b, c):
    if comprobar_triangulo2(a, b, c):
        if a == b == c:
            print('Su triangulo es equilatero')
        elif a == b or b == c:
            print('Su triangulo es isoceles')
        else:
            print('Su triangulo es escaleno')
    else:
        print('Sus valores no son acordes a un triangulo')

# lado_a = float(input('Digite el valor de su lado A: '))
# lado_b = float(input('Digite el valor de su lado B: '))
# lado_c = float(input('Digite el valor de su lado C: '))

# tipo_triangulo(lado_a, lado_b, lado_c)

def promedio(a, b):
    return (a + b) / 2

def valida_calificacion(a, b):
    return ((a >= 0) and (a <= 100) and (b >= 0) and (b <= 100))

def aprueba(calificacion_1, calificacion_2):
    if valida_calificacion(calificacion_1, calificacion_2):
        return promedio(calificacion_1, calificacion_2) >= 70
    # print("Las calificaciones no son válidas")
    # return False
    else:
        print("Las calificaciones no son válidas")
        return False

# cal1 = int(input("Escribe la calificación del primer parcial: "))
# cal2 = int(input("Escribe la calificación del segundo parcial: "))

# if aprueba(cal1, cal2):
#     print("Aprobaste!")
# else:
#     print("No aprobaste!")

def tipo_numero(num):
    tipo = ""
    if num > 0 :
        tipo = "positivo"
    elif num < 0 :
        tipo = "negativo"
    else:
        tipo = "cero"
    print(f"{num} es {tipo}")

tipo_numero(-10)
tipo_numero(0)
tipo_numero(200)