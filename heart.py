import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Equation Function
def heart_equation(x, k):
    return np.abs(x)**(2/3) + 0.9 * np.sin(k * x) * np.sqrt(3 - x**2)

# X values for heart
x = np.linspace(-np.sqrt(3), np.sqrt(3), 1000)

# Setup Plot
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

line, = ax.plot([], [], color='red', linewidth=2)
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.axis('off')

# Title and Equation
title = ax.text(0, 2.6, "Heart Equation" r"$y = |x|^{\frac{2}{3}} + 0.9 \sin(kx)\sqrt{3 - x^2}$" , fontsize=18, ha='center', color='violet')


# Animation Function
def update(frame):
    k = 40 + 40 * np.sin(frame / 10)  # oscillating k value
    y = heart_equation(x, k)
    line.set_data(x, y)
    return line,

# Animate
ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)

plt.show()
