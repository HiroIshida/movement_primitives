"""
======================
Spatial Scaling of DMP
======================

The standard DMP definition of Ijspeert et al. (2013) does not scale well,
when the original demonstration has both the start and the goal state close
together: small perturbation in the start and/or goal state often result in
large accelerations. '''To fix this issue, our implementation of the DMP does
not scale the forcing term by $(g - y_0)$!''' This example demonstrates the
behavior of this DMP implementation in these cases.
"""
import numpy as np
import matplotlib.pyplot as plt
from movement_primitives.dmp import DMP


T = np.linspace(0, 1, 101)
x = np.sin(T ** 2 * 1.99 * np.pi)
y = np.cos(T ** 2 * 1.99 * np.pi)
Y = np.column_stack((x, y))
start = Y[0]
goal = Y[-1]
new_goal = np.array([0.5, 0.5])
Y_shifted = Y - goal[np.newaxis] + new_goal[np.newaxis]

dmp = DMP(n_dims=len(start), execution_time=1.0, dt=0.01, n_weights_per_dim=20)
dmp.imitate(T, Y)
dmp.configure(goal_y=new_goal)
_, Y_dmp = dmp.open_loop()

plt.plot(Y[:, 0], Y[:, 1], label=r"Demonstration, $g \approx y_0$", ls="--")
plt.plot(Y_shifted[:, 0], Y_shifted[:, 1], label="Original shape with new goal", ls="--")
plt.plot(Y_dmp[:, 0], Y_dmp[:, 1], label="DMP with new goal", lw=5, alpha=0.5)
plt.scatter(start[0], start[1], c="r", label="Goal of demonstration: $g$")
plt.scatter(goal[0], goal[1], c="g", label="Start of demonstration: $y_0$")
plt.scatter(new_goal[0], new_goal[1], c="y", label="New goal: $g'$")
plt.xlabel("$y_1$")
plt.ylabel("$y_2$")
plt.legend(loc="best", ncol=2)
plt.xlim((-1.8, 2.1))
plt.ylim((-1.7, 2.2))
plt.tight_layout()
plt.show()