import math

def sumatory(start, end):
    i = start
    sumatory = 0

    while i < end:
        sumatory += math.sqrt(i)
        i += 1

    return sumatory


a = input("introduce valor inicio\n")
b = input("introduce valor final\n")
if a.isnumeric() & a.isnumeric():

    a = int(a)
    b = int(b)
    if 0<a & a<b:
        print(sumatory(a, b))
    else:
        print("a tiene que ser mayor que 0\ny b mayor que a")
else:
    print("valor incorrecto, itroduce un valor numerico")
