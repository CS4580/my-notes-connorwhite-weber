from number_of_digits import factorial_length as facL
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(1, 1500, 1500).astype(int)
y = []
for i in x:
  y.append(facL(x[i-1])/x[i-1])

y = np.array(y) * np.e
z = np.log(x)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot data
ax.plot(x, y)
ax.plot(x, z)
# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Sample Plot')

# Show plot
plt.show()