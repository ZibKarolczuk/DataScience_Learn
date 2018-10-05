import matplotlib.pyplot as plot
import numpy as np
import math as mt
import random as rd

participants = np.arange(1,31,1)

height = []
weight = []

for x in participants:
    height.append(rd.randint(153, 203))
    weight.append(rd.randint(51, 93))

plot.plot(participants, weight)
plot.plot(participants, height)
plot.grid(True)
plot.title("Wyjkres wzrostu/wagi uczestników")
plot.xlabel("Uczestnicy")
plot.ylabel("Wzrost [cm] / Waga [kg]")
plot.savefig("z6x.png")
# plot.legend(weight, height)
plot.show()
