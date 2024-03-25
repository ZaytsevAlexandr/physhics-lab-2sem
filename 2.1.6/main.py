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
plt.grid(which="both")
plt.minorticks_on()
plt.tick_params(which="minor", bottom=True, left=True)

T = [20, 35, 45, 55]
mu_error = []

for i in range(4):
    x, y = read_points(f'data_{i+1}.txt')
    k, b = fit_line(x, y)
    sr_x2 = 0
    sr_x = 0
    sr_y = 0
    sr_y2 = 0
    for e in range(6):
        sr_x2 = sr_x2 + x[e] * x[e]
        sr_x = sr_x + x[e]
    sr_x2 = sr_x2 / 6
    sr_x = sr_x / 6
    for h in range(6):
        sr_y2 = sr_y2 + y[h] * y[h]
        sr_y = sr_y + y[h]
    sr_y2 = sr_y2 / 6
    sr_y = sr_y / 6
    error_k = (1 / (6**0.5)) * (((sr_y2 - sr_y*sr_y) / (sr_x2 - sr_x*sr_x) - k**2)**0.5)
    c = []
    for j in range(len(x)):
        c.append(k * x[j] + b)
    plt.plot(x, c, color=colors[i], linestyle='dashed', linewidth=2, label=f'T = {T[i]}°C, μ = {round(k,2)} $\pm$ {round(error_k,2)} K/бар')
    plt.errorbar(x, y, xerr=0.1, yerr=0.01, fmt='.', color=colors[i], markersize='2', capsize=1, elinewidth=1)

plt.legend()
# plt.text(0.005, 0.72, f'Угловой коэффициент прямой k: {round(k, 3)}')
# plt.text(0.005, 0.71, f'Свободный член m: {round(b, 2)}')
plt.xlabel('ΔP, бар')
plt.ylabel('ΔT, K')
plt.title('ΔT(ΔP)')
plt.xlim(1.38, 4.2)
plt.ylim(0, 3.1)

plt.show()
