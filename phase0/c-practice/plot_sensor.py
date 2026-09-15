import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("sensor.csv",delimiter = "," , skiprows=1)

sample_index = data[:, 0]
values = data[:, 1]
sample_rate = 10.0

time = sample_index / sample_rate

print("Number of samples:", values.size)
print("Minimum:", values.min())
print("Maximum:", values.max())
print("Mean:", values.mean())
print("Variance:", values.var())

plt.plot(time , values , marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Sensor Value")
plt.title("Synthetic Triangular sensor signal")
plt.grid(True)
plt.tight_layout()
plt.savefig("sensor_plot.png", dpi =150)
plt.show()
