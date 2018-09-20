#! /usr/bin/env python3

# Solution for ISTA 421 / INFO 521 Fall 2015, HW 2, Problem 1
# Author: Clayton T. Morrison, 12 September 2015
# Modified by Kai Blumberg to answer the questions for HW2

import os
import numpy
# NOTE: If you are running on MacOSX and encounter an error like the following:
#     RuntimeError: Python is not installed as a framework.
#     The Mac OS X backend will not be able to function correctly
#     if Python is not installed as a framework...
# Then uncomment the following 2 lines:
# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#import os to change the file path
import os

#get the directory of this file.
directoryPath = os.path.dirname(os.path.abspath(__file__))

#change the file path to this directory to be able to load in the data.
os.chdir(directoryPath)

# -------------------------------------------------------------------------
# Utilities


def read_data(filepath, d=','):
    """
    Returns a numpy.array of the data.

    :param filepath: sting representing path to data file to load.
    :param d: char string representing delimiter separating values on a line in data file.
    """
    return numpy.genfromtxt(filepath, delimiter=d, dtype=None)


def plot_data(x, t, x_axis_lab, y_axis_lab, title):
    """
    Plot single input feature x data with corresponding response
    values t as a scatter plot.

    :param x: sequence of 1-dimensional input data values (numbers)
    :param t: sequence of 1-dimensional responses
    :param title: title of plot (default 'Data')
    :param x_axis_lab: string for the label of the x axis
    :param y_axis_lab: string for the label of the y axis
    :return: None
    """
    plt.figure()  # Create a new figure object for plotting
    plt.scatter(x, t, edgecolor='b', color='w', marker='o')
    plt.xlabel(x_axis_lab)
    plt.ylabel(y_axis_lab)
    plt.title(title)
    plt.pause(.1)  # required on some systems to allow rendering


def plot_model(x, w):
    """
    Plot the function (curve) of an n-th order polynomial model:
        t = w0*x^0 + w1*x^1 + w2*x^2 + ... wn*x^n
    This works by creating a set of x-axis (plotx) points and
    then use the model parameters w to determine the corresponding
    t-axis (plott) points on the model curve.

    :param x: sequence of 1-dimensional input data values (numbers)
    :param w: n-dimensional sequence of model parameters: w0, w1, w2, ..., wn
    :return: the plotx and plott values for the plotted curve
    """
    # NOTE: this assumes a figure() object has already been created.

    # plotx represents evenly-spaced set of 100 points on the x-axis
    # used for creating a relatively "smooth" model curve plot.
    # Includes points a little before the min x input (-0.25)
    # and a little after the max x input (+0.25)
    plotx = numpy.linspace(min(x)-0.25, max(x)+0.25, 100)

    # plotX (note that python is case sensitive, so this is *not*
    # the same as plotx with a lower-case x) is the "design matrix"
    # for our model curve inputs represented in plotx.
    # We need to do the same computation as we do when doing
    # model fitting (as in fitpoly(), below), except that we
    # don't need to infer (by the normal equations) the values
    # of w, as they are given here as input.
    # plotx.shape[0] ensures we create a matrix with the number of
    # rows corresponding to the number of points in plotx (this will
    # still work even if we change the number of plotx points to
    # something other than 100)
    plotX = numpy.zeros((plotx.shape[0], w.size))

    # populate the design matrix plotX
    for k in range(w.size):
        plotX[:, k] = numpy.power(plotx, k)

    # Take the dot (inner) product of the design matrix plotX and the
    # parameter vector w
    plott = numpy.dot(plotX, w)

    # plot the x (plotx) and t (plott) values in red
    plt.plot(plotx, plott, color='r', linewidth=2)

    plt.pause(.1)  # required on some systems to allow rendering
    return plotx, plott


def scale01(x):
    """
    HELPER FUNCTION: only needed if you are working with large
    x values.  This is NOT needed for problems 1, 2 and 4.

    Mathematically, the sizes of the values of variables (e.g., x)
    could be arbitrarily large.  However, when we go to manipulate
    those values on a computer, we need to be careful.  E.g., in
    these exercises we are taking powers of values and if the
    values are large, then taking a large power of the variable
    may exceed what can be represented numerically.

    For example, in the Olympics data (both men's and women's),
    the input x values are years in the 1000's.  If you model
    is, say, polynomial order 5, then you're taking a large
    number to the power of 5, which is the order of a quadrillion!
    Python floating point numbers have trouble representing this
    many significant digits.

    This function here scales the input data to be the range [0, 1]
    (i.e., between 0 and 1, inclusive).

    :param x: sequence of 1-dimensional input data values (numbers)
    :return: x values linearly scaled to range [0, 1]
    """
    x_min = min(x)
    x_range = max(x) - x_min
    return (x - x_min) / x_range


