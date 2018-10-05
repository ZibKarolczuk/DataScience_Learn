import statistics
import math
import numpy

def printStats(arr):
    print("\nMediana: ")
    print(statistics.median(arr))
    print("Średnia erytmetyczna: ")
    print(statistics.mean(arr))

def addToArray(var, arr):
    arr.append(len(var))

pierwszy_uczestnik = "Ania"
drugi_uczestnik = "Marek"

print(pierwszy_uczestnik)
print(drugi_uczestnik)

#PIERWSZY SPOSÓB WYMIANY ZMIANNYCH
#temp = drugi_uczestnik
#drugi_uczestnik = pierwszy_uczestnik
#pierwszy_uczestnik = temp

#DRUGI SPOSÓB NA ZAMIANĘ ZMIENNYCH
pierwszy_uczestnik, drugi_uczestnik = drugi_uczestnik, pierwszy_uczestnik

print(pierwszy_uczestnik)
print(drugi_uczestnik)

trzeci_uczestnik = "Wierzchosława"

print (len(pierwszy_uczestnik))
print(len(drugi_uczestnik))
print(len(trzeci_uczestnik))

array = []

addToArray(pierwszy_uczestnik, array)
addToArray(drugi_uczestnik, array)
addToArray(trzeci_uczestnik, array)

printStats(array)

czwarty_uczestnik = "Ada"

addToArray(czwarty_uczestnik, array)
printStats(array)
