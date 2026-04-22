import numpy as np

# Sample dataset (X: input, Y: output)
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 5, 4, 5])

# Initialize parameters
m = 0  # slope
b = 0  # intercept
learning_rate = 0.01
epochs = 1000
n = len(X)

# Gradient Descent
for i in range(epochs):
    Y_pred = m * X + b
    
    # Calculate gradients
    dm = (-2/n) * sum(X * (Y - Y_pred))
    db = (-2/n) * sum(Y - Y_pred)
    
    # Update parameters
    m = m - learning_rate * dm
    b = b - learning_rate * db

# Final error
error = sum((Y - (m * X + b))**2) / n

print("Final Slope (m):", m)
print("Final Intercept (b):", b)
print("Error:", error)
