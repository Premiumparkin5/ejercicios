# Funciones
def saludo():
    print("Hola Fulano")

saludo()

# Funcion con Parametro
def saludo_personal(nombre):
    print(f"Hola, {nombre}")

# nombre_usuario = input("¿Cual es tu nombre?")

saludo_personal("Samuel")

# Funcion con Valores de Retorno
def suma(num1, num2):
    resultado = num1 + num2
    return resultado

total = suma(5, 2 )
print(f"La suma es: {total}")

# Funcion con parametros por defectos
def perfil(nombre, edad, ciudad="Medellín"):
           return{
                 "nombre":nombre,
                 "edad":edad,
                 "ciudad":ciudad
           }

perfil1 = perfil("Samuel", 17)
perfil2 = perfil("Juan", 23, "Cali")
print(perfil1)
print(perfil2)