# -------------------------------------------------------------------------
# fitpoly

def fitpoly(x, t, model_order):
    """
    Given "training" data in input sequence x (number features),
    corresponding target value sequence t, and a specified
    polynomial of order model_order, determine the linear
    least mean squared (LMS) error best fit for parameters w,
    using the generalized matrix normal equation.

    model_order is a non-negative integer, n, representing the
    highest polynomial exponent of the polynomial model:
        t = w0*x^0 + w1*x^1 + w2*x^2 + ... wn*x^n

    :param x: sequence of 1-dimensional input data features
    :param t: sequence of target response values
    :param model_order: integer representing the highest polynomial exponent of the polynomial model
    :return: parameter vector w
    """

    # Construct the empty design matrix
    # numpy.zeros takes a python tuple representing the number
    # of elements along each axis and returns an array of those
    # dimensions filled with zeros.
    # For example, to create a 2x3 array of zeros, call
    #     numpy.zeros((2,3))
    # and this returns (if executed at the command-line):
    #     array([[ 0.,  0.,  0.],
    #            [ 0.,  0.,  0.]])
    # The number of columns is model_order+1 because a model_order
    # of 0 requires one column (filled with input x values to the
    # power of 0), model_order=1 requires two columns (first input x
    # values to power of 0, then column of input x values to power 1),
    # and so on...
    X = numpy.zeros((x.shape[0], model_order+1))

    # Fill each column of the design matrix with the corresponding
    for k in range(model_order+1):  # w.size
        X[:, k] = numpy.power(x, k)

    print('model_order', model_order)
    print('x.shape', x.shape)
    print('X.shape', X.shape)
    print('t.shape', t.shape)

    # according to the matrix normal equation w can be calculated from X and t by the following:
    # w = (X^T X)^1 X^T t
    w = numpy.linalg.inv(X.T.dot(X)).dot(X.T).dot(t) # Calculate w vector (as a numpy.array)

    print('w.shape', w.shape)

    return w


# -------------------------------------------------------------------------
# Script to run on particular data set
# -------------------------------------------------------------------------

# NOTE: You may need to update this path, depending on where you
# are running this script relative to the data directory.
# Here, I'm assuming the data directory is up one directory from
# the current directory (the '../' means "up one directory").
DATA_ROOT = '../data'


def read_data_fit_plot(data_path, x_axis_lab, y_axis_lab, plot_title, model_order=1, scale_p=False,
                       save_path=None, plot_p=False):
    """
    A "top-level" script to
        (1) Load the data
        (2) Optionally scale the data between [0, 1]
        (3) Plot the raw data
        (4) Find the best-fit parameters
        (5) Plot the model on top of the data
        (6) If save_path is a filepath (not None), then save the figure as a pdf
        (6) Optionally call the matplotlib show() fn, which keeps the plot open
    :param data_path: Path to the data
    :param x_axis_lab: string for x axis title
    :param y_axis_lab: string for y axis title
    :param plot_title: Title of the plot (default 'Data')
    :param model_order: Non-negative integer representing model polynomial order
    :param scale_p: Boolean Flag (default False)
    :param save_path: Optional (default None) filepath to save figure to file
    :param plot_p: Boolean Flag (default False)
    :return: None
    """

    print('\n-----------------------------------------------')

    # (1) load the data
    data = read_data(data_path, ',')

    # (2) Optionally scale the data between [0,1]
    # See the scale01 documentation for explanation of why you might want to scale
    if scale_p:
        x = scale01(data[:, 0])  # extract x (slice first column) and scale so x \in [0,1]
    else:
        x = data[:, 0]  # extract x (slice first column)
    t = data[:, 1]  # extract t (slice second column)

    # (3) plot the raw data
    plot_data(x, t, title=plot_title, x_axis_lab=x_axis_lab, y_axis_lab=y_axis_lab)

    # (4) find the best-fit model parameters using the fitpoly function
    w = fitpoly(x, t, model_order)

    print('Identified model parameters w (in scientific notation):\n', w)
    # python defaults to print floats in scientific notation,
    # so here I'll also print using python format, which I find easier to read
    print('w again (not in scientific notation):')
    print(' ', ['{0:f}'.format(i) for i in w])

    # (5) Plot the model on top of the data
    plot_model(x, w)

    # (6) If save_path is a filepath (not None), then save the figure as a pdf
    if save_path is not None:
        plt.savefig(save_path, fmt='pdf')

    # (7) Optionally show the plot window (and hold it open)
    if plot_p:
        plt.show()


