import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        try:
            suposicion = int(input("Introduce tu suposición: "))
            intentos += 1

            if suposicion < numero_secreto:
                print("El número es más alto.")
            elif suposicion > numero_secreto:
                print("El número es más bajo.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

    jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ")
    if jugar_otra_vez.lower() == 's':
        adivina_el_numero()
    else:
        print("¡Gracias por jugar!")

# Iniciar el juego
adivina_el_numero()


