# last graphic hard to understand :(

import numpy as np
import matplotlib.pyplot as plt
import math

def least_squares_fit(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xx = np.sum(x * x)
    sum_xy = np.sum(x * y)

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
    b = (sum_y - m * sum_x) / n
    # plt.text(300, 0.4, "k = {0:.5f}".format(m))

    return m, b


def plot_least_squares_line(x, y, ax):
    m, b = least_squares_fit(x, y)
    ax.plot(x, m * x + b, color='red', linestyle='dashed')

def plot_points(x, y, ax):
    ax.scatter(x, y, color='blue', s=20)


def read_numbers_from_fileX(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = float(line.strip()) + 273
                numbers.append(number)
            except ValueError:
                print(f"Skipping line '{line.strip()}' as it doesn't contain a valid number.")

    return np.array(numbers)
def read_numbers_from_fileY(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Skipping line '{line.strip()}' as it doesn't contain a valid number.")

    return np.array(numbers)

x = read_numbers_from_fileX("pressure.txt")
sigma = read_numbers_from_fileY("Q.txt")
y = x * 0.002 + sigma


fig, ax = plt.subplots()
ax.set_title('U/F(T)')
ax.set_xlabel('T, K')
ax.set_ylabel('U/F, Дж/м2')
ax.set_xlim(295,335)
ax.set_ylim(2.385,2.405)

plot_points(x, y, ax)
plot_least_squares_line(x, y, ax)
# plt.vlines(x = 18.569, ymin = 80, ymax = 500, colors = 'red', linestyles = 'dashed')

ax.grid(True)

plt.show()
