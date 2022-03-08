from matplotlib import pyplot as plt
from math import *
x =[x for x in range(361)]
sine = [sin(x*2*pi/180) for x in range(361)]
plt.title("sine wave")
plt.plot(x,sine)
plt.show()