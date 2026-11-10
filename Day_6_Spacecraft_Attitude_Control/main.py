import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


I = 8               # Moment of Inertia, kg * m ** 2
Kp = .8             # Proportional gain, N * m / rad
Kd = 4              # Derivative gain, N * m * s / rad
theta0 = 20         # Initial angular position, deg
omega0 = 0          # Initial angular velocity, rad / s
theta_target = 0    # Target angular position, deg
dt = .05            # Time step, s
duration = 60       # Duration, s

def deg_to_rad(theta):
    deg = theta
    rad = (deg / 180) * np.pi
    return rad

def control_torque(theta, omega, theta_target, Kp, Kd):
    torque = -1 * Kp * (theta - theta_target) - Kd * omega
    return torque
    
def simulate_attitude(theta0, omega0, theta_target, I, Kp, Kd, dt, duration):
    time = np.arange(0, duration + dt / 2, dt)
    torque = np.zeros(len(time))
    ang_pos = np.zeros(len(time))
    ang_vel = np.zeros(len(time))

    ang_pos[0] = theta0
    ang_vel[0] = omega0

    for i in range(len(time) - 1):
        tau = control_torque(ang_pos[i], ang_vel[i], theta_target, Kp, Kd)
        torque[i] = tau
        ang_pos[i + 1] = (
            ang_pos[i] + ang_vel[i] * dt
        )
        ang_vel[i + 1] = (
            ang_vel[i] + tau / I * dt
        )
    torque[-1] = control_torque(ang_pos[-1], ang_vel[-1], theta_target, Kp, Kd)


    results = {
        "time": time,
        "ang_pos": ang_pos,
        "ang_vel": ang_vel,
        "control_torque": torque
    }

    return results

def plot(results):
    plt.figure()
    plt.plot(results["time"], results["ang_pos"])
    plt.xlabel("Time (s)")
    plt.ylabel("Angular Position (rad)")
    plt.title("Angular Position vs. Time")
    plt.grid()
    folder = Path(__file__).resolve().parent
    plt.savefig(folder / "ang_pos_vs_time.png",
                dpi=300, bbox_inches="tight")
    plt.show()

    plt.figure()
    plt.plot(results["time"], results["ang_vel"])
    plt.xlabel("Time (s)")
    plt.ylabel("Angular Velocity (rad/s)")
    plt.title("Angular Velocity vs. Time")
    plt.grid()
    folder = Path(__file__).resolve().parent
    plt.savefig(folder / "ang_vel_vs_time.png",
                    dpi=300, bbox_inches="tight")
    plt.show()

theta0 = deg_to_rad(theta0)
theta_target = deg_to_rad(theta_target)

results = simulate_attitude(theta0, omega0, theta_target, I, Kp, Kd, dt, duration)
plot(results)

Kd_values = [0, 4, 8] 

def compare_controllers(theta0, omega0, theta_target, I, Kp, Kd_values, dt, duration):
    plt.figure()
    for k in Kd_values:
        results = simulate_attitude(theta0, omega0, theta_target, I, Kp, k, dt, duration)

        plt.plot(results["time"], results["ang_pos"], label = f"Kd = {k}")
    plt.xlabel("Time (s)")
    plt.ylabel("Angular Position (rad)")
    plt.title("Effect of Derivative Gain on Spacecraft Attitude")
    plt.legend()
    plt.grid()
    folder = Path(__file__).resolve().parent
    plt.savefig(folder / "controller_comparison.png", dpi=300, bbox_inches="tight")
    plt.show()

compare_controllers(theta0, omega0, theta_target, I, Kp, Kd_values, dt, duration)

assert np.isclose(results["ang_pos"][0], theta0)
assert np.isclose(results["ang_vel"][0], omega0)

test_results = simulate_attitude(0, 0, 0, I, Kp, Kd, dt, duration)

assert np.allclose(test_results["ang_pos"], 0)
assert np.allclose(test_results["ang_vel"], 0)    
print("All simulation tests passed")
    
    
