import numpy as np
from scipy.optimize import minimize
import math
import matplotlib.pyplot as plt
import pandas as pd

# NumPy example
print("NumPy Example:")
arr = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(arr)
print(f"Mean: {mean_value}")

# SciPy example
print("\nSciPy Example:")
def objective_function(x):
    return x**2 + 5*x + 6

result = minimize(objective_function, x0=0)
print(result)

# Math module example
print("\nMath Module Example:")
print(f"Square root: {math.sqrt(25)}")
print(f"Sine of 30 degrees: {math.sin(math.radians(30))}")

# Matplotlib example
print("\nMatplotlib Example:")
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave Plot')
plt.show()

# Pandas example
print("\nPandas Example:")
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}

df = pd.DataFrame(data)
print(df)
