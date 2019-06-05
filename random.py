import random
bol_sac =[]

c= 0
num = list(range(1,81))
random.shuffle(num)

def mostrar_bolilla():
    c= 0
    resultado = 0
    if c>80:
        resultado = num[1]
        bol_sac.append(resultado)
        num.remove(resultado)
        c=c+1
    else:
        resultado = "Ya no hay más bolillas "
    return resultado