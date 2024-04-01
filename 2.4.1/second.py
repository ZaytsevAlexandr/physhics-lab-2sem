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


colors = ['red', 'blue']

plt.figure(figsize=(8, 6))
plt.grid(which="both")
plt.minorticks_on()
plt.tick_params(which="minor", bottom=True, left=True)

text = ['Нагревание', 'Охлаждение']
N = [17, 8]

for i in range(2):
    x, y = read_points(f'data_second_{i}.txt')
    k, b = fit_line(x, y)
    sr_x2 = 0
    sr_x = 0
    sr_y = 0
    sr_y2 = 0
    for e in range(N[i]):
        sr_x2 = sr_x2 + x[e] * x[e]
        sr_x = sr_x + x[e]
    sr_x2 = sr_x2 / N[i]
    sr_x = sr_x / N[i]
    for h in range(N[i]):
        sr_y2 = sr_y2 + y[h] * y[h]
        sr_y = sr_y + y[h]
    sr_y2 = sr_y2 / N[i]
    sr_y = sr_y / N[i]
    error_k = (1 / (N[i]**0.5)) * (((sr_y2 - sr_y*sr_y) / (sr_x2 - sr_x*sr_x) - k**2)**0.5)
    c = []
    for j in range(len(x)):
        c.append(k * x[j] + b)
    plt.plot(x, c, color=colors[i], linestyle='dashed', linewidth=2, label=f'{text[i]}: k = {round(k,2)} $\pm$ {round(error_k,2)}')
    plt.errorbar(x, y, xerr=0.000003, yerr=0.01, fmt='.', color=colors[i], markersize='2', capsize=1, elinewidth=1)

plt.legend()
plt.xlabel('1/K, T$^-$$^1$')
plt.ticklabel_format(style='scientific', useMathText=True)
plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
plt.ylabel('lnP')
plt.title('lnP (1/T)')
plt.xlim(0.00318, 0.00337)
plt.ylim(7.7, 8.9)

plt.show()
