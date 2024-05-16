import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create figure and axes
fig, ax = plt.subplots()

# Plot data on the first axes
ax.plot(x, y1, color='blue', label='sin(x)')
ax.plot(x, y2, color='red', linestyle='--', label='cos(x)')

# Set axis labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Trigonometric Functions')

# Add a legend
ax.legend()

# Create a second axes that shares the same x-axis
ax2 = ax.twinx()
y3 = np.exp(x / 10)
ax2.plot(x, y3, color='green', linestyle=':', label='exp(x/10)')
ax2.set_ylabel('Y-axis (exp)')

# Add a legend for the second axes
ax2.legend(loc='lower right')

# Add grid
ax.grid(True)

# Show plot
plt.show()
