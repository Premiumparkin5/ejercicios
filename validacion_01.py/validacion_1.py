"""validar el ingreso de un número entero del 1 al 10"""
while True:

    entrada = input("Digite un número entero del 1 al 10: ")
   
    # Validacion de los datos ingresados
    try:
        num = int(entrada)
        if 1 <= num <=10:
            print(f"el {num} es número valido")
            break
        else:
            print("El número ingresado no esta en el rango permitido.")
    except ValueError:
        print("El dato ingresado no es un número valido.")
        