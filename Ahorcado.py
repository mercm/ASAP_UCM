import os

os.system('cls||clear')
seleccion = 's'

print("¡Bienvenido al ahorcado!")

while seleccion == 's':
    adivinadas = []
    falladas = []
    intentos = 6
    comprueba = ""
    palabra = str(input("Inserta una palabra: ")).upper()
    os.system('cls||clear')

    for _ in range(len(palabra)):
        adivinadas.append("_")

    print("¡Ya podemos empezar a jugar!")
    while intentos != 0 and comprueba != palabra:

        print("\n", " ".join(adivinadas))
        print("Palabras intentadas: ", ", ".join(falladas))
        print("Intentos restantes: ", intentos, "\n\n")
        letra = str(input("Escribe una letra: ")).upper()
        while len(letra) != 1:
            letra = str(input("Escribe solo una letra: ")).upper()

        if letra not in adivinadas and letra not in falladas:
            if letra in palabra:
                print("¡Has acertado!")
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        adivinadas[i] = letra
            else:
                print("¡Ops! Esa letra no está en la palabra")
                falladas.append(letra)
                intentos = intentos - 1
        else:
            print("Ya has probado con esta letra")
        
        comprueba = "".join(adivinadas)

    if comprueba == palabra:
        print("¡Enhorabuena! Has adivinado la palabra", palabra, ". ¿Quieres volver a jugar?")
    elif intentos == 0:
        print("Te quedaste sin intentos, la respuesta era: ", palabra)
    seleccion = input("Escribe s para empezar una partida nueva y cualquier otro caracter para terminar el juego: ")

