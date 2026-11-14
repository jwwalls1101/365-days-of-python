
import numpy as np
import matplotlib.pyplot as plt

mu = 398600.4  # Gravitational Parameter of Earth (km^3/s^2)
Re = 6378.14   # Radius of Earth (km)
h0 = 500       # Initial Altitude (km)
dt = 10        # Time Step (s)
duration = 6000  # Duration (s)
r0 = np.array([Re + h0, 0, 0])  # Initial Position (km)
v0 = np.array([0, 7.4, 2.4])    # Initial Velocity (km/s)
initial_state = np.concatenate((r0, v0))

def orbital_dynamics(state, mu):
    position = state[:3]
    velocity = state[3:]
    r = np.linalg.norm(position)

    acceleration = -mu * position / r**3
    
    state_derivative = np.concatenate((velocity, acceleration))

    return state_derivative


def propagate_orbit(initial_state, mu, dt, duration):
    time = np.arange(0, duration + dt, dt)
    states = np.zeros((len(time), 6))
    states[0] = initial_state

    for i in range(len(time) - 1):
        state_derivative = orbital_dynamics(states[i], mu)
        states[i + 1] = states[i] + state_derivative * dt

    return states, time


def plot_orbit(states, time):
    positions = states[:, :3]
    velocities = states[:, 3:]

    plt.figure()
    plt.plot(time, positions[:, 0], label="X Position")
    plt.plot(time, positions[:, 1], label="Y Position")
    plt.plot(time, positions[:, 2], label="Z Position")

    plt.xlabel("Time (s)")
    plt.ylabel("Position (km)")
    plt.title("Spacecraft Position vs. Time")
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure()
    plt.plot(time, velocities[:, 0], label="X Velocity")
    plt.plot(time, velocities[:, 1], label="Y Velocity")
    plt.plot(time, velocities[:, 2], label="Z Velocity")

    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (km/s)")
    plt.title("Spacecraft Velocity vs. Time")
    plt.legend()
    plt.grid()
    plt.show()

states, time = propagate_orbit(initial_state, mu, dt, duration)
print("Time array shape:", time.shape)
print("State history shape:", states.shape)
plot_orbit(states, time)
