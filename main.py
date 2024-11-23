import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 10))
plt.grid(True)

# Vertical
vertical_lines = [
    (-4.8, -2, 2), (-3, -2, 2), (1.2, -2, 2), (2.8, -2, 2), (6, -2, 2),
    (-6.9, -5, -3), (-6.1, -5, -3), (-4.9, -5, -3), (-3.5, -5, -3),
    (7, -5, -3), (6.1, -4, -3), (5.9, -4, -3), (5.1, -5, -4),
    (4.9, -5, -3), (4.1, -5, -3), (3.9, -4, -3), (3.1, -5, -4),
    (-1.9, -5, -3), (-1.1, -5, -4), (-0.9, -5, -3), (-0.1, -5, -3),
    (0.1, -5, -3), (1.1, -5, -3), (1.9, -5, -3)
]

for x, ymin, ymax in vertical_lines:
    plt.vlines(x=x, ymin=ymin, ymax=ymax, color='blue', linewidth=3)

# Horizontal
horizontal_segments = [
    (-4.8, -3.5, 2), (-4.8, -4, 0), (-4.8, -3.5, -2), (-3, -1.5, -2),
    (-0.5, 0.5, 0), (3.5, 4.5, 0), (5, 7, 2), (-6.9, -6.1, -4),
    (-5.75, -5.25, -4), (-3.9, -3.1, -3), (-3.9, -3.1, -5),
    (6.1, 7, -4), (5.1, 5.9, -3), (5.1, 5.9, -4), (5.1, 5.9, -5),
    (4.1, 4.9, -3), (4.1, 4.9, -5), (3.1, 3.9, -3), (3.1, 3.9, -4),
    (3.1, 3.9, -5), (-1.9, -1.1, -3), (-1.9, -1.1, -5), (-1.4, -1.1, -4),
    (-0.9, -0.1, -5), (1.1, 1.9, -5)
]

for x_start, x_end, y in horizontal_segments:
    plt.plot([x_start, x_end], [y, y], 'blue', linewidth=3)

# Linear
linear_segments = [
    ((-1, 0), lambda x: 4*x + 2),
    ((0, 1), lambda x: -4*x + 2),
    ((1.2, 2), lambda x: -2.5*x + 5),
    ((2, 2.8), lambda x: 2.5*x - 5),
    ((3, 4), lambda x: 4*x - 14),
    ((4, 5), lambda x: -4*x + 18),
    ((-6, -5.5), lambda x: 4*x + 19),
    ((-5.5, -5), lambda x: -4*x - 25),
    ((-4.9, -4.1), lambda x: -1.25*x - 10.13),
    ((0.1, 0.9), lambda x: -1.25*x - 3.88)  # New linear segment
]

for (start, end), func in linear_segments:
    x = np.linspace(start, end, 100)
    plt.plot(x, func(x), 'blue', linewidth=3)

# Parabola
y_parab1 = np.linspace(-4, -3, 100)
x_parab1 = -3.2*(y_parab1 + 3.5)**2 - 4.1
plt.plot(x_parab1, y_parab1, 'blue', linewidth=3)
y_parab2 = np.linspace(-5, -3, 100)
x_parab2 = -3.2*(y_parab2 + 3.5)**2 + 0.9
x_parab2_masked = np.where(x_parab2 >= 0.1, x_parab2, np.nan)
plt.plot(x_parab2_masked, y_parab2, 'blue', linewidth=3)

# Lingkaran
theta1 = np.linspace(np.pi, 3*np.pi, 100)
x_circle1 = np.cos(theta1) - 6
y_circle1 = np.sin(theta1) + 1
x_circle1_masked = np.where(x_circle1 < -6, x_circle1, np.nan)
plt.plot(x_circle1_masked, y_circle1, 'blue', linewidth=3)
x_circle1_masked = np.where(x_circle1 > -6, x_circle1, np.nan)
y_circle1_masked = np.where(y_circle1 > 1, y_circle1, np.nan)
plt.plot(x_circle1_masked, y_circle1_masked, 'blue', linewidth=3)

theta2 = np.linspace(-np.pi, np.pi, 100)
x_circle2 = np.cos(theta2) - 6
y_circle2 = np.sin(theta2) - 1
x_circle2_masked = np.where(x_circle2 > -6, x_circle2, np.nan)
plt.plot(x_circle2_masked, y_circle2, 'blue', linewidth=3)
x_circle2_masked = np.where(x_circle2 < -6, x_circle2, np.nan)
y_circle2_masked = np.where(y_circle2 < -1, y_circle2, np.nan)
plt.plot(x_circle2_masked, y_circle2_masked, 'blue', linewidth=3)

plt.xlim(-8, 8)
plt.ylim(-6, 4)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Selamat Hari Guru 2024')
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)

plt.show()