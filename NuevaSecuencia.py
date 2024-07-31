# Escriba un programa que le solicite al usuario
# un numero entero y muestre todos los numeros
# ingresado por el usuario

numero = int(input("ingrese un numero: "))
num = range(1,numero + 1)
num2 = " ", num[:-1]
for indice in num:
    num2+= indice+ " "
print(num2)
