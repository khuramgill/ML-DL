import matplotlib.pyplot as plt
import numpy as np


def ThreeM_Var(arr):
    x = np.mean(arr)
    y = np.median(arr)
    z = np.std(arr)
    v = np.var(arr)
    return x, y, z, v

def Percentile(Arr , x):
    p = np.percentile(Arr, x)
    return p


if __name__ == "__main__":
    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
    mean_speed, median_speed, std_speed, var_speed = ThreeM_Var(speed)
    percentile_ages = Percentile(ages, 75)
    
    # Print results
    print(f"Mean of speed: {mean_speed}")
    print(f"Median of speed: {median_speed}")
    print(f"Standard Deviation of speed: {std_speed}")
    print(f"Variance of speed: {var_speed}")
    print(f"75th Percentile of ages: {percentile_ages}")

    # Prepare data for plotting
    labels = ['Mean', 'Median', 'Standard Deviation', 'Variance', '75th Percentile (Ages)']
    values = [mean_speed, median_speed, std_speed, var_speed, percentile_ages]

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color=['blue', 'green', 'red', 'purple', 'orange'])
    
    # Customize the plot
    plt.title('Statistical Measures of Speed and Percentile of Ages')
    plt.ylabel('Values')
    plt.grid(True)
    
    # Display the plot
    plt.show()
    

