# Solving linear systems with numpy

import numpy as np

state = np.array([7000, 0, 0, 7.5])

position = state[:2]
velocity = state[2:]

print("Position: ", position)
print("Velocity: ", velocity)

radius = np.linalg.norm(position)
speed = np.linalg.norm(velocity)

def dynamics(state):
    x, v = state

    acceleration = 2

    return np.array([v, acceleration])
