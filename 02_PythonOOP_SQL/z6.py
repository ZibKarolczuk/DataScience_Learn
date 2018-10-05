import math as m

def powerDividedByNum(number, power):
    if (number % 3 == 0):
        return m.pow(number, power)

def printList(array):
    for x in array:
        if (x != None):
            print(x)

lista_kwadrat = map(lambda x: m.pow(x, 2), range(1,13))
printList(lista_kwadrat)

lista_kwadrat2 = map(lambda x: powerDividedByNum(x, 2), range (1,31))
printList(lista_kwadrat2)
