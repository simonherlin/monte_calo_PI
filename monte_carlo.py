"""
    Aproximation of PI value with the method monte carlo
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

figure = plt.figure(figsize=(8,8))
axes1 = figure.add_subplot(1, 1, 1)
axes1.set_title("Aproximation of PI value with the method monte carlo")
axes1.set_xlim(0, 1.5)
axes1.set_ylim(0, 1.5)

# Draw square
x = [1, 1, 1, 0]
y = [0, 1, 1, 1]
axes1.plot(x, y, color='k', linestyle='-', linewidth=3)

# Draw quarter circle
circle1 = plt.Circle((0, 0), 1, color='k', fill=False, linewidth=3)
axes1.add_artist(circle1)
plt.show()