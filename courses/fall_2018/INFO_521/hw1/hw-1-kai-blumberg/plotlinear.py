# plotlinear.py

import numpy as np
# NOTE: If you are running on MacOSX and encounter an error like the following:
#     RuntimeError: Python is not installed as a framework.
#     The Mac OS X backend will not be able to function correctly
#     if Python is not installed as a framework...
# Then uncomment the following 2 lines:
# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Define two points for the x-axis
x = np.array([-5, 5])

# Define the different intercepts and gradients to plot
w0 = np.arange(0, 20)
w1 = np.arange(0, 8, 0.4)

# Plot all of the lines
plt.figure()
plt.plot()

for i in range(w0.shape[0]):
    plt.plot(x, w0[i] + w1[i]*x)
    print('\ny = ' + str(w0[i]) + ' + ' + str(w1[i]) + ' x')

print("\nClose the current plot window to continue")

plt.show()

# Request user input
plt.figure()
plt.plot()
plt.ion()

print("\nThe following will ask you for intercept and slope values")
print("   (assuming floats) and will keep plotting lines on a new plot ")
print("   until you enter 'save', which will save the plot as a pdf ")
print("   called 'line_plot.pdf'.")
print("(NOTE: you may see a MatplotlibDeprecationWarning -- you can safely ignore this)\n")

while True:
    intercept = input("Enter intercept: ")
    if intercept == 'save':
        break
    else:
        intercept = float(intercept)

    gradient = input("Enter gradient (slope): ")
    if gradient == 'save':
        break
    else:
        gradient = float(gradient)

    plt.plot(x, intercept + gradient*x)
    plt.show()
    plt.pause(.1)

    plt.savefig('line_plot.pdf', format='pdf')

    print("\ny = " + str(intercept) + " + " + str(gradient) + " x\n")

