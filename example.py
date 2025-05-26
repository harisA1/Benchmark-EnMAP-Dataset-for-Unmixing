import numpy as np
data = np.load("benchmark_dataset.npz")
X = data["image"]              # shape (N, B)
y = data["ground_truth"]       # shape (N,3)
H = int(data["height"])
W = int(data["width"])

# Optional: reshape to 3D if needed
X_image = X.reshape(H, W, -1)
y_image = y.reshape(H, W, -1)