import numpy as np 
import matplotlib.pyplot as plt

def random():
    x = np.random.randint(2,29,15)
    y = np.random.randint(41,89,15)
    return x, y

def bar(x,y):
    colors = np.where(x < 10, 'skyblue' , np.where(y < 50, 'grey', 'pink'))
    plt.figure(figsize=(10, 6))
    plt.bar(x,y,color=colors)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Tesing Bar Plot")
    plt.grid(True)
    plt.show()

def line(x,y):
    
    plt.plot(x,y)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.grid(True)
    plt.show()

def vline(x,y):
    plt.vlines(x, [0], y, color='red', label='Random data')
    plt.plot_date(x, y, color='blue', linestyle='solid', marker='o', label='Random data')
    plt.xlabel("Year")
    plt.ylabel("Ratio")
    plt.title("Line Chart")
    # plt.bar(x, y, color='green', label='Random data')
    plt.legend()
    plt.show()

def Dot(x,y):
    # plt.plot(x,y)
    plt.scatter(x,y)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    x, y = random()
    print("Values of X: ", x)
    print("Values of Y: ",y)
    Dot(x,y)

    
    
