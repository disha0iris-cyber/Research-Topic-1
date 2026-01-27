MODULE 4– Robust Optimization Model
Questions & Answers


1. How do you formulate the allocation problem?
• Decision variables
Bandwidth allocated to each service.
• Objective function
Minimize total allocation cost and QoS violation penalties.
• Constraints
Capacity limits, QoS requirements, and non-negativity constraints.
2. How do you model uncertainty?
• Uncertain parameters
Future service demand.
• Uncertainty set
A box uncertainty set is used due to its simplicity and tractability.
• Sizing the uncertainty set
Bounds are derived from ML prediction error statistics.
3. How do you solve the robust problem?
• Tractable reformulation
The min–max problem is reformulated into a linear program.
• Solver
CVXPY is used as the optimization solver.
• Computational complexity
The problem remains computationally efficient and solvable in polynomial time.
4. What is the robustness–efficiency trade-off?
• Effect of Γ on cost
Higher Γ increases conservatism and allocation cost.

• Effect on violation rate
Increasing Γ significantly reduces QoS violations.
• Choosing Γ
Γ is selected by balancing acceptable cost increases against required robustness guarantees.



