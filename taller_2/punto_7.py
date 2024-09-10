# Calificaciones obtenidas en cada actividad
taller1 = float(input("Ingrese la nota del Taller 1 (1.0 a 5.0): "))
taller2 = float(input("Ingrese la nota del Taller 2 (1.0 a 5.0): "))
cuestionario1 = float(input("Ingrese la nota del Cuestionario 1 (1.0 a 5.0): "))
cuestionario2 = float(input("Ingrese la nota del Cuestionario 2 (1.0 a 5.0): "))
proyecto_final = float(input("Ingrese la nota del Proyecto Final (1.0 a 5.0): "))

# Pesos de cada actividad
peso_taller1 = 0.20
peso_taller2 = 0.15
peso_cuestionario1 = 0.22
peso_cuestionario2 = 0.10
peso_proyecto_final = 0.33

# Cálculo de la nota final
nota_final = (
    (taller1 * peso_taller1) +
    (taller2 * peso_taller2) +
    (cuestionario1 * peso_cuestionario1) +
    (cuestionario2 * peso_cuestionario2) +
    (proyecto_final * peso_proyecto_final)
)

# Mostrar el resultado
print(f"La nota final del curso es: {nota_final:.2f}")

