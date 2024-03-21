import numpy
import numpy as np
import matplotlib.pyplot as plt

def fit_line(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    k, b = np.linalg.lstsq(A, y, rcond=None)[0]
    return k, b

def read_points(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        x = [float(line.split()[0]) for line in lines]
        y = [float(line.split()[1]) for line in lines]
    return x, y

colors = ['red', 'green', 'blue', 'purple']

plt.figure(figsize=(8, 6))
plt.grid(True)

T = [20, 35, 45, 55]

for i in range(4):
    x, y = read_points(f'data_{i+1}.txt')
    k, b = fit_line(x, y)
    c = []
    for j in range(len(x)):
        c.append(k * x[j] + b)
    plt.plot(x, c, color=colors[i], linewidth=2, label=f'T = {T[i]}°C, μ = {round(k, 2)} К/бар')
    plt.errorbar(x, y, xerr=0.01, yerr=0.01, fmt='o', color=colors[i])

plt.legend()
plt.xlabel('ΔP, бар')
plt.ylabel('ΔT, °C')
plt.title('ΔT от ΔР')
plt.xlim(1.3, 4.2)
plt.ylim(0, 3.2)

plt.show()
