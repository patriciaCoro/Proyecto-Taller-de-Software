from time import sleep
import random
while True:
    n = input("Ingrese número de jugadores:") 
        
    try:
        n = int(n)
        break
               
    except ValueError:
        print ("Atención debe ingresar un número entero.")
        
lista_integrantes =[]
NumCartillas =[]
for i in range (n):
    Integrante = input("Integrante" + str(i+1)+": ")
    lista_integrantes.append(Integrante)
    while True:
        while True:
            cartillas = input("Número de cartillas: ")
            try:
                cartillas = int(cartillas)
                break
            except ValueError:
                print ("Atención debe ingresar un número entero.")
                
        if (cartillas <= 3):
            NumCartillas.append(cartillas)
            break
        else:
            print("Recuerde que solo puede commprar 3 cartillas")

bol_sac =[]

num = list(range(1,81))
random.shuffle(num)


def mostrar_bolilla():
    resultado = num[0]
    bol_sac.append(resultado)
    num.remove(resultado)
       
    return resultado

suma = 0
for i in NumCartillas:
    suma = suma + i
pozo = suma*5

 

      
def menu():
    print("=-="*30)
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
        if len(bol_sac) ==80:
            print ("Ya no hay más bolillas")
        else:
            print (mostrar_bolilla())
    elif menu_opciones == "2":
        print("")
        print("Haz pulsado la opción Mostrar Resumen de bolillas")
        print (bol_sac)
    elif menu_opciones == "3":
        print("")
        print("Finalizando..............")
        print("Haz pulsado la opción Finalizar juego, el pozo ganado es: ")
        print(pozo)
        sleep(5)
    elif menu_opciones == "4":
        print("")
        print("Haz pulsado la opción Reiniciar juego ")
        while True:
            n = input("Ingrese número de jugadores:") 
        
            try:
                n = int(n)
                break
               
            except ValueError:
                print ("Atención debe ingresar un número entero.")
        
        
        lista_integrantes =[]
        NumCartillas =[]
        for i in range (n):
            Integrante = input("Integrante" + str(i+1)+": ")
            lista_integrantes.append(Integrante)
            while True:
                while True:
                    cartillas = input("Número de cartillas: ")
                    try:
                        cartillas = int(cartillas)
                        break
                    except ValueError:
                        print ("Atención debe ingresar un número entero.")
                
                if (cartillas <= 3):
                    NumCartillas.append(cartillas)
                    break
                else:
                    print("Recuerde que solo puede commprar 3 cartillas")
            
        bol_sac =[]

        num = list(range(1,81))
        random.shuffle(num)
        suma = 0
        for i in NumCartillas:
            suma = suma + i
        pozo = suma*5
    else:
        print("")
        print("Ingrese un número válido")