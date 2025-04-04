# Brachistochrone Problem

## Overview
The **Brachistochrone problem** asks: _What is the fastest path for a particle to travel between two points under gravity?_  
Surprisingly, the shortest path (a straight line) is not the fastest—the optimal path is a **cycloid**, a curve that minimises descent time.

## Mathematical Formulation
Using energy conservation, the velocity of the particle at any height `y` is:

v = sqrt(2 * g * |y|)


The total travel time along a curve `(x(t), y(t))` is given by:

T = ∫ (ds / v)


where `ds` is the infinitesimal arc length.

## Implementation
Our numerical solution approximates the Brachistochrone curve using discrete **angle segments** (θ), solving for the optimal angles that minimize descent time.

- We define the path using cumulative sums of `cos(θ)` and `sin(θ)`.
- Using energy principles, we compute velocity and arc length at each step.
- The total descent time is minimized using `scipy.optimize.minimize`.

## Running the Code
To generate the optimal path, run:

```sh
python brachistochrone.py
```

# Rocket Launch Fuel Minimisation

This section of the project demonstrates the application of optimal control theory to minimise fuel usage during a rocket launch. The problem involves determining the optimal thrust profile for a rocket under the influence of gravity, which would minimise fuel consumption while ensuring the rocket reaches the desired altitude within a given time frame.

## Problem Setup
The rocket dynamics are simulated using the following key assumptions:
- The rocket's mass decreases as fuel is consumed.
- The rocket experiences a constant gravitational force during ascent.
- The thrust generated by the rocket is the control input, which influences the rocket's velocity and altitude over time.

## Code Overview
The main components of the code include:
- **Rocket Dynamics Simulation**: This function simulates the rocket's ascent under the control of an optimal thrust profile. It integrates the rocket's dynamics over discrete time steps, updating the rocket's altitude, velocity, and mass at each step.
  
- **Cost Function**: The objective of the optimisation is to minimise the total thrust used during the ascent. This cost function returns the sum of the thrust applied over the entire duration, which the optimiser seeks to minimise.

- **Optimisation**: Using the `scipy.optimize.minimise` function, the optimal thrust profile is computed over a fixed time horizon, subject to the constraint that the thrust must be within a specific range. The result is an optimised trajectory that minimises fuel usage.

## Results and Visualisation
The optimal altitude profile is plotted as a function of time, showing how the rocket's height changes during the ascent. By minimising the thrust applied throughout the ascent, the fuel usage is reduced while still ensuring the rocket reaches the desired altitude.

This approach ties into the broader goals of the *Optimal Control and Backpropagation* project, where we explore how optimal control theory can be used to solve real-world problems. In this case, the goal is to minimise fuel consumption in rocket launches, which is analogous to the underlying principles of optimising a system's performance subject to constraints.

## Running the Code
To generate the optimal path, run:

```sh
python rocket_launch_opt.py
```

# Optimal Resource Allocation

This implementation solves a **resource allocation problem** using **Pontryagin’s Maximum Principle** and numerical optimisation techniques. Given a fixed total amount of resources, we optimise how they should be distributed among **three competing processes**, each with different efficiency functions:  

- **Process 1**: Diminishing returns modelled by a square root function.  
- **Process 2**: Rapid early gains, then slowing, modelled by a logarithmic function.  
- **Process 3**: Slower but steady growth, modelled by a cube root function.  

## Methodology 
The problem is formulated as a constrained optimisation task:  

Maximise: sqrt(x1) + log(1 + x2) + cbrt(x3) Subject to: x1 + x2 + x3 = R

where `R` is the total available resource.  

We use **SciPy’s `minimize` function** with equality constraints to find the optimal allocation. The result is visualised with a **3D surface plot**, showing how different allocations affect total output.  

## Results
For `R = 100`, a sample output might be:  

Optimal allocation for Process 1: 40.32
Optimal allocation for Process 2: 20.15
Optimal allocation for Process 3: 39.53


## running the Code 
Run the script to compute the optimal allocation:  

```sh
python resource_allocation.py
```

This will output the best allocation strategy and generate a 3D plot illustrating the solution space.