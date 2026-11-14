import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

R = 6378.137 # Earth's radius (km)
mu = 398600.4 # Earth's Gravitational Parameter (km^3/s^2)
h = 600 # Altitude (km)
e = 0 # Eccentricity
theta0 = 0 # Initial True Anomaly (rad)
q = 1001 # Time samples

r = R + h
n = np.sqrt(mu / (r ** 3))
T = (2 * np.pi) / n

def spacecraft_position(r, theta0, T, q, n):
    x_pos = []
    y_pos = []
    eclipse_x = []
    eclipse_y = []
    eclipse_times = []
    time = np.linspace(0, T, q)
    for t in time:
        theta = theta0 + n * t
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        x_pos.append(x)
        y_pos.append(y)
        
        if x < 0 and np.abs(y) < R:
            eclipse_times.append(t)
            eclipse_x.append(x)
            eclipse_y.append(y)

    return x_pos, y_pos, eclipse_x, eclipse_y, eclipse_times


def plot_position(x, y, e_x, e_y):

    plt.plot(x, y, label = "Orbit")
    plt.plot(e_x, e_y, label = "In eclipse", color="red")
    plt.xlabel("X position")
    plt.ylabel("Y position")
    plt.title("Eclipse")
    plt.axis("equal")
    plt.legend(loc = "upper right")
    plt.grid()
    folder = Path(__file__).resolve().parent
    plt.savefig(folder / "orbit_eclipse.png", dpi = 300, bbox_inches = "tight")
    plt.show()

def eclipse_time(time, T):
    entry = time[0]
    exit = time[-1]
    duration = exit - entry
    percentage = (duration / T) * 100
    results = {
        "Eclipse Entry Time": float(entry),
        "Eclipse Exit Time": float(exit),
        "Duration of Eclipse": float(duration),
        "Percentage Spent in Eclipse": float(percentage)
    }

    return results

x_pos, y_pos, e_x, e_y, e_time = spacecraft_position(r, theta0, T, q, n)
plot_position(x_pos, y_pos, e_x, e_y)
print(eclipse_time(e_time, T))



