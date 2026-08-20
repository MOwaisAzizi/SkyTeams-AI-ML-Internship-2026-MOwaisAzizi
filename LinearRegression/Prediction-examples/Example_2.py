import numpy as np
import math

# =========================
# HELPER FUNCTIONS
# =========================

def calculate_mean(data, column_index):
    """Calculate mean of a specific column"""
    total = 0
    for row in range(len(data)):
        total += data[row][column_index]
    return total / len(data)

def calculate_std(data, column_index, mean_value):
    """Calculate standard deviation of a specific column"""
    variance = 0
    for row in range(len(data)):
        variance += (data[row][column_index] - mean_value) ** 2
    variance = variance / len(data)
    return math.sqrt(variance)

def normalize_data(X):
    """Normalize all features using z-score normalization"""
    rows = len(X)
    cols = len(X[0])
    normalized_matrix = []
    
    for row in range(rows):
        new_row = []
        for col in range(cols):
            mean_val = calculate_mean(X, col)
            std_val = calculate_std(X, col, mean_val)
            norm_val = (X[row][col] - mean_val) / std_val
            new_row.append(norm_val)
        normalized_matrix.append(new_row)
    
    return normalized_matrix

# =========================
# LOAD AND PREPARE DATA
# =========================

# Training features
X = np.array([
    [2104, 5, 1, 45],
    [1416, 3, 2, 40],
    [852,  2, 1, 35]
])

# Target prices (in thousands)
y = np.array([460, 232, 178])

# Data dimensions
num_training_examples = X.shape[0]  # Number of training examples (m)
num_features = X.shape[1]            # Number of features (n)

# Normalize features
X_normalized = normalize_data(X)

# Calculate mean and std for future predictions (using original X)
X_mean = np.zeros(num_features)
X_std = np.zeros(num_features)
for col in range(num_features):
    X_mean[col] = calculate_mean(X, col)
    X_std[col] = calculate_std(X, col, X_mean[col])

# =========================
# INITIALIZE PARAMETERS
# =========================

weights = np.zeros(num_features)  # Initialize weights to 0
bias = 0                          # Initialize bias to 0
learning_rate = 0.01
num_iterations = 1000

# =========================
# MODEL FUNCTIONS
# =========================

def predict(X, weights, bias):
    """Make predictions using linear regression"""
    predictions = []
    for row in range(len(X)):
        current_prediction = 0
        for col in range(len(X[row])):
            current_prediction += weights[col] * X[row][col]
        current_prediction += bias
        predictions.append(current_prediction)
    return predictions

def compute_cost(X, weights, bias, y):
    """Calculate mean squared error cost"""
    m = len(y)
    predictions = predict(X, weights, bias)  # Fixed: renamed variable to avoid conflict
    
    total_cost = 0
    for i in range(m):
        total_cost += (predictions[i] - y[i]) ** 2
    
    total_cost = total_cost / (2 * m)
    return total_cost

def compute_weight_derivative(X, weights, y, bias, feature_index):
    """Calculate derivative for a specific weight"""
    predictions = predict(X, weights, bias)
    error_sum = 0
    
    for i in range(len(y)):
        error_sum += (predictions[i] - y[i]) * X[i][feature_index]  # Fixed: predictions - y
    
    derivative = error_sum / len(y)
    return derivative

def compute_bias_derivative(X, weights, y, bias):
    """Calculate derivative for bias"""
    predictions = predict(X, weights, bias)
    error_sum = 0
    
    for i in range(len(y)):
        error_sum += (predictions[i] - y[i])  # Removed X[i][col_index]
    
    derivative = error_sum / len(y)
    return derivative

def gradient_descent(X, y, weights, bias, learning_rate, num_iterations):
    """Perform gradient descent to optimize parameters"""
    num_features = len(weights)
    
    for iteration in range(num_iterations):
        new_weights = []
        
        # Update all weights
        for feature_idx in range(num_features):
            weight_derivative = compute_weight_derivative(X, weights, y, bias, feature_idx)
            new_weight = weights[feature_idx] - learning_rate * weight_derivative
            new_weights.append(new_weight)
        
        # Update bias
        bias_derivative = compute_bias_derivative(X, weights, y, bias)
        new_bias = bias - learning_rate * bias_derivative
        
        # Simultaneous update
        weights = new_weights
        bias = new_bias
        
        # Print progress every 100 iterations
        if iteration % 100 == 0:
            current_cost = compute_cost(X, weights, bias, y)
            print(f"Iteration {iteration}, Cost: {current_cost:.4f}")
    
    return weights, bias

# =========================
# TRAIN MODEL
# =========================

print("=" * 50)
print("TRAINING LINEAR REGRESSION MODEL")
print("=" * 50)

# Calculate initial cost
initial_cost = compute_cost(X_normalized, weights, bias, y)
print(f"Initial Cost: {initial_cost:.4f}")

# Train the model
trained_weights, trained_bias = gradient_descent(
    X_normalized, y, weights, bias, learning_rate, num_iterations
)

# Calculate final cost
final_cost = compute_cost(X_normalized, trained_weights, trained_bias, y)
print(f"\nFinal Cost: {final_cost:.4f}")

# Display trained parameters
print("\nTrained Parameters:")
for i in range(num_features):
    print(f"  Weight {i}: {trained_weights[i]:.4f}")
print(f"  Bias: {trained_bias:.4f}")

# =========================
# MAKE PREDICTIONS
# =========================

print("\n" + "=" * 50)
print("MAKING PREDICTIONS")
print("=" * 50)

# Predict on training data
training_predictions = predict(X_normalized, trained_weights, trained_bias)
print("\nTraining Data Predictions:")
for i in range(num_training_examples):
    print(f"  House {i+1}: Predicted={training_predictions[i]:.2f}, Actual={y[i]:.2f}")

# Predict for a new house
new_house = np.array([2000, 4, 1, 30], dtype=float)

# Normalize using training statistics
new_house_normalized = []
for col in range(num_features):
    norm_val = (new_house[col] - X_mean[col]) / X_std[col]
    new_house_normalized.append(norm_val)

# Make prediction
predicted_price = 0
for col in range(num_features):
    predicted_price += trained_weights[col] * new_house_normalized[col]
predicted_price += trained_bias

print(f"\nNew House Features: {new_house}")
print(f"Predicted Price: ${predicted_price:.2f} thousand dollars")
print(f"Predicted Price: ${predicted_price * 1000:.2f} dollars")