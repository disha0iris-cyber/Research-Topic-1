# Module 1 – Problem Domain Overview

## Why is network traffic unpredictable?

Network traffic is highly dynamic because user behavior and application usage change over time. 
Traffic demand is affected by peak usage hours, sudden events, and different service requirements. 
As a result, demand is not constant and can vary significantly during the day.

## What causes demand spikes?

Demand spikes usually occur during peak hours (for example in the evening), live events, or periods 
of high user activity. These spikes are difficult to predict accurately and often exceed average 
traffic levels.

## How do different services behave?

Different services have different traffic patterns. Video streaming typically requires high bandwidth 
and shows strong variability. API services are more stable and predictable, while analytics workloads 
are more flexible and can tolerate delays.

## What are the consequences of poor resource allocation?

Poor allocation can lead to high latency, packet loss, and Quality of Service (QoS) violations. 
When network utilization becomes too high, congestion increases and performance degrades. 
This also increases operational costs due to penalty fees and service-level agreement violations.

## Why do traditional approaches fail?

Static allocation does not adapt to changing demand and often wastes resources. Reactive allocation 
responds only after problems occur, which is usually too late. Pure machine learning approaches depend 
on predictions that are not always accurate and provide no guarantees in worst-case scenarios.

## Why is robust optimization important?

Robust optimization addresses uncertainty by considering worst-case demand scenarios. Instead of 
optimizing only for average conditions, it provides safer allocation decisions that remain feasible 
even when predictions are inaccurate. This makes it suitable for real-world network management problems.
