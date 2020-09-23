# Code for "Creating Functions", module #8 from
#  Software Carpentry's "Programming with Python"
# Team member: Miguel E. Cruz Molina
# Student ID #: 801-16-1956
# Date of creation: 9-21-2020
# Date of last edit: 9-22-2020

# Import packages used in module:

import numpy as np
import matplotlib.pyplot as plt
import glob

# Introductory exercises

'''
def fahr_to_celsius(temp):
  return ((temp - 32) * (5/9))

# print(fahr_to_celsius(32))

print("freezing point of water:", fahr_to_celsius(32), 'C')
print("boiling point of water:", fahr_to_celsius(212), 'C')

# Composing functions:

def celsius_to_kelvin(temp_c):
  return temp_c + 273.15

print("freezing point of water in Kelvin:", celsius_to_kelvin(0.))

def fahr_to_kelvin(temp_f):
  temp_c = fahr_to_celsius(temp_f)
  temp_k = celsius_to_kelvin(temp_c)
  return temp_k

print("boiling point of water in Kelvin:", fahr_to_kelvin(212.0))
'''

# Tidying up

'''
def visualize(filename):
  
  data = np.loadtxt(fname = filename, delimiter = ',')

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
  plt.show()

def detect_problems(filename):

  data = np.loadtxt(fname = filename, delimiter = ',')

  if np.max(data, axis = 0)[0] == 0 and np.max(data, axis = 0)[20] == 20:
    print("Suspicious looking maximal")
  elif np.sum(data, axis = 0) == 0:
    print("Minima add up to zero!")
  else:
    print("Seems OK!")

filenames = sorted(glob.glob('data/inflammation*.csv'))

for filename in filenames[:3]:
  print(filename)
  visualize(filename)
  detect_problems(filename)
'''

# Testing and documenting:

'''
def offset_mean(data, target_mean_value):
  """Return a new array containing the original data 
  with its mean offset to match the desired value.
  
  Examples:
  ---------
  >>> offset_mean([1, 2, 3], 0)
  array([-1., 0., 1.])
  """
  return (data - np.mean(data)) + target_mean_value

  # z = np.zeros((2, 2))
  # print(offset_mean(z, 3))

data = np.loadtxt(fname = "data/inflammation-01.csv", delimiter = ',')
  # print(offset_mean(data, 0))

print("original min, mean, and max are:", 
  np.min(data), 
  np.mean(data), 
  np.max(data))

offset_data = offset_mean(data, 0)

print("min, mean, and max of offset data are:",
  np.min(offset_data),
  np.mean(offset_data),
  np.max(offset_data))

print("difference in standard deviations before and after:",
  np.std(data) - np.std(offset_data))

help(offset_mean)
'''

# Defining defaults

  # np.loadtxt(fname = "data/inflammation-01.csv", delimiter = ',')

def offset_mean(data, target_mean_value = 0.0):
  """Return a new array containing the original data 
  with its mean offset to match the desired value.
  
  Examples:
  ---------
  >>> offset_mean([1, 2, 3], 0)
  array([-1., 0., 1.])
  """
  return (data - np.mean(data)) + target_mean_value

test_data = np.zeros((2, 2))
print(offset_mean(test_data, 2))

more_data = 5 + np.zeros((2, 2))
print('data before mean offset:')
print(more_data)
print('offset data')
print(offset_mean(more_data))

def display(a = 1, b = 2 , c = 3):
  print('a:', a, 'b:', b, 'c:', c)

print("no parameters:")
display()
print("one parameetr:")
display(55)
print("two parameters:")
display(55, 66)
print("only setting the value of c:")
display(c = 77) 

  # help(np.loadtxt)

# Readable functions:

  # This section doesn't have any executable code, just
  # a reflection about documenting functions, something
  # the authors recommend because it makes programs more
  # easy to understand.

# Combining strings (bonus exercise):

'''
def fence(original = "string", wrapper = '*'):

  """Returns string 'original' with 'wrapper' character
  concatenated to it at its beginning and end.
  
  Example: fence('name', '*') returns string '*name*'
  """

  return (wrapper + original + wrapper)

print(fence("name", '*'))
'''

# Return versus print (bonus exercise):

  # The described code will display 10 because of the
  #  'print' in the definition of add(), but because
  #  add() doesn't really return anything, 'print(A)'
  #  will return 'None', the default value returned by
  #  print().

# Selecting characters from strings (bonus exercise):

'''
def outer(word = "abcdefghijklmnopqrstuvwxyz"):

  """Returns first and last characters from string input.
  """

  return (word[0] + word[-1])

print(outer('helium'))
'''

# Rescaling an array (bonus exercise):

'''
def rescale(input_array):

  """Returns rescaled version of array by replacing each
  of its values with a corresponding value between 0.0 
  and 1.0.
  """

  L = np.min(input_array)
  H = np.max(input_array)
  output_array = (input_array - L)/(H - L)

  return output_array
'''

# Testing and documenting your function (bonus exercise):

  # help(np.arange)
  # help(np.linspace)

  # arr1 = np.arange(10.0)
  # print(rescale(arr1))
  
  # arr2 = np.linspace(0, 100, 5)
  # print(rescale(arr2))

  # arr1 = [1, 2, 4, 5, 6]
  # print(rescale(arr1))

# Defining defaults (bonus exercise):

'''
def rescale2(input_array, LBound = 0.0, UBound = 1.0):

  """Returns rescaled version of array by replacing each
  of its values with a corresponding value between the  
  lower bound 'LBound' (0.0 by default) and the higher
  boung (1.0 by default) provided.
  """

  L = np.min(input_array); H = np.max(input_array)
  output_array = (input_array - L)/(H - L)

  # We adjust the range of the values
  output_array * (UBound - LBound)

  # We move the array so that its min value coincides
  #  with the lower bound.
  output_array - (np.min(output_array) -  LBound)

  return output_array

print(rescale2([1, 2, 4, 5, 6]))
'''

# Variables inside and outside functions (bonus exercise):

  # 'f2k(8)' returns 259.81666666666666
  # 'f2k(41)' returns 287.15
  # 'f2k(32)' returns 273.15
  # 'print(k)' returns 0

  # The k value printed is 0 because it corresponds to the
  #  variable that was initialized before defining f2k(),
  #  not the copy of that variable created in f2k().

# Mixing default and non-default parameters

  
  # The first code displays answer (4.), "SyntaxError".
  # The second displays answer (3.), "a: -1, b: 2, c: 6".

# The old switcheroo (bonus exercise):

  # The code displays answer (2.), "3 7", because it uses
  #  original values of a and b.abs
