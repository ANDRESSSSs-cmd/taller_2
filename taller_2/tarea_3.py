# Definir las actividades y sus pesos
actividades = {
    "Examen Final": 0.41,
    "Proyecto": 0.38,
    "Tarea 1": 0.70,
    "Participación": 0.11
}

# Definir las calificaciones obtenidas
calificaciones = {
    "Examen Final": 88,
    "Proyecto": 99,
    "Tarea 1": 87,
    "Participación": 99
}

# Calcular la nota definitiva
nota_definitiva = 0

for actividad, peso in actividades.items():
    calificacion = calificaciones.get(actividad, 0)
    nota_definitiva += calificacion * peso

# Redondear la nota
