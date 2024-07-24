edad = int(input("Ingresar tu edad: "))
articulo = int(input("Ingresar cantidad de articulo: "))
if edad > 18:
    if articulo > 1:
        print(True)
    else:
        print(False)
else:
    print(False)