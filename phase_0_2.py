"""
Reactor Type: Batch. Contains solvers for the initial reaction terms only. No input/output.
Processes: 2 dependent Monod-type reactions. One for the Substrate (S), the other for Biomass (X).
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Initial Reactor Parameters
S_ini = 10000  # Initial COD in reactor, mg/L as COD
X_ini = 1000  # Initial biomass in reactor, mg/L as COD

# Process Parameters
u_max_H = 4  # Maximum specific growth rate of heterotrophic microorgranisms, 1/d
b_H = 0.2  # Specific decay rate of heterotrophic microorgranisms, 1/d
K_s = 10  # Half saturation constant, mg/L as COD
Y = 0.63  # Yield constant, g COD / g COD


# Model Function
def model(x, t, u_max_H, b_H, K_s, Y):

    # State Variables
    S = x[0]
    X = x[1]

    dSdt = -(u_max_H / Y) * (S / (K_s + S)) * X
    dXdt = (u_max_H * (S / (K_s + S)) - b_H) * X
    return [dSdt, dXdt]


# Time Steps
start = 0  # day
end = 4  # day
step = 1001

t = np.linspace(start, end, step)

# Initial Conditions
x = [S_ini, X_ini]

# Solve ODEs
solution1 = odeint(model, x, t, (1, b_H, K_s, Y))
solution2 = odeint(model, x, t, (2, b_H, K_s, Y))
solution3 = odeint(model, x, t, (0.5, b_H, K_s, Y))
solution4 = odeint(model, x, t, (4, b_H, K_s, Y))

# Assign Results
S1 = solution1[:, 0]
X1 = solution1[:, 1]
S2 = solution2[:, 0]
X2 = solution2[:, 1]
S3 = solution3[:, 0]
X3 = solution3[:, 1]
S4 = solution4[:, 0]
X4 = solution4[:, 1]

# Plot Results
plt.plot(t,S3,'g:',linewidth=2,label='u_max = 0.5')
plt.plot(t,S1,'r-',linewidth=2,label='u_max = 1')
plt.plot(t,S2,'b--',linewidth=2,label='u_max = 2')
plt.plot(t,S4,'-',linewidth=2,label='u_max = 4')
plt.xlabel('Time (day)')
plt.ylabel('COD (mg/L as COD)')
plt.legend()
plt.show()

plt.plot(t,X3,'g:',linewidth=2,label='u_max = 0.5')
plt.plot(t,X1,'r-',linewidth=2,label='u_max = 1')
plt.plot(t,X2,'b--',linewidth=2,label='u_max = 2')
plt.plot(t,X4,'-',linewidth=2,label='u_max = 4')
plt.xlabel('Time (day)')
plt.ylabel('X_H (mg/L as COD)')
plt.legend()
plt.show()

