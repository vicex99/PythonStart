import calendar

year = input("elige un año para comprobar si es bisiesto\n")
#
if year.isnumeric():
    if calendar.isleap(int(year)):
        print("Bisiesto")
    else:
        print("no es Bisiesto")


#     if len(year) == 4:
#         year = int(year)
#         print(year % 4)
#         if year % 4 == 0 & year % 100 != 0:
#             print("ES BISIESTO")
#         else:
#             print("no es Bisiesto")
#     else:
#         print("datos erroneos, acuerdate que un año tiene 4 digitos")
else:
    print("datos erroneos, acuerdate que un año solo digitos")



