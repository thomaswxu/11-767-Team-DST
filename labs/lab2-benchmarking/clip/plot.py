import matplotlib.pyplot as plt

plot_fname = "plot.png"
x = [1, 5, 10, 40, 70] # e.g. batch sizes
#y = [0.234, 0.297, 0.375] # mean timings
y = [1.0, 1.15, 1.3, 1.8, 2.1] # mean timings

plt.plot(x, y, '-o')
plt.xlabel('Input Size (# tokens)')
plt.ylabel('Latency (seconds)')
plt.savefig(plot_fname)
# or plot.show() if you e.g. copy results to laptop

