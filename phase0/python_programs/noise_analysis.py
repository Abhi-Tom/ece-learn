import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data_files"

data = np.loadtxt(DATA_DIR / "sensor.csv", delimiter=",", skiprows=1)
sample_index = data[:,0]
clean_values = data[:,1]
sample_rate = 10.0
time = sample_index / sample_rate

rng = np.random.default_rng(42)
noise = rng.normal(loc=0.0 , scale=2.0 , size=clean_values.shape)
noisy_values = clean_values + noise

print("Clean signal")
print("Mean:", clean_values.mean())
print("Variance:", clean_values.var())
print("Standard deviation:", clean_values.std())

print("\nNoisy signal")
print("Mean:", noisy_values.mean())
print("Variance:", noisy_values.var())
print("Standard deviation:", noisy_values.std())

print("\nGenerated noise")
print("Mean:", noise.mean())
print("Variance:", noise.var())
print("Standard deviation:", noise.std())

noisy_data = np.column_stack((sample_index, noisy_values))
np.savetxt(
    "noisy_sensor.csv",
    noisy_data,
    delimiter=",",
    header="sample,value",
    comments="",
    fmt=["%d", "%.4f"],
)

plt.plot(
    time,
    clean_values,
    marker="o",
    label="Clean signal",
)

plt.plot(
    time,
    noisy_values,
    marker="x",
    linestyle="--",
    label="Noisy signal",
)

plt.xlabel("Time (s)")
plt.ylabel("Sensor value")
plt.title("Clean and noisy synthetic sensor signals")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(DATA_DIR / "noise_comparison.png", dpi=150)
plt.show()
