# Definir las actividades y sus pesos
actividades = {
    "Examen Final": 0.40,
    "Proyecto": 0.30,
    "Tarea 1": 0.20,
    "Participación": 0.10
}

# Definir las calificaciones obtenidas
calificaciones = {
    "Examen Final": 85,
    "Proyecto": 90,
    "Tarea 1": 80,
    "Participación": 95
}

# Calcular la nota definitiva
nota_definitiva = 0

for actividad, peso in actividades.items():
    calificacion = calificaciones.get(actividad, 0)
    nota_definitiva += calificacion * peso

# Imprimir la nota final redondeada a dos decimales usando f-string
print(f"La nota definitiva del curso es: {nota_definitiva:.2f}")


