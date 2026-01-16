import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------------------
# Simple visualization for Module 2
# Purpose: show basic time-of-day traffic pattern
# -----------------------------------------

# Simulated hourly traffic demand (example data)
traffic_demand = [80, 75, 70, 65, 60, 55, 60, 70,
                  90, 110, 130, 150, 160, 155,
                  140, 130, 120, 110, 100, 95,
                  90, 85, 80, 75]

data = pd.DataFrame({
    "hour": range(len(traffic_demand)),
    "demand": traffic_demand
})

# -----------------------------------------
# Plot traffic demand over time
# -----------------------------------------
plt.figure()
plt.plot(data["hour"], data["demand"])
plt.xlabel("Hour of Day")
plt.ylabel("Traffic Demand (Mbps)")
plt.title("Module 2: Traffic Demand Pattern Over Time")
plt.grid(True)
plt.show()


This visualization shows the variation of traffic demand over a 24-hour period. 
The figure highlights clear peak hours during the evening and lower demand during off-peak periods.
These time-based patterns motivate the need for time-aware forecasting and dynamic resource allocation strategies.
