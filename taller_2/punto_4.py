# Función para convertir metros a millas
def metros_a_millas(metros):
    # Definir la constante de conversión
    METROS_POR_MILLA = 1609.34
    # Convertir metros a millas
    millas = metros / METROS_POR_MILLA
    return millas

# Solicitar al usuario la cantidad de metros
metros = float(input("Introduce la cantidad de metros: "))

# Realizar la conversión
millas = metros_a_millas(metros)

# Mostrar el resultado
print(f"{metros} metros son equivalentes a {millas:.6f} millas.")
