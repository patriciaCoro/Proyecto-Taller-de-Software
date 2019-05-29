import os 

def menu():
    os.system('cls')
    print ("Seleccione una opcion: ")
    print ("\t1 - Obtener bolilla")
    print ("\t2 - Reiniciar juego")
    print ("\t3 - Mostrar resumen de bolillas obtenidas")
    print ("\t4 - Finalizar juego ")

while True:
    menu()
    menu_opciones = input("Ingresa un valor: ")
    if menu_opciones == "1":
        print ("")
        input("Haz pulsado la opcion Obtener bolillas ... \npulsa una tecla para continuar")
    elif menu_opciones == "2":
        print ("")
        input("Haz pulsado la opcion Reiniciar juego ... \npulsa una tecla para continuar")
    elif menu_opciones == "3":
        print("")
        input("Haz pulsado la opcion Mostrar resumen de bolillas obtenidas ... \npulsa una tecla para continuar")
    elif menu_opciones == "4 ":
        break
    else:
        print("")
        input("No haz pulsado ninguna opcion")