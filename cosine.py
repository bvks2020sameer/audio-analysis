from matplotlib import pyplot as plt
from math import *
x = [x for x in range(361)]
cosine = [cos(x*2*pi/180) for x in range(361)]
plt.title("Cosine Wave")
plt.plot(x,cosine)
plt.show()