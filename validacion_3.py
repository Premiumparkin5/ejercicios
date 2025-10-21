"""Formulario que solicite nombre, edad y correo"""

import re

def validar_nombre(nombre):
    
    # Verificiar la variable nombre no esta vacia
    return nombre.replace(" ", "").isalpha()

# Funcion que valida la edad entre 14 y 100 años.
def validar_edad(edad_val):
    try:
        edad = int(edad_val)
        return 14 <= edad <= 100
    except ValueError:
        return False
    
def validar_correo(correo):
    patron = r"^[\w\.-]+@[\w\.-]+\w+$"
    return re.match(patron, correo) is not None


while True:

    nombre = input("Ingrese su nombre: ").strip()
    if not validar_nombre(nombre):
        print("Nombre invalido. ingrese su nombre correctamente.")
        continue

    edad = input("ingrese su edad: ").strip()
    if not validar_edad(edad):
        print("Edad invalida.Ingrese un valor entre 14 y 100.")
        continue

    correo = input("Ingrese su correo electronico: ").strip()
    if not validar_correo(correo):
        print("Correo invalido. Ingrese su correo valido.")
        
        
        
    print(f"Registro exitoso: Nombre: {nombre}, Edad: {edad}, Correo: {correo}")
    break