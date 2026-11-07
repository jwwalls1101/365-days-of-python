
import matplotlib.pyplot as plt
from pathlib import Path


def load_flight_data():
    folder = Path(__file__).resolve().parent
    file_path = folder / "flightdata.txt"

    with open(file_path, "r") as file:
        lines = file.readlines()

    flight_data = []

    for line in lines[1:]:
        values = line.strip().split(",")

        time = float(values[0])
        altitude = float(values[1])
        velocity = float(values[2])

        data = {
            "time": time,
            "altitude": altitude,
            "velocity": velocity
        }

        flight_data.append(data)

    return flight_data


def analyze_flight(data):
    if len(data) < 2:
        raise ValueError("At least two measurements are required.")

    max_altitude = data[0]["altitude"]
    max_velocity = data[0]["velocity"]
    climb_rates = []
    climb_times = []

    for measurement in data:
        if measurement["altitude"] > max_altitude:
            max_altitude = measurement["altitude"]

        if measurement["velocity"] > max_velocity:
            max_velocity = measurement["velocity"]

    for i in range(len(data) - 1):
        start_time = data[i]["time"]
        end_time = data[i + 1]["time"]
        max_time_start = start_time
        max_time_end = end_time

        if end_time <= start_time:
            raise ValueError("Flight times must be increasing.")

        climb = (data[i + 1]["altitude"] - data[i]["altitude"]) / (end_time - start_time)

        climb_rates.append(climb)

        climb_time = (start_time + end_time) / 2
        climb_times.append(climb_time)

    average_climb_rate = (data[-1]["altitude"] - data[0]["altitude"]) / (data[-1]["time"] - data[0]["time"])

    max_climb_rate = max(climb_rates)
    index = climb_rates.index(max_climb_rate)

    results = {
        "max_altitude": max_altitude,
        "max_velocity": max_velocity,
        "average_climb_rate": average_climb_rate,
        "climb_rates": climb_rates,
        "climb_times": climb_times,
        "max_climb_rate": max_climb_rate,
        "max_climb_start": max_time_start,
        "max_climb_end": max_time_end
    }

    return results


def plot_flight(data, results):
    times = []
    altitudes = []

    for measurement in data:
        times.append(measurement["time"])
        altitudes.append(measurement["altitude"])

    folder = Path(__file__).resolve().parent

    plt.plot(times, altitudes)
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title("Altitude vs. Time")
    plt.grid()
    plt.savefig(folder / "altitude_profile.png",
                dpi=300, bbox_inches="tight")
    plt.show()

    plt.plot(results["climb_times"], results["climb_rates"])
    plt.xlabel("Time (s)")
    plt.ylabel("Climb Rate (m/s)")
    plt.title("Climb Rate vs. Time")
    plt.grid()
    plt.savefig(folder / "climb_rate.png",
                dpi=300, bbox_inches="tight")
    plt.show()

flight_data = load_flight_data()
results = analyze_flight(flight_data)
print(results)
plot_flight(flight_data, results)