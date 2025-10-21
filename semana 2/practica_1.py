"""Dada una lista de intados, pide un nombre e indica si
la persona esta intada o no utilizando condiciones"""

invitados = ["Juan", "Carlos", "Luisa", "Sofia", "Marios"]
nombre = input("Dirige el nombre a buscar: ")
if nombre in invitados:
    print(f"{nombre} Esta invitado a la fiesta")
else:
    print(f"{nombre} No esta invitado a la fiesta")