import random

def funcionAcertar():

    noAcierta = True

    while noAcierta:

        strInput = input("¿Que numero he pensado?\n")
        if strInput.isnumeric():
            numInput = int(strInput)
            if numInput == numRandom:
                noAcierta = False
            elif numInput <= numRandom:
                print("mi numero pensado es mayor")
            else:
                print("mi numero pensado es menor")
        else:
            print("valor incorrecto, porfavor inserta un numero")

    print("acertastes")


# el segundo numero tiene que ser el siguiente al ultimo deseado
numRandom = random.randrange(1, 101)
print(numRandom, " he pensado un numero entre 1 y 100")

funcionAcertar()