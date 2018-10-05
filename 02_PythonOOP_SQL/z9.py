import random as rd
import numpy as np

import matplotlib.pyplot as pypl

samples = range(1, 21)
salary = []

for s in samples:
    salary.append(rd.randint(3500, 9601))

print ("Average salary is " + str(np.round(np.mean(salary), 0)) + " PLN")
print ("Median salary is " + str(np.round(np.median(salary), 0)) + " PLN")

pypl.plot(samples, salary)
pypl.grid(True)
pypl.show()
