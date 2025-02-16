
# TASK: Create a scatter plot with x = [1, 2, 3, 4, 5] and y = [2, 4, 6, 8, 10].
# Annotate each point with its (x, y) value, and set the title as 'Scatter Plot with Annotations'.
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the scatter plot
plt.scatter(x, y, color='blue')

# Annotate each point
for i in range(len(x)):
    plt.text(x[i], y[i], f'({x[i]}, {y[i]})', fontsize=12, ha='right')

# Customization
plt.title('Scatter Plot with Annotations')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.grid(True)

# Show the scatter plot
plt.show()



