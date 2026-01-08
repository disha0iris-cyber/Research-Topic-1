# Research-Topic-1
TOPIC 1: ML - Driven Network Resource Allocation with Robust Optimization




# ML-Driven Network Resource Allocation with Robust Optimization

This repository contains the implementation and analysis for the research topic
**ML-Driven Network Resource Allocation with Robust Optimization**.

The project studies how network bandwidth can be allocated among multiple
services under uncertain traffic demand, with the goal of reducing QoS
violations while keeping efficient use of network resources.

---

## Project Context

The research is based on a simulated cloud network with limited capacity and
heterogeneous services:
- Video services
- API services
- Analytics services

Traffic demand varies over time and cannot be predicted perfectly. Traditional
allocation methods and ML-based approaches without robustness may fail during
traffic spikes.

---

## Dataset

The file `network_simulated_data.csv` contains simulated network traffic data,
including:
- Service demand and allocated bandwidth
- Network utilization
- Latency and QoS violations
- Cost and priority information

The dataset is used for statistical analysis and evaluation of allocation
strategies.

---

## Code Structure

- `data.py`  
  Performs statistical analysis of network traffic and QoS behavior.

- `optimization.py`  
  Implements and compares baseline, nominal, and robust resource allocation
  strategies.

- `topic1.tex`  
  LaTeX document containing the theoretical background of the research.

- `RESEARCH_EXPLANATION.md`  
  Detailed explanation of the full research and methodology.

---

## Main Findings

- Network traffic is heterogeneous and uncertain
- Video services dominate bandwidth usage
- QoS violations increase with network utilization
- Robust optimization reduces QoS violations compared to nominal allocation

---
