import random
n= int(input("Ingrese número de jugadores: "))
lista_integrantes =[]
NumCartillas =[]
for i in range (n):
    Integrante = input("Integrante" + str(i+1)+": ")
    lista_integrantes.append(Integrante)
    while True:
        cartillas = int(input("Número de cartillas: "))
        if (cartillas <= 3):
            NumCartillas.append(cartillas)
            break
        else:
            print("Recuerde que solo puede commprar 3 cartillas")

bol_sac =[]

num = list(range(1,81))
random.shuffle(num)


def mostrar_bolilla():
    resultado = num[1]
    bol_sac.append(resultado)
    num.remove(resultado)
       
    return resultado

suma = 0
for i in NumCartillas:
    suma = suma + i
print(suma)   
pozo = suma*5

 

      
def menu():
    print ("Seleccione una opción: ")
    print ("\t1 - Mostrar  bolillas  ")
    print ("\t2 - Mostrar resumen de bolillas obtenidas ")
    print ("\t3 - Finalizar juego y mostrar el pozo ganado ")
    print ("\t4 - Reiniciar juego ")
while True:
    menu()
    menu_opciones = input("Ingrese un número: ")
    if menu_opciones == "1":
        print("")
        print("Haz pulsado la opción Sacar bolillas")
        print (mostrar_bolilla())
    elif menu_opciones == "2":
        print("")
        print("Haz pulsado la opción Mostrar Resumen de bolillas")
        print (bol_sac)
    elif menu_opciones == "3":
        print("")
        print("Haz pulsado la opción Finalizar juego, el pozo ganado es: ")
        print(pozo)
    elif menu_opciones == "4":
        print("")
        print("Haz pulsado la opción Reiniciar juego ")
        n= int(input("Ingrese número de jugadores: "))
        lista_integrantes =[]
        NumCartillas =[]
        for i in range (n):
            Integrante = input("Integrante" + str(i+1)+": ")
            lista_integrantes.append(Integrante)
            while True:
                cartillas = int(input("Número de cartillas: "))
                if (cartillas <= 3):
                    NumCartillas.append(cartillas)
                    break
                else:
                    print("Recuerde que solo puede commprar 3 cartillas")

        bol_sac =[]

        num = list(range(1,81))
        random.shuffle(num)
    else:
        print("")
        print("Ingrese un número válido")
