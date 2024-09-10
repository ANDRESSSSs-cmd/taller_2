# Función para convertir pesos colombianos a dólares
def convertir_pesos_a_dolares(pesos_colombianos, tasa_cambio):
    """
    Convierte una cantidad de pesos colombianos a dólares estadounidenses.

    :param pesos_colombianos: Cantidad en pesos colombianos
    :param tasa_cambio: Tasa de cambio (pesos colombianos por dólar)
    :return: Cantidad en dólares estadounidenses
    """
    dolares = pesos_colombianos / tasa_cambio
    return dolares


# Solicitar al usuario la cantidad de pesos colombianos
pesos_colombianos = float(input("Introduce la cantidad de pesos colombianos: "))

# Solicitar al usuario la tasa de cambio actual
tasa_cambio = float(input("Introduce la tasa de cambio (pesos por dólar): "))

# Verificar que la tasa de cambio no sea cero para evitar división por cero
if tasa_cambio == 0:
    print("La tasa de cambio no puede ser cero.")
else:
    # Calcular el monto en dólares
    dolares = convertir_pesos_a_dolares(pesos_colombianos, tasa_cambio)

    # Mostrar el resultado
    print(f"{pesos_colombianos:.2f} pesos colombianos son equivalentes a ${dolares:.2f} dólares.")
