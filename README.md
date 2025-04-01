## Brachistochrone Problem

### Overview
The **Brachistochrone problem** asks: _What is the fastest path for a particle to travel between two points under gravity?_ Surprisingly, the shortest path (a straight line) is not the fastest—the optimal path is a **cycloid**, a curve that minimises descent time.

### Mathematical Formulation
Using energy conservation, the velocity of the particle at any height \( y \) is:

\[
v = \sqrt{2 g |y|}
\]

The total travel time along a curve \( (x(t), y(t)) \) is given by:

\[
T = \int \frac{ds}{v}
\]

where \( ds \) is the infinitesimal arc length.

### Implementation
Our numerical solution approximates the Brachistochrone curve using discrete **angle segments** \( \theta \), solving for the optimal angles that minimise descent time.

- We define the path using cumulative sums of `cos(θ)` and `sin(θ)`.
- Using energy principles, we compute velocity and arc length at each step.
- The total descent time is minimised using `scipy.optimize.minimize`.

### Running the Code
To generate the optimal path, run:

```sh
python brachistochrone.py