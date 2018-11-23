def comprobar(inputPassword):
    haveNumeric = False

    longer = False
    haveMayus = False
    haveMinus = False
    notSpace = False

    if len(inputPassword) > 12:
        for caracter in inputPassword:
            if caracter.isspace() & ~notSpace:
                notSpace = True
            elif caracter.isnumeric() & ~haveNumeric:
                haveNumeric = True
            elif caracter.islower() & ~haveMinus:
                haveMinus = True
            elif caracter.isupper() & ~haveMayus:
                haveMayus = True

            if haveMinus & haveMayus & haveMayus & notSpace:
                print("valida")
            else:
                print("La contraseña elegida no es segura")
    else:
        print("La contraseña elegida no es segura")


inputPassword = input("Escribe la contraseña\n")
comprobar(inputPassword)
