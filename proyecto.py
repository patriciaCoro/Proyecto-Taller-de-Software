
n= int(input("Ingrese numero de jugadores: "))
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

def SumaPozo():
    suma = 0
    for i in NC:
        suma = suma + i
    pozo = suma*5

    return pozo

    
OB = int(input("¿Desea obtener una bolilla?: "))

rb = int(input("Desea mostrar el resumen de bolillas:"))

finjuego = int(input("Desea finalizar juego"))
    

R = int(input("¿ Desea reiniciar el juego?: "))
 




















































