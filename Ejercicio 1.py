def jugar(intento -1):
    respuesta = input("Ingrese el color de la fruta: ")

    if respuesta != "naranja":
        if intento < 3:
            print("")
            print("Fallaste, intenta de nuevo:")
            intento += 1
            jugar(intento)
        else:
            print("Perdiste")
    else:
        print("Ganaste")

jugar()