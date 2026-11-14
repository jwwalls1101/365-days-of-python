import numpy as np

temperatures = np.array([20, 25, 35, 45, 30, 15])
overheating = temperatures > 40
print(overheating)

safe = (temperatures >= 20) & (temperatures <=40)
safe_count = np.count_nonzero(safe)
print(safe_count)

values = np.array([10, 15, 20, 18])
changes = np.diff(values)
print(changes)