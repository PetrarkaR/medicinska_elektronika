import matplotlib.pyplot as plt


time = [0.0, 0.2, 0.23, 0.25, 0.3, 0.31, 0.33, 0.34, 0.5, 0.58, 0.65, 0.74, 1.0]
voltage = [0,   0,   0.25,  0,    0,    1,    -0.2,  0,    0,    0.3,   0.6,  0,    0]

plt.figure()
plt.plot(time, voltage)
plt.scatter([0.23, 0.31, 0.33, 0.65], [0.25, 1, -0.2, 0.6])  # P, R, S, T points
for t, v, label in zip([0.23, 0.31, 0.33, 0.65], [0.25, 1, -0.2, 0.6], ["P", "R", "S", "T"]):
    plt.annotate(label, (t, v), textcoords="offset points", xytext=(0,10), ha='center')

plt.title("EKG signali sa P R S T signalima")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (mV)")
plt.grid(True)
plt.show()
