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
            
print(NC)     











rb = int(input("Desea mostrar el resumen de bolillas"))
finjuego = int(input("Desea finalizar juego"))
    



















































