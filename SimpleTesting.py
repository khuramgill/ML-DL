import numpy as np
import matplotlib.pyplot as plt

def randomData():
    x = np.random.randint(27, 38, 15)
    y = np.random.randint(10, 76, 15)
    return x, y

def main():
    x, y = randomData()
    plt.vlines(x, [0], y, color='red', label='Random data')
    plt.plot_date(x, y, color='blue', linestyle='solid', marker='o', label='Random data')
    # plt.bar(x, y, color='green', label='Random data')
    plt.axhline(0, color='blue', linewidth=1)  # Plot x-axis line
    plt.axvline(0, color='yellow', linewidth=1)  # Plot y-axis line
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
