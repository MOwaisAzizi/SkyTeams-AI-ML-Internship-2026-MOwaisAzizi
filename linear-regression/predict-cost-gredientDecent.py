import numpy as np

# -------------------------
# Training data
# -------------------------
x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([300.0, 500.0, 700.0, 900.0])

m = x.shape[0]  # number of training examples

# -------------------------
# Model: f(x) = w*x + b
# -------------------------
def predict(x, w, b):
    return w * x + b


# -------------------------
# Cost function (MSE / 2m)
# -------------------------
def compute_cost(x, y, w, b):
    cost_sum = 0
    for i in range(m):
        f_wb = predict(x[i], w, b)
        cost_sum += (f_wb - y[i]) ** 2

    total_cost = cost_sum / (2 * m)
    return total_cost


# -------------------------
# Gradient computation
# -------------------------
def compute_gradient(x, y, w, b):
    dj_dw = 0
    dj_db = 0

    for i in range(m):
        f_wb = predict(x[i], w, b)
        error = f_wb - y[i]

        dj_dw += error * x[i]
        dj_db += error

    dj_dw = dj_dw / m
    dj_db = dj_db / m

    return dj_dw, dj_db


# -------------------------
# Gradient Descent
# -------------------------
def gradient_descent(x, y, w, b, alpha, num_iters):
    J_history = []

    for i in range(num_iters):

        dj_dw, dj_db = compute_gradient(x, y, w, b)

        # update parameters
        w = w - alpha * dj_dw
        b = b - alpha * dj_db

        # save cost
        cost = compute_cost(x, y, w, b)
        J_history.append(cost)

        # print progress
        if i % 10 == 0:
            print(f"iter {i}: cost={cost:.4f}, w={w:.4f}, b={b:.4f}")

    return w, b, J_history


w_init = 0
b_init = 0
alpha = 0.01
iterations = 100

w_final, b_final, J_history = gradient_descent(
    x, y, w_init, b_init, alpha, iterations
)

print("\nFinal model:")
print("w =", w_final)
print("b =", b_final)

# -------------------------
# Test prediction
# -------------------------
x_test = 5
print("\nPrediction for x=5:", predict(x_test, w_final, b_final))
