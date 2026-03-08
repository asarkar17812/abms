import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 10
b = 2

# Equilibria
x_eq1 = 0           # unstable
x_eq2 = a / b       # stable

# Determine symmetric x-limits centered at 0
x_max_orig = x_eq2 * 1.5
x_max = max(abs(x_eq2 * 1.5), abs(-0.5))
x_min = -x_max

x = np.linspace(x_min, x_max, 300)

# Growth curve
G = a*x - b*x**2

# Symmetric y-limits
y_lim = max(abs(G.max()), abs(G.min())) * 1.1

plt.figure(figsize=(10,6))

# Plot growth curve
plt.plot(x, G, color='blue', lw=2, label=r'$G(x) = ax - bx^2$')
plt.axhline(0, color='black', linewidth=1)

# Plot equilibria points
plt.plot(x_eq1, 0, 'ro', markersize=10, label=r'Unstable equilibrium $x^*=0$')
plt.plot(x_eq2, 0, 'go', markersize=10, label=r'Stable equilibrium $x^*=5$')

# Phase arrows along x-axis
arrow_props = dict(facecolor='black', width=1, headwidth=6, headlength=8)

# Left of unstable equilibrium (point away)
arrow_x_left = np.linspace(x_min+0.2, -0.2, 6)
for xi in arrow_x_left:
    plt.annotate('', xy=(xi-0.25,0), xytext=(xi+0.25,0), arrowprops=arrow_props)

# Between equilibria (toward stable)
arrow_x_middle = np.linspace(0.2, x_eq2-0.2, 6)
for xi in arrow_x_middle:
    plt.annotate('', xy=(xi+0.25, 0), xytext=(xi-0.25, 0), arrowprops=arrow_props)

# Right of stable equilibrium (point toward stable)
arrow_x_right = np.linspace(x_eq2+0.2, x_max-0.2, 6)
for xi in arrow_x_right:
    plt.annotate('', xy=(xi-0.25, 0), xytext=(xi+0.25, 0), arrowprops=arrow_props)

# Labels and legend
plt.xlabel('Population (x)', fontsize=12)
plt.ylabel('Growth Rate (G(x))', fontsize=12)
plt.title('Question 6e: Logistic Growth Curve Stability and Equilibria Plot', fontsize=14)
plt.legend()
plt.grid(True)
plt.xlim(x_min, x_max)
plt.ylim(-y_lim, y_lim)

plt.show()