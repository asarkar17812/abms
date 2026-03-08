import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 0.5
k = 2

# Equilibrium
P_eq = k / alpha

# Symmetric x-limits centered at zero, ensure equilibrium fits well
x_max = max(abs(P_eq * 1.5), 6)
x_min = -x_max

# x values
P = np.linspace(x_min, x_max, 300)

# Growth curve
G = alpha * P - k

# Symmetric y-limits centered at zero
y_lim = max(abs(G.max()), abs(G.min())) * 1.1
y_min = -y_lim
y_max = y_lim

plt.figure(figsize=(10,6))

# Plot growth curve
plt.plot(P, G, color='blue', lw=2, label=r'$G(P) = \alpha P - k$')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1, linestyle='--', alpha=0.6)  # vertical line at origin

# Plot equilibrium point
plt.plot(P_eq, 0, 'ro', markersize=10, label=r'Equilibrium $P^* = k/\alpha$')

# Phase arrows along x-axis
arrow_props = dict(facecolor='black', width=1, headwidth=6, headlength=8)

# Left of equilibrium (point away)
arrow_x_left = np.linspace(x_min+0.2, P_eq-0.2, 6)
for xi in arrow_x_left:
    plt.annotate('', xy=(xi-0.25, 0), xytext=(xi+0.25, 0), arrowprops=arrow_props)

# Right of equilibrium (point toward equilibrium)
arrow_x_right = np.linspace(P_eq+0.2, x_max-0.2, 6)
for xi in arrow_x_right:
    plt.annotate('', xy=(xi+0.25, 0), xytext=(xi-0.25, 0), arrowprops=arrow_props)

# Labels and legend
plt.xlabel('Party Size (P)', fontsize=12)
plt.ylabel('Growth Rate (G(P))', fontsize=12)
plt.title('Question 1c: Party Growth Curve Stability and Equilibria Plot', fontsize=14)
plt.legend()
plt.grid(True)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.show()