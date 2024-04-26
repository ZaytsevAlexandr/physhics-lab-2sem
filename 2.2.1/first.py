import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from scipy.optimize import curve_fit
import pandas as pd
import numpy as np

import os

fig, axs = plt.subplots(2, 3, figsize=(10, 7))
plt.tight_layout()

current = os.getcwd()
path = "".join([current, "/csv/"])
dir_list = os.listdir(path)

df, sheets = [], []
tau = []

majorLocator = MultipleLocator(20)
majorFormatter = FormatStrFormatter('%d')
minorLocator = MultipleLocator(5)

for file in dir_list:
    df.append(pd.DataFrame(pd.read_csv("".join([path, file]))))
    sheets.append(file.split('_')[2].replace('.csv', ''))


def line(x, a, b):
    return a * x + b


def draw(i, current, color, surest):
    popt, pcov = curve_fit(line, df[i]["t (s)"], np.log(df[i]["V (mV)"]))
    current.plot(df[i]["t (s)"], np.log(df[i]["V (mV)"]), ''.join(['tab:', color]), label='fit: k=%6.4f, b=%3.4f' % tuple(popt))
    current.set_xlim(0, 250)
    current.grid(which="both")
    current.minorticks_on()
    current.tick_params(which="minor", bottom=True, left=True)
    current.legend()
    tau.append(-1 / popt[0])
    if surest:
        current.set_title('37.5 торр (другой пункт)')
    else:
        current.set_title(sheets[i] + ' торр')



draw(0, axs[0, 0], 'orange', 0)
draw(1, axs[0, 1], 'blue', 0)
draw(2, axs[0, 2], 'purple', 0)
draw(3, axs[1, 0], 'green', 0)
draw(4, axs[1, 1], 'olive', 0)
draw(5, axs[1, 2], 'cyan', 1)

axs[0, 0].xaxis.set_ticks(np.arange(0, 300, 50))

tau = np.array(tau)
V = 1200 * 10 ** (3)
LnaS = 5.5 * 10 ** (-1)

D = 0.5 * V * LnaS / tau * 0.01
obrP = np.array([1 / float(p.replace('(new)', '')) for p in sheets])

fig.tight_layout()
plt.show()

print([round(i, 2) for i in D])
obrP = obrP[:-1]
D = D[:-1]
plt.plot(obrP, D)
plt.errorbar(obrP, D, yerr=0.1, xerr=0.0001, marker='o', linestyle='none',
             ecolor='k', elinewidth=0.75, capsize=1, markersize=0.75, capthick=0.75, color='red')

plt.grid()

plt.ylabel(r'$D, \frac{см^2}{c \cdot торр} $')
plt.grid(which="both", axis="both")
plt.minorticks_on()
plt.tick_params(which="major", bottom=True, left=True)
plt.xlabel(r'$\frac{1}{P}, \frac{1}{торр}$')
plt.show()

popt, pcov = curve_fit(line, obrP, D)
round(popt[0] / 729 + popt[1], 2)
