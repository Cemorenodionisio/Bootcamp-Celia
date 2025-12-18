import os
import sys

def main():
    # Leer variables de entorno
    opcion = os.getenv("VAR_CHOICE", "Primera opción")
    nombre = os.getenv("NOMBRE", "Desconocido")

    print(f"Opción elegida desde Jenkins: {opcion}")

    # Leer archivo
    archivo = sys.argv[1] if len(sys.argv) > 1 else None
    if archivo:
        print(f"Leyendo archivo de entrada: {archivo}")
        with open(archivo, 'r') as f:
            contenido = f.read()
            print(contenido)

    if opcion == "Primera opción":
        print("Has elegido la Primera opción: Por tanto te diré mi nombre")
        print(f"Mi nombre es {nombre}")

    elif opcion == "Segunda opción":
        print("Has elegido la Segunda opción: Por tanto te diré mis estudios")
        print("Grado en Matemáticas y Máster en Análisis Avanzado de Datos Multivariantes y Big Data")

    else:
        print("Opción desconocida, no hacemos nada.")

if __name__ == "__main__":
    main()
