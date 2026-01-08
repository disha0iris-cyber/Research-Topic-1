import pandas as pd
import numpy as np

TOTAL_CAPACITY = 900

def load_data(path="network_simulated_data.csv"):
    return pd.read_csv(path)

def preprocess_data(df):
    df["network_utilization"] = df["total_network_demand"] / TOTAL_CAPACITY
    return df

def service_traffic_statistics(df):
    return df.groupby("service")["demand_mbps"].agg(
        mean_demand="mean",
        std_demand="std",
        min_demand="min",
        max_demand="max",
        p95_demand=lambda x: np.percentile(x, 95)
    )

def time_based_statistics(df):
    return df.groupby("hour")["total_network_demand"].mean()

def service_qos_violation_rate(df):
    return df.groupby("service")["qos_violated"].mean()

def latency_violation_rate(df):
    return df.groupby("service")["latency_violation"].mean()

def bandwidth_violation_rate(df):
    return df.groupby("service")["bandwidth_violation"].mean()

def utilization_threshold_analysis(df, threshold=0.7):
    high_util = df[df["network_utilization"] > threshold]
    low_util = df[df["network_utilization"] <= threshold]

    return {
        "high_util_violation_rate": high_util["qos_violated"].mean(),
        "low_util_violation_rate": low_util["qos_violated"].mean()
    }

def cost_analysis(df):
    return df.groupby("service").agg(
        avg_allocation_cost=("allocation_cost", "mean"),
        avg_violation_cost=("violation_cost", "mean"),
        total_cost=("total_cost", "sum")
    )

def priority_impact_analysis(df):
    return df.groupby("priority")["qos_violated"].mean()

def peak_hour_analysis(df):
    peak = df.loc[df["total_network_demand"].idxmax()]
    (service_peak, hour_peak, demand_peak) = (
        peak["service"],
        peak["hour"],
        peak["total_network_demand"]
    )
    return service_peak, hour_peak, demand_peak

def summary_report(df):
    return {
        "avg_utilization": df["network_utilization"].mean(),
        "max_utilization": df["network_utilization"].max(),
        "overall_violation_rate": df["qos_violated"].mean(),
        "total_operational_cost": df["total_cost"].sum()
    }

if __name__ == "__main__":
    df = preprocess_data(load_data())

    print("\nService Traffic Statistics")
    print(service_traffic_statistics(df))

    print("\nHourly Traffic Pattern")
    print(time_based_statistics(df))

    print("\nQoS Violation Rate per Service")
    print(service_qos_violation_rate(df))

    print("\nLatency Violation Rate")
    print(latency_violation_rate(df))

    print("\nBandwidth Violation Rate")
    print(bandwidth_violation_rate(df))

    print("\nUtilization Threshold Analysis")
    print(utilization_threshold_analysis(df))

    print("\nCost Analysis")
    print(cost_analysis(df))

    print("\nPriority Impact Analysis")
    print(priority_impact_analysis(df))

    print("\nPeak Hour Analysis")
    print(peak_hour_analysis(df))

    print("\nSummary Report")
    print(summary_report(df))



The data.py module provides a complete statistical and exploratory analysis of the simulated network traffic dataset.

The results confirm that network traffic is heterogeneous, time-varying, and uncertain. Video services dominate bandwidth usage and exhibit high variance, while API and analytics traffic show different stability and burstiness characteristics.

The analysis also reveals that QoS violations increase significantly when network utilization grows, confirming that performance degradation is not linear.

These findings justify the need for predictive and robust resource allocation mechanisms, forming the analytical foundation of the proposed solution.
