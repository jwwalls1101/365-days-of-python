import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x) + x ** 2

def anaf(x):
    return np.cos(x) + 2 * x

def fwddiff(f, x, h):
    fxh = f(x + h)
    df = (fxh - f(x)) / h
    return df

def cntrdiff(f, x, h):
    fxh1 = f(x + h)
    fxh2 = f(x - h)
    df = (fxh1 - fxh2) / (2 * h)
    return df

forward_result = fwddiff(f, 2, .1)
central_result = cntrdiff(f, 2, .1)
real = anaf(2)

fwderror = np.abs(((forward_result - real) / real) * 100)
cntrerror = np.abs(((central_result - real) / real) * 100)

print("Forward Difference: ", forward_result)
print("Central Difference: ", central_result)
print("Analytical Derivative: ", real)
print("Forward Difference Percent Error: ", fwderror)
print("Center Difference Percent Error: ", cntrerror)

hs = np.logspace(-1, -12, 100)

error1 = []
error2 = []

analytical = anaf(2)

for h in hs:
    fd = fwddiff(f, 2, h)
    fc = cntrdiff(f, 2, h)
    abserror1 = np.abs(fd - analytical)
    error1.append(abserror1)
    abserror2 = np.abs(fc - analytical)
    error2.append(abserror2)

index1 = np.argmin(error1)
index2 = np.argmin(error2)
print("Forward Optimal h: ", hs[index1])
print("Forward Minimum Error: ", error1[index1])
print("Central Optimal h: ", hs[index2])
print("Central Minimum Error: ", error2[index2])

      
plt.loglog(hs, error1, label="Forward Difference")
plt.scatter(hs[index1], error1[index1], label="Forward Optimal h")
plt.loglog(hs, error2, label="Central Difference")
plt.scatter(hs[index2], error2[index2], label="Central Optimal h")
plt.xlabel("Step Size (h)")
plt.ylabel("Absolute Error")
plt.grid(True, which="both", alpha=.3)
plt.legend()
plt.title("Absolute Error vs. h")
plt.savefig("Day_1_Numerical_Differentiation/results.png",
            dpi=300, bbox_inches="tight")
plt.show()




