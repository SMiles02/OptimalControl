import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# --- Resource Allocation using Pontryagin's Maximum Principle ---

def objective(x, R):
    """
    The objective function to maximise.
    x[0] is the resource allocated to process 1, x[1] to process 2, x[2] to process 3.
    """
    process_1_output = np.sqrt(x[0])  # Process 1 benefit (concave function)
    process_2_output = np.log(1 + x[1])  # Process 2 benefit (diminishing returns)
    process_3_output = np.cbrt(x[2])  # Process 3 benefit (cube root function)
    
    return -(process_1_output + process_2_output + process_3_output)  # Negative for minimisation

def resource_constraint(x, R):
    """
    Ensures the sum of allocated resources is equal to the total available.
    """
    return np.sum(x) - R  # Ensuring the total sum does not exceed available resources

# --- Main optimisation function ---
def optimize_resource_allocation(R):
    """
    Optimises the resource allocation between three processes to maximise the total output.
    """
    # Initial guess (evenly distribute resources)
    initial_guess = [R / 3, R / 3, R / 3]
    
    # Constraints (total resource must sum to R)
    cons = ({'type': 'eq', 'fun': resource_constraint, 'args': (R,)})
    
    # Bounds for resource allocation (between 0 and R for each process)
    bounds = [(0, R), (0, R), (0, R)]
    
    # Minimise the negative of the objective (since we're maximising)
    result = minimize(objective, initial_guess, args=(R,), bounds=bounds, constraints=cons)
    
    # The optimal allocation
    optimal_allocation = result.x
    return optimal_allocation

# --- Example usage ---

R = 100  # Total resources available

# Find optimal allocation
optimal_allocation = optimize_resource_allocation(R)
print(f"Optimal allocation for Process 1: {optimal_allocation[0]:.2f}")
print(f"Optimal allocation for Process 2: {optimal_allocation[1]:.2f}")
print(f"Optimal allocation for Process 3: {optimal_allocation[2]:.2f}")

# Visualisation: How total output changes based on allocations to Process 1 and Process 2
allocations_p1 = np.linspace(0, R, 50)
allocations_p2 = np.linspace(0, R, 50)
X, Y = np.meshgrid(allocations_p1, allocations_p2)
Z = np.array([[np.sqrt(x) + np.log(1 + y) + np.cbrt(R - x - y) if x + y <= R else 0 for x in allocations_p1] for y in allocations_p2])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel("Resources to Process 1")
ax.set_ylabel("Resources to Process 2")
ax.set_zlabel("Total Output")
ax.set_title("Optimal Resource Allocation Surface")

plt.show()
