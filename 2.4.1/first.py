import numpy as np
import matplotlib.pyplot as plt

def read_points(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        x = [float(line.split()[0]) for line in lines]
        y = [float(line.split()[1]) for line in lines]
    return x, y


colors = ['red', 'blue']
text = ['Нагревание', 'Охлаждение']

plt.figure(figsize=(8, 6))
plt.grid(which="both")
plt.minorticks_on()
plt.tick_params(which="minor", bottom=True, left=True)
for i in range(2):
    x, y = read_points(f'data_{i}.txt')
    plt.plot(x, y, 'ro', color=colors[i], label=text[i])
    plt.errorbar(x, y, xerr=0.01, yerr=0.01, fmt='.', color=colors[i], markersize='2', capsize=1, elinewidth=1)

plt.legend()
plt.xlabel('T, K')
plt.ylabel('ΔP, Па')
plt.title('ΔP(T)')
plt.xlim(273+23, 273+41)
plt.ylim(2300, 6500)

plt.show()

