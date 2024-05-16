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
    # using default X-axis and marker properties
    plt.subplot(2,2,1)
    plt.plot(y,marker = '^',mec = 'hotpink',mfc = 'black' , ms = 10)
    # using custom X-axis and marker properties
    plt.subplot(2,2,3)
    plt.plot(x,marker = '*',mec = 'blue',mfc = 'red' , ls=":" , lw=0.9)
    # plt.plot(x,y,x,y**2,x,y**3)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.grid(color = 'g',ls=':',lw = 0.9)
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
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    plt.subplot(2,2,1)
    plt.scatter(y,x, color = 'blue', marker = '^', s = 12,)
    plt.subplot(2,2,3)
    plt.scatter(x,y, color='Hotpink', marker = '*', s = 12)
    plt.grid(color = 'g',ls=':',lw = 0.9)
    plt.show()

if __name__ == "__main__":
    x, y = random()
    print("Values of X: ", x)
    print("Values of Y: ",y)
    Dot(x,y)

    
    
