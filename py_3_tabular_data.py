# Code for "Tabular Data", module #3 from
#  Software Carpentry's "Programming with Python"
# Team member: Miguel E. Cruz Molina
# Student ID #: 801-16-1956
# Date: 9-16-2020

# Import packages used in module:

import numpy as np
import matplotlib.pyplot as plt

# Read data from "inflammation-01.csv":

data = np.loadtxt(fname = "data/inflammation-01.csv", delimiter = ",")

# Introductory code: plots for data average, max values
#  and min values:

'''
  image = plt.imshow(data)
  plt.show()

  ave_inflammation = np.mean(data, axis = 0)
  ave_plot = plt.plot(ave_inflammation)
  plt.show()

  max_plot = plt.plot(np.max(data, axis = 0))
  plt.show() 

  min_plot = plt.plot(np.min(data, axis = 0))
  plt.show() 
'''

# Formal code from the module, generates figure with three
#  plots displayed side by side: data average plot, max values
#  plot and min values:

fig = plt.figure(figsize = (10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel("average")
axes1.plot(np.mean(data, axis = 0))

axes2.set_ylabel("max")
axes2.plot(np.max(data, axis = 0))

axes3.set_ylabel("min")
axes3.plot(np.min(data, axis = 0))

fig.tight_layout()

plt.savefig("inflammation.png")
plt.show()

# Variation on the original code, integrating added code
#  from the bonus exercises: (1.) display plots using straight
#  lines as steps instead of continuous lines denoting non-int
#  values, (2.) change y-axis range to (0, 6), (3.) display
#  plot of standard deviation of data, and (4.) display plots
#  one on top another instead of side by side. 

'''
  fig = plt.figure(figsize = (3.0, 13.0))

  axes1 = fig.add_subplot(4, 1, 1)
  axes2 = fig.add_subplot(4, 1, 2)
  axes3 = fig.add_subplot(4, 1, 3)
  axes4 = fig.add_subplot(4, 1, 4)

  axes1.set_ylabel("average")
  axes1.plot(np.mean(data, axis = 0), drawstyle = "steps-mid")
  axes1.set_ylim(0, 6)

  axes2.set_ylabel("max")
  axes2.plot(np.max(data, axis = 0), drawstyle = "steps-mid")
  axes2.set_ylim(0, 6)

  axes3.set_ylabel("min")
  axes3.plot(np.min(data, axis = 0), drawstyle = "steps-mid")
  axes3.set_ylim(0, 6)

  axes4.set_ylabel("std dev")
  axes4.plot(np.std(data, axis = 0), drawstyle = "steps-mid")
  axes4.set_ylim(0, 6)

  fig.tight_layout()

  plt.savefig("inflammation.png")
  plt.show()
'''
