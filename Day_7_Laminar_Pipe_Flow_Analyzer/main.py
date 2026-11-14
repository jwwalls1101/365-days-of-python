import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

folder = Path(__file__).resolve().parent

R = .04 # Pipe radius (m)
U_max = 1.8 # Maximum Velocity (m/s)
n_values = 11 # Number of Points
rs = np.linspace(0, R, n_values)


def velocity_profile(rs, R, U_max):
    vel = U_max * (1 - ((rs ** 2) / (R ** 2)))
    return vel

vel = velocity_profile(rs, R, U_max)

plt.plot(rs, vel)
plt.xlabel("Radial Position (m)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity Profile across different radii")
plt.grid()
plt.savefig(folder / "velocity_profile.png", dpi = 300, bbox_inches = "tight")
plt.show()

assert np.isclose(vel[0], U_max)
assert np.isclose(vel[-1], 0)

def calculate_volumetric_flow_rate(vel, r):
    integral = np.trapezoid((vel * r), r)
    Q = 2 * np.pi * integral
    return Q

def calc_error(U_max, R, Q):
    Q_exact = (np.pi * (R ** 2) * U_max) / 2
    error = np.abs(((Q - Q_exact) / Q_exact) * 100)
    return error

new_values = [11, 21, 51, 101, 201]
errors = []

for n in new_values:
    rs = np.linspace(0, R, n)
    vel = velocity_profile(rs, R, U_max)
    Q = calculate_volumetric_flow_rate(vel, rs)
    error = calc_error(U_max, R, Q)
    errors.append(error)

def plot_error(error, points):
    plt.plot(points, error)
    plt.xlabel("Number of Points")
    plt.ylabel("Percentage Error")
    plt.title("Percentage Error vs. Number of Points")
    plt.grid()
    plt.savefig(folder / "grid_convergence.png", dpi = 300, bbox_inches = "tight")
    plt.show()

plot_error(errors, new_values)


