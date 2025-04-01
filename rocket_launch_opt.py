import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# --- Rocket Launch (Fuel Minimisation) ---

def rocket_dynamics(thrust, dt=0.1, T=10):
    """Simulates rocket ascent under gravity with optimal thrust."""
    g = 9.81  # Gravity (m/s^2)
    m0 = 500  # Initial mass (kg)
    ve = 3000 # Exhaust velocity (m/s)
    h, v, m = [0], [0], [m0]
    
    for t in range(len(thrust)):
        dm = -thrust[t] * dt / ve  # Mass loss
        dv = (thrust[t] / m[-1] - g) * dt  # Velocity change
        
        m.append(m[-1] + dm)
        v.append(v[-1] + dv)
        h.append(h[-1] + v[-1] * dt)
    
    return h, v, m

# Define cost function (minimise fuel usage)
def cost_function(thrust):
    return np.sum(thrust)  # Minimise total thrust usage

# Initial guess and constraints
T_steps = 100
thrust_guess = np.ones(T_steps) * 5000  # Initial thrust guess
bounds = [(0, 10000)] * T_steps
result = minimize(cost_function, thrust_guess, bounds=bounds)

# Solve for optimal trajectory
h_opt, v_opt, m_opt = rocket_dynamics(result.x)

# Plot results
plt.figure()
plt.plot(np.linspace(0, 10, len(h_opt)), h_opt, label="Altitude")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Optimal Rocket Trajectory")
plt.legend()
plt.show()
