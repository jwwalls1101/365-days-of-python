
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

CD0 = 0.025
e = 0.82
AR = 8.5
CL = np.linspace(0, 1.5, 200)

def drag_polar(CL, CD0, e, AR):
    K = 1 / (np.pi * e * AR)
    CDi = K * CL ** 2
    CD = CD0 + CDi

    results = {
        "Parasitic Drag Coefficient": CD0,
        "Induced Drag Factor": K,
        "Induced Drag Coefficient": CDi,
        "Total Drag Coefficient": CD
    }

    return results


def plot_drag_polar(CL, results):
    plt.figure()
    plt.plot(CL, results["Total Drag Coefficient"], label="Total Drag Coefficient")
    plt.plot(CL, results["Induced Drag Coefficient"], label="Induced Drag Coefficient")
    plt.xlabel("Lift Coefficient")
    plt.ylabel("Drag Coefficient")
    plt.title("Aircraft Drag Polar")
    plt.legend()
    plt.grid()

    folder = Path(__file__).resolve().parent
    plt.savefig(folder / "drag_polar.png",
                dpi=300, bbox_inches="tight")
    plt.show()


def calculate_ratio(CL, results):
    lift_drag = CL / results["Total Drag Coefficient"]

    max_lift_drag = np.max(lift_drag)
    index = np.argmax(lift_drag)

    CL_at_max = CL[index]
    CD_at_max = results["Total Drag Coefficient"][index]
    induced_drag_at_max = results["Induced Drag Coefficient"][index]

    max_results = {
        "max_lift_drag": max_lift_drag,
        "CL_at_max": CL_at_max,
        "CD_at_max": CD_at_max,
        "induced_drag_at_max": induced_drag_at_max
    }

    return max_results


def analytical(CD0, K, numerical_max_LD):
    CL_optimal = np.sqrt(CD0 / K)
    analytical_max_LD = 1 / (2 * np.sqrt(CD0 * K))
    LDerror = (np.abs(numerical_max_LD - analytical_max_LD) / analytical_max_LD) * 100

    analytical_results = {
        "CL_optimal": CL_optimal,
        "analytical_max_LD": analytical_max_LD,
        "LDerror": LDerror
    }

    return analytical_results

results = drag_polar(CL, CD0, e, AR)
plot_drag_polar(CL, results)
max_results = calculate_ratio(CL, results)

analytical_results = analytical(
    CD0,
    results["Induced Drag Factor"],
    max_results["max_lift_drag"]
)

print("\n--- Numerical Results ---")
print("Maximum L/D:", max_results["max_lift_drag"])
print("CL at Maximum L/D:", max_results["CL_at_max"])
print("CD at Maximum L/D:", max_results["CD_at_max"])

print("\n--- Drag Comparison ---")
print("Parasitic Drag:", CD0)
print("Induced Drag:", max_results["induced_drag_at_max"])

if np.isclose(CD0, max_results["induced_drag_at_max"], rtol=0.01):
    print("Parasitic and Induced Drag Coefficients are Approximately Equal")

print("\n--- Analytical Results ---")
print("Optimal CL:", analytical_results["CL_optimal"])
print("Maximum L/D:", analytical_results["analytical_max_LD"])
print("Percentage Error:", analytical_results["LDerror"], "%")



