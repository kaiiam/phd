# -*- coding: utf-8 -*-
# hw1_2.py 

#answering exercise 7 with the modifications of the script from exercise 6. 

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

# exercise 7

def plot_1d_array(arr, title):
    """
    Function to plot arrays
    :param arr: input ndarray
    :param title: input title string to add to a plot
    :return: printed plot of array specified by data in arr and with a title specified by title
    """
    plt.figure()
    plt.plot(arr)
    plt.suptitle(title, fontsize=20)

def exercise_6(infile, outfile):
    """
    Function to read in an ndarray, assess it's size, shape, colormap, and print it, 
    generate 2 random array of same size and print them, take in another 'walk.txt' array, 
    scale it within the range [0,1] and output it to an outfile walk_scale01.txt.
    :param infile: a string refering to a filename of an ndarray to import
    :param outfile: a string refering to a filename in which to output a scaled ndarray 
    """
    
    # load in a ndarray specifed by the param infile
    fname = infile
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

    # Write the uniformly random array (randomData2) to an file specified by the param outfile
    np.savetxt(outfile, randomData2, delimiter=" ") 

    # this outfile file can be read with a text editor

    # load the oufile file back into a new variable reloadedRandomData
    fname = outfile
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

    #plot the original:
    plot_1d_array(walkData, 'orginal walk data')

    #plot the scaled data:
    plot_1d_array(walk_scale01, 'scaled walk data')

#call exercise_6 function
exercise_6('humu.txt', 'random.txt')

# exercise 9

#set the seed
np.random.seed(seed=8)

def exercise9():
    """
    Function to estimate the probability of rolling double 6's in 1000 rolls of two dice.
    no params
    outputs to terminal: The estimated probability of rolling two 6's in 1000 double dice rolls.
    """   
    #generate 1000 events in which two dice are rolled and put them into an array of arrays
    # from https://docs.scipy.org/doc/numpy/reference/generated/numpy.stack.html#numpy.stack
    arrays = [np.random.randint(1,7,size=2) for _ in range(1000)]
    
    #put together the arrays into a single array using np.stack
    array = np.stack(arrays, axis=0)
    
    # make a summation integer
    sumInt = 0
    
    for x in array:
        #check if both dice rolls are the same and if they are both 6's,
        #if so add them to the doubles count 
        if x[0] == x[1] and x[0] == 6:
            sumInt += 1
    #print out the number of double 6's divided by 1000
    #hence the estimated probability of rolling two 6's in 1000 double dice rolls
    print("The estimated probability of rolling two 6's in 1000 double dice rolls is " + str(sumInt/1000))

# call exercise9
exercise9()

# procceded to call exercise9 an additional 9 times. 
exercise9()
exercise9()
exercise9()
exercise9()
exercise9()
exercise9()
exercise9()
exercise9()
exercise9()

#print comment describing results:
print('The results of running the experiment 10 times indicate that the estimated probability varies.')
print('For example values range from 0.021-0.045 when the seed is set to 8')
print('The original estimate of 0.026 was reproduced in an additional 2/9 runs')

#reset the seed to 8 again 
np.random.seed(seed=8)

print('after resetting the seed and reruning the estimation procedure 10 times again we have:')

# rerun the estimation procedure 10 times again
exercise9()
exercise9()
exercise9()
exercise9()
exercise9()
exercise9()
exercise9()
exercise9()
exercise9()
exercise9()

print('Is often important to have random number sequences that are controlled and not truly random,')
print('so that randomization experiments such as this can be re-run in a reproducible manner.')


# exercise 10

def exercise10():
    """
    Function to generate two random colum vectors a and b of size 3 rows by 1 column, add them, multiply them, compute Hadamard product,
    compute the dot product. Additionally to create a random 3 × 3 matrix X and perform the operations: a^T X, a^T X b, X^-1. 
    Printing all answers to the terminal. 
    params: none 
    """
    #Part A
    
    #set the seed
    np.random.seed(seed=5)
    
    #create two colum vectors of size 3 rows by 1 column
    a = np.random.rand(3,1)
    b = np.random.rand(3,1)
    
    #print out a
    print('vector a = ')
    print(a)
    
    #print out b
    print('vector b = ')
    print(b)
    
    #Part B
    
    #compute a + b
    print('a + b = ')
    print(a + b)
    
    # a◦b element-wise multiply, or Hadamard product, or the entrywise product, or the Schur product
    print('a◦b =')
    print(a * b)
    
    # a^T b or dot product
    print('a dot b =')
    print(np.vdot(a, b))

    # Part C
    
    #set the seed to 2
    np.random.seed(seed=2)
    
    #generate a random 3 × 3 matrix X
    X = np.random.rand(3,3)    
    #print(X)
    
    # a^T X =
    print('a^T X =')
    print(a.T * X)
    
    # a^T X b =
    print('a^T X b =')
    print(a.T * X * b)
    
    # X^-1 =
    print('X^-1 =')
    print(np.linalg.inv(X))

#call the exercise10() function  
exercise10()


def exercise11():
    """
    Function to plot a pdf graphic of the function sin(x) where x is between 0 and 10 in steps of 0.01
    Params: none
    Returns a pdf plot image 'exercise11_b.pdf'
    """
    #generate x axis points between 0 and 10 with steps of 0.01
    x_axis = np.linspace(0,10,101)
    #generate y axis by taking sin(x) for every x point
    y_axis = [ np.sin(x) for x in x_axis ]

    #create a new figure
    fig = plt.figure()
    #plot the data points 
    plt.plot(x_axis, y_axis)
    
    #add title
    plt.title('Sine Function for x from 0.0 to 10.0',fontsize=20)
    
    #add x axis label
    plt.xlabel('x values')
    
    #add y axis label
    plt.ylabel('sin(x)')
    
    #show the figure
    plt.show()
    
    #save the figure to file
    plt.savefig('exercise11_b.pdf', format='pdf')

    
#call the exercise11() function  
exercise11()