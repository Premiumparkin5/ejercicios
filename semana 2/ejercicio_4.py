# Creación de Diccionarios
estudiante = {
    "nombre": "Samuel",
    "edad": 17,
    "profesion": "Aprendiz/Estudiante",
    "competencia": ["Programación","Base de Datos","Algoritmos"]
}

# Mostrar  Información
print(estudiante["nombre"])
print(estudiante["profesion"])
print(estudiante["competencia"][0])

# Modificar Información
estudiante["celular"] = 3234805002
estudiante["edad"] = 17

# Recorrer Diccionario
for clave, valor in estudiante. items():
    print(f"{clave}: {valor}")