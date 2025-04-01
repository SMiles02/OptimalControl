import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# --- Brachistochrone Problem ---

def brachistochrone(theta):
    """Computes the time for a particle to slide along a curve."""
    g = 9.81  # Gravity (m/s^2)
    x, y = np.cumsum(np.cos(theta)), np.cumsum(np.sin(theta))
    
    ds = np.sqrt(np.diff(x)**2 + np.diff(y)**2)  # Arc length
    v = np.sqrt(2 * g * np.abs(y[:-1]))  # Velocity from energy conservation
    dt = ds / v  # Time step
    return np.sum(dt)

# Solve for optimal angles
theta_guess = np.linspace(-np.pi / 4, -np.pi / 2, 50)
result = minimize(brachistochrone, theta_guess)

# Plot Brachistochrone curve
theta_opt = result.x
x_opt, y_opt = np.cumsum(np.cos(theta_opt)), np.cumsum(np.sin(theta_opt))
plt.figure()
plt.plot(x_opt, -y_opt, label="Brachistochrone Path")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Optimal Brachistochrone Curve")
plt.legend()
plt.show()
