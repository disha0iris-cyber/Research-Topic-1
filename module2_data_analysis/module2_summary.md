# Module 2 – Data Analysis and Observations

## What patterns exist in the data?

The traffic dataset shows clear time-based patterns. Demand is generally higher during peak 
hours and lower during off-peak periods. This indicates the presence of daily usage cycles 
that repeat over time.

## Time-of-day effects

Traffic demand increases significantly in the evening when user activity is higher. 
This behavior is consistent across multiple days and highlights the importance of 
time-aware allocation strategies.

## Service-specific behavior

Different services show different demand characteristics. Video traffic is more variable 
and experiences larger peaks. API traffic is more stable and predictable, while analytics 
workloads tend to be smoother and more flexible.

## What causes QoS violations?

QoS violations mainly occur when network resources are poorly allocated rather than when 
total capacity is insufficient. During high utilization periods, congestion increases and 
latency rises, leading to service degradation.

## How predictable is the demand?

Short-term demand is moderately predictable using simple forecasting methods. However, 
prediction accuracy decreases as the forecast horizon increases, especially during sudden 
traffic changes.

## Dataset limitations

The dataset is based on simulated traffic patterns and does not fully capture real-world 
effects such as unexpected failures, flash crowds, or external events. In real deployments, 
traffic behavior would be more noisy and less stable.
