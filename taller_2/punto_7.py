# Función para calcular la nota final
def calcular_nota_final(taller1, taller2, cuestionario1, cuestionario2, proyecto_final):
    """
    Calcula la nota final basada en las notas de diferentes actividades y sus respectivos pesos.

    :param taller1: Nota del Taller 1
    :param taller2: Nota del Taller 2
    :param cuestionario1: Nota del Cuestionario 1
    :param cuestionario2: Nota del Cuestionario 2
    :param proyecto_final: Nota del Proyecto Final
    :return: Nota final del curso
    """
    # Pesos de cada actividad
    peso_taller1 = 0.20
    peso_taller2 = 0.15
    peso_cuestionario1 = 0.22
    peso_cuestionario2 = 0.10
    peso_proyecto_final = 0.36

    # Calcular la nota final
    nota_final = (taller1 * peso_taller1 +
                  taller2 * peso_taller2 +
                  cuestionario1 * peso_cuestionario1 +
                  cuestionario2 * peso_cuestionario2 +
                  proyecto_final * peso_proyecto_final)

    return nota_final


# Solicitar al usuario las notas de las actividades
taller1 = float(input("Introduce la nota del Taller 1 (1.0 a 5.0): "))
taller2 = float(input("Introduce la nota del Taller 2 (1.0 a 5.0): "))
cuestionario1 = float(input("Introduce la nota del Cuestionario 1 (1.0 a 5.0): "))
cuestionario2 = float(input("Introduce la nota del Cuestionario 2 (1.0 a 5.0): "))
proyecto_final = float(input("Introduce la nota del Proyecto Final (1.0 a 5.0): "))

# Validar que las notas están en el rango correcto
if any(nota < 1.0 or nota > 5.0 for nota in [taller1, taller2, cuestionario1, cuestionario2, proyecto_final]):
    print("Todas las notas deben estar en el rango de 1.0 a 5.0.")
else:
    # Calcular la nota final
    nota_final = calcular_nota_final(taller1, taller2, cuestionario1, cuestionario2, proyecto_final)

    # Mostrar el resultado
    print(f"La nota final en el curso es: {nota_final:.2f}")
