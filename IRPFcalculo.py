
tramosProcentaje = ["12450", "20200", "35200", "60000"]


# Con un for
# def calculoFor(sueldo):
#     if sueldo.isnumeric():
#         iSueldo = int(sueldo)
#         primero = True
#         cont = 0
#         print(cont)
#         while cont < len(tramosProcentaje):
#
#             if iSueldo < int(tramosProcentaje[cont]):
#                 iSueldo = (iSueldo * 19) / 100
#                 print(cont)
#                 print(iSueldo)
#                 # primero = False
#             print(cont)
#             cont += 1
#
#     else:
#         print("el sueldo tiene que ser un valor numerico")


# Con un if .. elif .. else
def calculoIf(sueldo):
    if sueldo.isnumeric():
        iSueldo = int(sueldo)
        if iSueldo < 12450:
            iSueldo = (iSueldo * 19) / 100
            print(1)
        elif iSueldo < 20200:
            iSueldo = (iSueldo * 24) / 100
            print(2)
        elif iSueldo < 35200:
            iSueldo = (iSueldo * 30) / 100
            print(3)
        elif iSueldo < 60000:
            iSueldo = (iSueldo * 37) / 100
            print(4)
        else:
            iSueldo = (iSueldo * 45) / 100
            print(5)
        print(iSueldo)
    else:
        print("el sueldo tiene que ser un valor numerico")


sSueldo = input("introduce tu sueldo para saber tu IRPF\n")

# calculoFor(sSueldo)
calculoIf(sSueldo)
