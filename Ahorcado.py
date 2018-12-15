import os

os.system('cls')
seleccion = 's'

print("¡Bienvenido al ahorcado!")

while seleccion == 's':
    output = []
    letras = []
    intentos = 8
    comprueba = ""
    palabra = str(input("Inserta una palabra: "))
    os.system('cls')

    for i in range(0, len(palabra)):
        output.insert(i, "_")

    print("¡Ya podemos empezar a jugar!")
    while intentos != 0 and comprueba != palabra:

        print("\n", " ".join(output))
        print("Letras intentadas: ", ", ".join(letras))
        print("Intentos restantes: ", intentos, "\n\n")
        letra = str(input("Escribe una letra: "))
        while len(letra) != 1:
            letra = str(input("Escribe solo una letra: "))


        if letra in palabra:
            if letra not in output:
                print("¡Has acertado!")
                for i in range(0, len(palabra)):
                    if palabra[i] == letra:
                        output[i] = letra
            else:
                print("Ya has adivinado esta letra")
        else:
            if letra not in letras:
                print("¡Ops! Esa letra no está en la palabra")
                letras.append(letra.lower())
                intentos = intentos - 1
            else:
                print("Ya has intentado poner esta letra")
        
        comprueba = "".join(output)

    if comprueba == palabra:
        print("¡Enhorabuena! Has adivinado la palabra. ¿Quieres volver a jugar?")
        seleccion = str(input("Escribe s para empezar una partida nueva y cualquier otro caracter para terminar el juego: "))
        while len(seleccion) != 1:
            seleccion = str(input("Inserta solo un caracter: "))