def fit_mens100_data(plot_title, x_axis_lab, y_axis_lab, model_order=1, scale_p=False, plot_p=False):
    """
    The data/mens100.csv data is provided just for fun, not required for HW 2.
    This function calls the "top-level" read_data_fit_plot script using the
    path to the men's 100 data.

    After you have implemented the fitpoly function, you will be able to run
    this function.

    When you do, try the following experiment:
    Run this with model_order=6 with the scale_p=False and then again scale_p=True.
    You'll (likely) see that when you don't scale, the best-first model is "off",
    but when you do scale, then it fits well.  When not scaling, we're loosing
    precision due to the very large calculations with powers of 6.
    (model_order=4 will likely do this as well, but 6 almost certainly will.)

    :param plot_title: Title of the plot
    :param x_axis_lab: string for x axis title
    :param y_axis_lab: string for y axis title
    :param model_order: Integer representing the polynomial model order
    :param scale_p: Boolean specifying whether to scale the input data between [0, 1] before fitting
    :param plot_p: Boolean specifying whether to
    :return:
    """
    data_path = os.path.join(DATA_ROOT, 'mens100.csv')
    read_data_fit_plot(data_path, x_axis_lab=x_axis_lab, y_axis_lab=y_axis_lab, plot_title=plot_title, model_order=model_order, scale_p=scale_p, plot_p=plot_p)


# Example executions of the script -- uncomment to run:
# fit_mens100_data(plot_title='data', x_axis_lab='x', y_axis_lab='t', model_order=1, scale_p=False, plot_p=True)
# fit_mens100_data(x_axis_lab='x', y_axis_lab='t', model_order=6, scale_p=False, plot_p=True)
# fit_mens100_data(x_axis_lab='x', y_axis_lab='t', model_order=6, scale_p=True, plot_p=True)

def fit_womens100_data(plot_title, x_axis_lab, y_axis_lab, model_order=1, scale_p=False, plot_p=False):
    """
    Function to call the "top-level" read_data_fit_plot script using the
    path to the women's 100 data.

    :param plot_title: Title of the plot
    :param x_axis_lab: string for x axis title
    :param y_axis_lab: string for y axis title
    :param model_order: Integer representing the polynomial model order
    :param scale_p: Boolean specifying whether to scale the input data between [0, 1] before fitting
    :param plot_p: Boolean specifying whether to
    :return:
    """
    data_path = os.path.join(DATA_ROOT, 'womens100.csv')
    read_data_fit_plot(data_path, x_axis_lab=x_axis_lab, y_axis_lab=y_axis_lab, plot_title=plot_title, model_order=model_order, scale_p=scale_p, plot_p=plot_p, save_path=directoryPath)

# Execute fit_womens100_data script
# fit_womens100_data(plot_title='womens 100m olympic dash', x_axis_lab='year', y_axis_lab='winning running speed', model_order=1, scale_p=False, plot_p=True)


def fit_synthdata2018(plot_title, x_axis_lab, y_axis_lab, model_order, scale_p=False, plot_p=False):
    """
    Function to call the "top-level" read_data_fit_plot script using the
    path to the synthdata2018 data set.

    :param plot_title: Title of the plot
    :param x_axis_lab: string for x axis title
    :param y_axis_lab: string for y axis title
    :param model_order: Integer representing the polynomial model order
    :param scale_p: Boolean specifying whether to scale the input data between [0, 1] before fitting
    :param plot_p: Boolean specifying whether to
    :return:
    """
    data_path = os.path.join(DATA_ROOT, 'synthdata2018.csv')
    read_data_fit_plot(data_path, x_axis_lab=x_axis_lab, y_axis_lab=y_axis_lab, plot_title=plot_title, model_order=model_order, scale_p=scale_p, plot_p=plot_p, save_path=directoryPath)

# Execute synthdata2018 function
fit_synthdata2018(plot_title='synth data 2018', x_axis_lab='synth data 2018 x', y_axis_lab='synth data 2018 t', model_order=3, scale_p=False, plot_p=True)


# synthdata2018
