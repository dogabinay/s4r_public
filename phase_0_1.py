"""
Reactor Type: Batch. Contains solvers for the initial reaction terms only. No input/output.
Processes: 2 independent 1st order kinetic reactions. One for the Substrate (C), the other for Biomass (X).
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Initial Reactor Parameters
C_ini = 10000  # Initial COD in reactor, mg/L as COD
X_ini = 1000  # Initial biomass in reactor, mg/L as COD

# Process Parameters
k1 = 2
k2 = 0.2


# Model Function for dC/dt
def model_dcdt(c, t, k):
    dcdt = -k * c
    return dcdt


# Model Function for dX/dt
def model_dxdt(x, t, k):
    dxdt = k * x
    return dxdt


# Time Points
start = 0  # days
stop = 5  # days
num = 1001  # number of evenly spaced points between $start and $stop
t = np.linspace(start, stop, num)
print(t)

# Solve ODEs
graph_C = odeint(model_dcdt, C_ini, t, (k1,))
graph_X = odeint(model_dxdt, X_ini, t, (k2,))

# Plot Results
plt.plot(t, graph_C)
plt.xlabel('Time (day)')
plt.ylabel('COD (mg/L)')
plt.show()

plt.plot(t, graph_X)
plt.xlabel('Time (day)')
plt.ylabel('X_H (mg/L as COD)')
plt.show()

