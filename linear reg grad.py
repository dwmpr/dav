import numpy as np
# Sample dataset
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 5, 4, 5], dtype=float)
# Hyperparameters
learning_rate = 0.01
epochs = 1000
# Initialize weights and bias
m = 0.0   # slope
b = 0.0   # intercept
n = len(X)
# Gradient Descent
for epoch in range(epochs):
    y_pred = m * X + b
    # Compute gradients
    dm = (-2/n) * np.sum(X * (y - y_pred))
    db = (-2/n) * np.sum(y - y_pred)
    # Update parameters
    m -= learning_rate * dm
    b -= learning_rate * db
    # Print loss every 200 epochs
    if epoch % 200 == 0:
        loss = np.mean((y - y_pred) ** 2)
        print(f"Epoch {epoch:4d} | Loss: {loss:.4f}")
# Final results
y_pred_final = m * X + b
mse = np.mean((y - y_pred_final) ** 2)
print("\n=== Final Results ===")
print(f"Slope (m)     : {m:.4f}")
print(f"Intercept (b) : {b:.4f}")
print(f"Mean Sq Error : {mse:.4f}")