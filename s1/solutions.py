import numpy as np
import matplotlib.pyplot as plt
import scipy

# Define a sin function using NumPy
sine = lambda x: np.sin(x)

# Find the minimum of the function using SciPy
res = scipy.optimize.minimize(sine, x0=[0])

print("X Location of minimum: {}".format(res.x[0]))
print("Value of sin(x): {}".format(sine(res.x[0])))

# X Location of minimum: -1.5707963335877664
# Value of sin(x): -1.0

# Integrate the function from [0, 1] using SciPy
res = scipy.integrate.quad(sine, 0.0, 1.0)

print("Integral of sin(x) from x=0...1: {}".format(res[0]))

# Integral of sin(x) from x=0...1: 0.45969769413186023

# Plot the function using Matplotlib from [0, 2π]
x = np.linspace(0, 2*np.pi, 500)
y = sine(x)

plt.plot(x,y)
plt.title(r'Sine Wave [0, 2$\pi$]')
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid()
plt.savefig("sine_wave.png")