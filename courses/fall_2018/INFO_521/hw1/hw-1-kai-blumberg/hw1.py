# -*- coding: utf-8 -*-
# hw1.py 

# import numpy to work with arrays
import numpy as np
#import os to change the file path
import os 
#import matplotlib to plot graphs
import matplotlib.pyplot as plt


#get the directory of this hw1.py file. 
directoryPath = os.path.dirname(os.path.abspath(__file__))

#change the file path to this directory to be able to load in the data. 
os.chdir(directoryPath)

#for implemenation only list the contents of the directory to ensure the data is present
#print(os.listdir(path='.'))

# exercise 6 

# Part A

# load in a ndarray called 'humu.txt'
fname = 'humu.txt'
humuData = np.loadtxt(fname)

# Print the type of the humuData object to the terminal 
print(type(humuData))

# Print the size of the loaded humu data
print('size = ' + str(humuData.size))

# Print the shape of the of the humu data
print('shape of the array is ' +str(humuData.shape) + ' with 366 rows and 576 columns')

# create a figure object fig
fig = plt.figure()

#add the humu data to the figure
fig = plt.imshow(humuData)

#plot the humu data
plt.show()

#print the current colormap 
print('current colormap is ' + str(plt.cm.cmapname))

#add the grey colormap to the plot
fig = plt.imshow(humuData, cmap='gray')

# Make a new greyscale image with the same size as the original data
randomData1= np.random.random_sample((366, 576))

# create a second figure object fig2
fig2 = plt.figure()

#add the randomData1 data to the figure
fig2 = plt.imshow(randomData1, cmap='gray')
#plot the randomData1
plt.show()

# Make an additional greyscale image with the same size as the original data
randomData2= np.random.random_sample((366, 576))

# create a second figure object fig2
fig3 = plt.figure()

#add the randomData1 data to the figure
fig3 = plt.imshow(randomData2, cmap='gray')
#plot the randomData1
plt.show()

#print explanation to random figures:
print('The randomly generated value figure does look as expected there are a random mix of black, white and inbetween grey tones distributed throughout. Clearly there is no longer a fish present.') 
print('The second random figure as expected is a different mix of random shades equaly distributed vs the data which has  a clear differentiation between low and high valuess')

# Write the uniformly random array (randomData2) to a file called ‘random.txt’
np.savetxt('random.txt', randomData2, delimiter=" ") 

# this 'random.txt' file can be read with a text editor

# load the 'random.txt' file back into a new variable reloadedRandomData
fname = 'random.txt'
reloadedRandomData = np.loadtxt(fname)

# Display the reloadedRandomData image again. 

# create a second figure object fig2
fig4 = plt.figure()

#add the randomData1 data to the figure
fig4 = plt.imshow(reloadedRandomData, cmap='gray')
#plot the humu data
plt.show()

print('I can confirm that the reloaded random data re-creates the same plot as it did before.')

print('"humu" refers to perhaps the Hawaiian fish "humu humu nuku nuku apua" which we see in the photo')


# Part B

fname = 'walk.txt'
walkData = np.loadtxt(fname)

print('min value of the walk array = ' + str(np.min(walkData)) + ', max value of the walk array = ' +  str(np.max(walkData)))

#To implement the scaling of the walk array, we need to apply the following function:
# F(x) = (x - min) / (max - min)

#set a walkData min variable
wmin = np.min(walkData)

#set a walkData max variable
wmax = np.max(walkData)

#initialize a new np array for our scaled array
walk_scale01 = np.array([])

# scale the array by implementing for each element in the array the function: F(x) = (x - min) / (max - min)
# referencing the link: http://akuederle.com/create-numpy-array-with-for-loop
for line in walkData:
    result = (line - wmin) / (wmax - wmin)
    walk_scale01 = np.append(walk_scale01, result)

#print(walk_scale01)

# Write the scaled walk_scale01 array to a file called 'walk_scale01.txt’
np.savetxt('walk_scale01.txt', walk_scale01, delimiter=" ") 

#Figure out the range of values contained within the array
print('min value of the walk_scale01 array = ' + str(np.min(walk_scale01)) + ', max value is = ' +  str(np.max(walk_scale01)))

#Verify that the new, scaled array has the same dimensions as the original
print('shape of the original walk array is ' +str(walkData.shape))
print('shape of the walk_scale01 array is ' +str(walk_scale01.shape))

# plot the original walk.txt and the scaled version walk_scale01

# function to plot arrays
def plot_1d_array(arr, title):
    plt.figure()
    plt.plot(arr)
    plt.suptitle(title, fontsize=20)

#plot the original:
plot_1d_array(walkData, 'orginal walk data')

#plot the scaled data:
plot_1d_array(walk_scale01, 'scaled walk data')


# for exercise 7,9,10,11 see file hw1_2.py



