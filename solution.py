import pandas as pd
from optimization import robust_allocation

TOTAL_CAPACITY = 900

def run_solution():
    df = pd.read_csv("network_simulated_data.csv")

    service_level = (
        df.groupby("service")
        .mean(numeric_only=True)
        .reset_index()
    )

    allocation = robust_allocation(service_level, uncertainty_factor=0.15)

    allocation["utilization"] = (
        allocation["allocated_mbps"].sum() / TOTAL_CAPACITY
    )

    allocation["bandwidth_gap"] = (
        allocation["demand_mbps"] - allocation["allocated_mbps"]
    )

    return allocation[[
        "service",
        "demand_mbps",
        "allocated_mbps",
        "bandwidth_gap",
        "utilization"
    ]]

if __name__ == "__main__":
    result = run_solution()
    print(result)


solution.py implements the final solution of the research project.
It applies a robust bandwidth allocation strategy using the simulated network traffic data.

The script reads the dataset, computes the average demand for each service, and allocates network resources while considering traffic uncertainty. The goal is to avoid network overload and reduce QoS violations under limited capacity.

When executed, the script produces:

a summary table showing the demand and allocated bandwidth for each service

a final graph comparing service demand with allocated bandwidth

This file serves as the main entry point of the project and demonstrates how robust optimization can be used to manage network traffic under uncertainty.
