"""Validar el ingreso de categoria: a, b o c"""

while True:
    categoria = input("Ingrese una categoria (a, b o c): ").lower()
    if categoria in ("a", "b", "c"):
        print(f"Ha selecionado la categoria: {categoria} ")
        break
    else:
        print("la categoria ingresada no es valida . intente de nuevo: ")