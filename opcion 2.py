import os
def menu():
    os.system('cls')
    print("Seleccione una opcion: \n \t1-registrar datos \n \t2-obtener bolillas \n \t3-Mostrar resumen de bolillas obtenidas \n \t4- Reiniciar juego \n \t5- Finalizar juego y mostrar pozo")

while True:
    menu()
    menu_opciones = input("Ingrese un numero: ")
    if menu_opciones == "1":
        print("")
        input("Haz pulsado la opcion registrar datos")
    elif menu_opciones == "2":
        print("")
        input("haz pulsado la opcion obtener bolillas")
    elif menu_opciones == "3":
        print("")
        input("haz pulsado la opcion mostrar resumen de bolillas")
    elif menu_opciones == "4":
        print("reiniciar juego")
        input("haz pulsado la opcion reiniciar juego")
    elif menu_opciones == "5":
        print("")
        input("haz pulsado la opcion finalizar juego, el pozo es, ")
    else:
        print("")
        input("ingrese un numero valido")



