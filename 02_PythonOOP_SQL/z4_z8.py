import math

name = "Zbyszek"

weight = 78.3
height = 178.5

def getBMI(w, h):
    return w / math.pow((h/100),2)

def printBMI(name, bmi):
    if (bmi > 25):
        print(name + " twoje BMI wynosi " + str(bmi) + " i masz nadwagę!")
    elif (bmi < 20.5):
        print(name + " twoje BMI wynosi " + str(bmi) + " i masz niedowagę...")
    else:
        print(name + " twoje BMI wynosi " + str(bmi) + " i jest w normie :-)")

printBMI(name, round(getBMI(weight, height), 2))
