import matplotlib.pyplot as plt
import numpy as np


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


plt.figure(figsize=(8, 6))
plt.grid(which="both")
plt.minorticks_on()
plt.tick_params(which="minor", bottom=True, left=True)

x, y = read_points('data_0.txt')
for k in range(4):
    x[k] = x[k] * x[k]
    print(x[k])
k, b = fit_line(x, y)
sr_x2 = 0
sr_x = 0
sr_y = 0
sr_y2 = 0
for e in range(4):
    sr_x2 = sr_x2 + x[e] * x[e]
    sr_x = sr_x + x[e]
sr_x2 = sr_x2 / 4
sr_x = sr_x / 4
for h in range(4):
    sr_y2 = sr_y2 + y[h] * y[h]
    sr_y = sr_y + y[h]
sr_y2 = sr_y2 / 4
sr_y = sr_y / 4
error_k = (1 / (4 ** 0.5)) * (abs((sr_y2 - sr_y * sr_y) / (sr_x2 - sr_x * sr_x) - k ** 2) ** 0.5)
error_m = error_k * ((sr_x2 - sr_x * sr_x)**0.5)
c = []
for j in range(len(x)):
    c.append(k * x[j] + b)
plt.plot(x, c, color='blue', linestyle='solid', linewidth=2)
errors = [0.01, 0.06, 0.02, 0.02]
for e in range(4):
    plt.errorbar(x[e], y[e], xerr=0, yerr=errors[e], fmt='o', color='red', markersize='4', capsize=2, elinewidth=0.3)

# plt.legend()
plt.ticklabel_format(style='scientific', useMathText=True)
plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
plt.text(0.0000095, 0.7, f'Угловой коэффициент прямой k: {round(k, 3)} $\pm$ {round(error_k,2)}')
plt.text(0.0000095, 0.65, f'Свободный член m: {round(b, 3)} $\pm$ {round(error_m,2)}')
plt.xlabel('1/T, K$^-$$^2$')
plt.ylabel('$\mu$, K/бар')
plt.title('$\mu$(T$^-$$^2$)')
plt.xlim(0.000009, 0.000012)
plt.ylim(0.45, 1.35)

plt.show()
