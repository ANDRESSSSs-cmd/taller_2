# Función para calcular el nuevo salario mínimo
def calcular_nuevo_salario(salario_actual, porcentaje_incremento):
    # Calcular el incremento
    incremento = salario_actual * (porcentaje_incremento / 100)
    # Calcular el nuevo salario
    nuevo_salario = salario_actual + incremento
    return nuevo_salario

# Solicitar al usuario el salario mínimo actual
salario_actual = float(input("Introduce el salario mínimo actual: "))

# Definir el porcentaje de incremento
porcentaje_incremento = 4.2

# Calcular el nuevo salario mínimo
nuevo_salario = calcular_nuevo_salario(salario_actual, porcentaje_incremento)

# Mostrar el resultado
print(f"El nuevo salario mínimo para el siguiente año es: ${nuevo_salario:.2f}")
