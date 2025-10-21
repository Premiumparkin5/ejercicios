"""Escribe un programa que permita al usuario ingresar tareas 
por hacer, hasta que escriba "salir". Al final, imprime la 
lista de tarea"""

tareas = []
while True:
    tarea = input("Ingrese una tarea (Digite 'salir' para terminar): ")
    if tarea.lower() == "salir":
        break
    tareas.append(tarea)
    print("Tarea guardada: ", tareas)
