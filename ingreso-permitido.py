#Paso 1: Solicitar al usuario que ingrese la edad del cliente.

from operator import truediv


edad = int(input("Por favor, ingrese la edad del cliente."))
#Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca.
permitido = True if edad >= 18 else False

#Paso 3: Mostrar al usuario si el usuario puede o no entrar a la discoteca. 
if permitido:
    print("El cliente puede ingresar a la discoteca.")
else:
    print("El cliente no puede ingresar a la discoteca siendo menor de edad")