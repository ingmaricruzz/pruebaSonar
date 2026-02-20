import random
import string

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def generar_contrasena_v2(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

if __name__ == "__main__":
    longitud = int(input("Ingresa la longitud de la contraseña: "))
    print("Contraseña generada:", generar_contrasena(longitud))
