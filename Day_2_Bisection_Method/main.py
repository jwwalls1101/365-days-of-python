
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

a = 2
b = 3
tol = 1e-8
max_iter = 100

def f(x):
    return x ** 3 - 4 * x - 9

def midpoint(a, b):
    c = (a + b) / 2
    return c

def bisection(f, a, b, tol, max_iter):
    
    if a >= b:
        raise ValueError("Lower bound must be smaller than upper bound.")

    if tol <= 0:
        raise ValueError("Tolerance must be positive.")

    if max_iter <= 0:
        raise ValueError("Maximum iterations must be positive.")

    if f(a) == 0:
        return a, 0, []

    if f(b) == 0:
        return b, 0, []

    if f(a) * f(b) > 0:
        raise ValueError("The interval does not bracket a root.")

    iterations = 0
    root_history = []

    for i in range(max_iter):

        c = midpoint(a, b)
        iterations += 1
        root_history.append(c)

        if f(c) == 0 or (b - a) / 2 <= tol:
            root = c
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    else:
        raise RuntimeError("Bisection failed to converge.")

    return root, iterations, root_history

root, iterations, root_history = bisection(f, a, b, tol, max_iter)

print("Estimated root:", root)
print("Iterations:", iterations)

iteration_number = range(1, len(root_history) + 1)
reference_root = 2.706527954497935
errors = []

for c in root_history:
    error = np.abs(c - reference_root)
    errors.append(error)

output_dir = Path(__file__).resolve().parent

plt.figure()
plt.plot(iteration_number, root_history, label="Estimated Root")
plt.axhline(
    reference_root,
    linestyle="--",
    label="Reference Root"
)
plt.xlabel("Iteration Number")
plt.ylabel("Estimated Root")
plt.title("Convergence of Roots")
plt.grid(True)
plt.legend()
plt.savefig(output_dir / "root_convergence.png",
            dpi=300, bbox_inches="tight")
plt.show()

plt.figure()
plt.semilogy(iteration_number, errors)
plt.xlabel("Iteration Number")
plt.ylabel("Absolute Error")
plt.title("Absolute Error vs. Iteration Number")
plt.grid(True, which="both", alpha=0.3)
plt.savefig(output_dir / "error_convergence.png",
            dpi=300, bbox_inches="tight")
plt.show()
