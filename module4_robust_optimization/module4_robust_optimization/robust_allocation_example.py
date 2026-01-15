"""
Module 4 – Robust Optimization Example

This script demonstrates a simple robust bandwidth allocation problem.
The demand value used here is obtained from a forecasting model (Module 3)
and includes uncertainty due to prediction errors.

Uncertainty is modeled using upper and lower bounds derived from the
forecasting error. A robustness parameter (Gamma) is used to control how
conservative the allocation is. Higher Gamma values provide more protection
against worst-case demand but result in higher allocation cost.

The goal is to allocate bandwidth in a way that remains feasible even when
actual demand deviates from predictions.
"""

import cvxpy as cp

# -----------------------------------------
# Problem parameters
# -----------------------------------------

# Total available network capacity (Mbps)
total_capacity = 300

# Predicted demand from Module 3 (example value)
predicted_demand = 150

# Prediction error bounds from Module 3
error_lower = -15
error_upper = 20

# Robustness parameter (0 <= Gamma <= 1)
Gamma = 0.7

# Worst-case demand estimation
worst_case_demand = predicted_demand + Gamma * error_upper

# -----------------------------------------
# Decision variable
# x represents allocated bandwidth
# -----------------------------------------
x = cp.Variable()

# -----------------------------------------
# Objective function
# Minimize allocated bandwidth (cost proxy)
# -----------------------------------------
objective = cp.Minimize(x)

# -----------------------------------------
# Constraints
# -----------------------------------------
constraints = [
    x >= worst_case_demand,   # robust demand satisfaction
    x <= total_capacity,      # capacity limit
    x >= 0                    # non-negativity
]

# -----------------------------------------
# Solve the optimization problem
# -----------------------------------------
problem = cp.Problem(objective, constraints)
problem.solve()

# -----------------------------------------
# Output results
# -----------------------------------------
print("Robust allocation results")
print("--------------------------")
print("Allocated bandwidth:", round(x.value, 2))
print("Worst-case demand covered:", round(worst_case_demand, 2))
print("Gamma value:", Gamma)

