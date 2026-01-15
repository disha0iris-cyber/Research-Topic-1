Module 3 – Simple Forecasting Example

This script provides a basic example of network traffic demand forecasting
using a moving average approach. The purpose of this implementation is to
analyze prediction errors and understand uncertainty in demand estimation,
rather than achieving high prediction accuracy.

The prediction error bounds computed in this script are later used to define
uncertainty sets in the robust optimization model (Module 4).
"""


import pandas as pd
import numpy as np

# -----------------------------------------
# Simple example of demand forecasting
# using a Moving Average approach
# -----------------------------------------

# Simulated hourly demand for a video service (Mbps)
demand = [80, 75, 70, 65, 60, 55, 60, 70,
          90, 110, 130, 150, 160, 155,
          140, 130, 120, 110, 100, 95,
          90, 85, 80, 75]

data = pd.DataFrame({
    "hour": range(len(demand)),
    "actual_demand": demand
})

# -----------------------------------------
# Moving Average Forecast (baseline method)
# -----------------------------------------
window_size = 3
data["forecast"] = data["actual_demand"].rolling(window_size).mean()

# Remove first rows where forecast is not available
data = data.dropna()

# -----------------------------------------
# Forecast error analysis
# -----------------------------------------
data["error"] = data["actual_demand"] - data["forecast"]

mae = np.mean(np.abs(data["error"]))
rmse = np.sqrt(np.mean(data["error"] ** 2))

print("Mean Absolute Error (MAE):", round(mae, 2))
print("Root Mean Squared Error (RMSE):", round(rmse, 2))

# -----------------------------------------
# Simple uncertainty estimation
# These bounds will be used in Module 4
# -----------------------------------------
lower_error = data["error"].quantile(0.05)
upper_error = data["error"].quantile(0.95)

print("Estimated uncertainty bounds:")
print("Lower bound:", round(lower_error, 2))
print("Upper bound:", round(upper_error, 2))
