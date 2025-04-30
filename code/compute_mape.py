import numpy as np

# Fill in with corresponding values 
    # y_true: correct outputs
    # y_pred: model predictions
y_true = np.array([1800, 70640, 14836, 220295, 1434, 65455, 5683, 207722, 27181, 31200, 18000])  
y_pred = np.array([2000, 12944.38, 3982, 35335, 1695.55, 9913, 3452.52, 28923, 1626, 32000, 6300])

# Filter out zero values in y_true (avoid division by 0)
nonzero_indices = y_true != 0
y_true_filtered = y_true[nonzero_indices]
y_pred_filtered = y_pred[nonzero_indices]

mape = np.mean(np.abs((y_true_filtered - y_pred_filtered) / y_true_filtered)) * 100

print("MAPE:", mape, "%")