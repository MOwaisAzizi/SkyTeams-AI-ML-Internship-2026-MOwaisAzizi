import numpy as np
import math

# Simple mean function
def mean(data, col):
    total = 0
    for row in range(len(data)):
        total += data[row][col]
    return total / len(data)

# Simple standard deviation function (like your example)
def std(data, col, mean_val):
    variance = 0
    for row in range(len(data)):
        variance += (data[row][col] - mean_val) ** 2
    variance = variance / len(data)
    return math.sqrt(variance)

# Simple normalization
def normalize(X):
    rows = len(X)
    cols = len(X[0])
    normalized = []
    
    for row in range(rows):
        new_row = []
        for col in range(cols):
            mean_val = mean(X, col)
            std_val = std(X, col, mean_val)
            norm_val = (X[row][col] - mean_val) / std_val
            new_row.append(norm_val)
        normalized.append(new_row)
    
    return normalized

# Run it
result = normalize(X)
# Training Data
# =========================
X = np.array([
    [2104, 5, 1, 45],
    [1416, 3, 2, 40],
    [852,  2, 1, 35]
])

# Prices
y = np.array([460, 232, 178])

number_training_examples = X.shape[0]   # number of training examples
number_features = X.shape[1]   # number of features

# =========================
# Feature Scaling
# =========================

X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X_norm = (X - X_mean) / X_std

# =========================
# Initialize Parameters
# =========================
w = np.zeros(number_features)
b = 0
alpha = 0.01
iterations = 1000

# =========================
# Cost Function
# =========================

def compute_cost(X, y, w, b):
    m = X.shape[0]

    predictions = X @ w + b

    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)

    return cost

# =========================
# Gradient Descent
# =========================

def gradient_descent(X, y, w, b, alpha, iterations):

    m = X.shape[0]

    for i in range(iterations):

        predictions = X @ w + b

        error = predictions - y

        # Derivatives
        dj_dw = (1 / m) * (X.T @ error)
        dj_db = (1 / m) * np.sum(error)

        # Update parameters
        w = w - alpha * dj_dw
        b = b - alpha * dj_db

        # Print cost every 100 iterations
        if i % 100 == 0:
            cost = compute_cost(X, y, w, b)
            print(f"Iteration {i}: Cost = {cost:.2f}")

    return w, b

# =========================
# Train Model
# =========================

initial_cost = compute_cost(X_norm, y, w, b)

print("Initial Cost:", initial_cost)

w, b = gradient_descent(X_norm, y, w, b, alpha, iterations)

final_cost = compute_cost(X_norm, y, w, b)

print("\nFinal Cost:", final_cost)

# =========================
# Prediction
# =========================

# New house:
# 2000 sqft, 4 bedrooms, 1 floor, 30 years old

new_house = np.array([2000, 4, 1, 30], dtype=float)

# Normalize using training mean/std
new_house_norm = (new_house - X_mean) / X_std

predicted_price = np.dot(new_house_norm, w) + b

print("\nPredicted Price:", predicted_price, "thousand dollars")