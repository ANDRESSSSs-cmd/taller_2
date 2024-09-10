def leer_notas():
    """
    Solicita al usuario que introduzca las cinco notas correspondientes a cada actividad.

    :return: Un diccionario con las notas de cada actividad.
    """
    try:
        # Solicitar al usuario las notas de las actividades
        notas = {
            'Taller 1': float(input("Introduce la nota del Taller 1 (1.0 a 5.0): ")),
            'Taller 2': float(input("Introduce la nota del Taller 2 (1.0 a 5.0): ")),
            'Cuestionario 1': float(input("Introduce la nota del Cuestionario 1 (1.0 a 5.0): ")),
            'Cuestionario 2': float(input("Introduce la nota del Cuestionario 2 (1.0 a 5.0): ")),
            'Proyecto Final': float(input("Introduce la nota del Proyecto Final (1.0 a 5.0): "))
        }

        # Validar que las notas están en el rango correcto
        for actividad, nota in notas.items():
            if nota < 1.0 or nota > 5.0:
                raise ValueError(f"La nota para {actividad} debe estar entre 1.0 y 5.0.")

        return notas

    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    # Leer las notas
    notas = leer_notas()

    if notas:
        # Mostrar las notas ingresadas
        print("\nNotas ingresadas:")
        for actividad, nota in notas.items():
            print(f"{actividad}: {nota:.2f}")


# Ejecutar el programa
if __name__ == "__main__":
    main()
