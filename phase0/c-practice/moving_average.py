import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("noisy_sensor.csv",delimiter=",",skiprows=1)

sample_index = data[:,0]
noisy_values = data[:,1]

sample_rate = 10.0
time = sample_index / sample_rate
window_size = 3

averages = []

for start in range(len(noisy_values) - window_size + 1 ):
	window = noisy_values[ start : start + window_size ]
	average = window.mean()
	averages.append(average)

smoothed_values = np.array(averages)

smoothed_time = time[ window_size - 1 : ]

print("Input samples : " , noisy_values.size)
print("Output samples:", smoothed_values.size)
print("Window size:", window_size)
print("First window:", noisy_values[:window_size])
print("First average:", smoothed_values[0])

plt.plot(time, noisy_values, "o--", label="Noisy signal")
plt.plot(
    smoothed_time,
    smoothed_values,
    "s-",
    label=f"Moving average: {window_size} samples",
)

plt.xlabel("Time (s)")
plt.ylabel("Sensor value")
plt.title("Smoothing synthetic sensor readings")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("moving_average.png", dpi=150)
plt.show()
