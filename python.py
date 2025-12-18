import os

def main():
    # Leer variables de entorno de Jenkins
    opcion = os.getenv("VAR_CHOICE", "Primera opción")
    nombre = os.getenv("NOMBRE", "Desconocido")

    print(f"Opción elegida desde Jenkins: {opcion}")

    if opcion == "Primera opción":
        print("Has elegido la Primera opción: Por tanto te diré mi nombre")
        print(f"Mi nombre es {nombre}")

    elif opcion == "Segunda opción":
        print("Has elegido la Segunda opción: Por tanto te diré mis estudios")
        print("Grado en Matemáticas y Máster en Análisis Avanzado de Datos Multivariantes y Big Data")

    elif opcion == "Tercera opción":
        print("Has elegido la Tercera opción: Por tanto vamos a contar números pares y adivinar mi edad")
        
        # Contar números pares antes de la edad 23
        pares = 0
        for i in range(23):  
            if i % 2 == 0:    
                pares += 1
        print(f"Números pares antes de mi edad: {pares}")

        # Preguntar al usuario su edad
        edad = int(input("Introduce un número: "))
        if edad != 23:
            print("No es la edad correcta. Saliendo...")
            exit()
        else:
            print("¡Correcto! Has adivinado mi edad.")

    else:
        print("Opción desconocida, no hacemos nada.")

if __name__ == "__main__":
    main()
