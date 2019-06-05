import os 

def menu():
    os.system('cls')
    print ("Seleccione una opcion: ")
    print ("\t1 - Registrar datos ")
    print ("\t2 - Obtener bolilla ")
    print ("\t3 - Mostrar resumen de bolillas obtenidas ")
    print ("\t4 - Finalizar juego y mostrar el pozo ganado ")
    print ("\t5 - Reiniciar juego ")

while True:
    menu()
    menu_opciones = input("Ingresa un valor: ")
    if menu_opciones == "1":
        print ("")
        input("Haz pulsado la opcion Registrar datos... \npulsa una tecla para continuar")
        n= int(input("\nIngrese numero de jugadores: "))
        J =[]
        NC =[]
        for i in range (n):
            Integrante = input("Integrante" + str(i+1)+": ")
            J.append(Integrante)
            while True:
                cartillas = int(input("Número de cartillas: "))
                if (cartillas <= 3):
                    NC.append(cartillas)
                    break
    elif menu_opciones == "2":
        print ("")
        input("Haz pulsado la opcion Obtener bolillas... \npulsa una tecla para continuar")
    elif menu_opciones == "3":
        print("")
        input("Haz pulsado la opcion Mostrar resumen de bolillas obtenidas... \npulsa una tecla para continuar")
    elif menu_opciones == "4 ":
        break
    elif menu_opciones == "5":
        print("")
        input("Haz pulsado la opcion Reiniciar juego... \npulsa una tecla para continuar")
    else:
        print("")
        input("No haz pulsado ninguna opcion")