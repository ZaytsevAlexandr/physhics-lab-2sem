import numpy as np
import matplotlib.pyplot as plt

def least_squares_fit(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xx = np.sum(x * x)
    sum_xy = np.sum(x * y)

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
    b = (sum_y - m * sum_x) / n

    return m, b

def plot_least_squares_line(x, y, ax):
    m, b = least_squares_fit(x, y)
    ax.plot(x, m * x + b, color='red', linestyle='dashed')


def plot_points(x, y, ax):
    ax.scatter(x, y, color='blue', s=20)


def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Skipping line '{line.strip()}' as it doesn't contain a valid number.")

    return np.array(numbers)

x = read_numbers_from_file("pressure.txt")
x1 = x[0:8]
y = read_numbers_from_file("Q.txt")
y1 = y[0:8]

fig, ax = plt.subplots()
ax.set_title('Q от dP')
ax.set_xlabel('dP')
ax.set_ylabel('Q')
ax.set_xlim(5, 155)
ax.set_ylim(0.01, 0.15)

plot_points(x, y, ax)
plot_least_squares_line(x1, y1, ax)

ax.grid(True)

plt.show()
