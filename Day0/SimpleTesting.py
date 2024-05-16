import numpy as np
import matplotlib.pyplot as plt

def randomData():
    x = np.random.randint(27, 38, 5)
    y = np.random.randint(10, 76, 5)
    return x, y

def main():
    x, y = randomData()
    plt.vlines(x, [0], y, color='red', label='Random data')
    plt.plot_date(x, y, color='blue', linestyle='solid', marker='o', label='Random data')
    plt.xlabel("Year")
    plt.ylabel("Ratio")
    plt.title("Line Chart")
    # plt.bar(x, y, color='green', label='Random data')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
