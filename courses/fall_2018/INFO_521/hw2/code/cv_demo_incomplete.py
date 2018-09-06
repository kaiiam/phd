# Script for ISTA 421 / INFO 521 Fall 2016, HW 2, Problem 4
# Author: Clayton T. Morrison, 13 September 2015
# Updated: 3 September 2018
# Based on cv_demo.m
# From A First Course in Machine Learning, Chapter 1.
# Simon Rogers, 31/10/11 [simon.rogers@glasgow.ac.uk]

# NOTE: In its released form, this script will NOT run
#       You will get an error originating from line 335 with an
#       attempt to take a dot product with None, but the origin
#       of the problem is that you need to fill in the calculation
#       of w on line 331

# NOTE:
# When summarizing log errors, DO NOT take the mean of the log
# instead, first take the mean of the errors, then take the log of the mean

import numpy
# NOTE: If you are running on MacOSX and encounter an error like the following:
#     RuntimeError: Python is not installed as a framework.
#     The Mac OS X backend will not be able to function correctly
#     if Python is not installed as a framework...
# Then uncomment the following 2 lines:
# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# -------------------------------------------------------------------------
# Utilities

# The following permutation tools are used below in run_cv() as a convenience
# for randomly sorting the order of the data (more specifically, the indices
# of the input data)

def random_permutation_matrix(n):
    """
    Generate a permutation matrix: an NxN matrix in which each row
    and each column has only one 1, with 0's everywhere else.
    See: https://en.wikipedia.org/wiki/Permutation_matrix
    :param n: size of the square permutation matrix
    :return: NxN permutation matrix
    """
    rows = numpy.random.permutation(n)
    cols = numpy.random.permutation(n)
    m = numpy.zeros((n, n))
    for r, c in zip(rows, cols):
        m[r][c] = 1
    return m


def permute_rows(X, P=None):
    """
    Permute the rows of a 2-d array (matrix) according to
    permutation matrix P: left-multiply X by P
    If no P is provided, a random permutation matrix is generated.
    :param X: 2-d array
    :param P: Optional permutation matrix; default=None
    :return: new version of X with rows permuted according to P
    """
    if P is None:
        P = random_permutation_matrix(X.shape[0])
    return numpy.dot(P, X)


def permute_cols(X, P=None):
    """
    Permute the columns of a 2-d array (matrix) according to
    permutation matrix P: right-multiply X by P
    If no P is provided, a random permutation matrix is generated.
    :param X: 2-d array
    :param P: Optional permutation matrix; default=None
    :return: new version of X with columns permuted according to P
    """
    if P is None:
        P = random_permutation_matrix(X.shape[0])
    return numpy.dot(X, P)


# -------------------------------------------------------------------------
# Utilities from fitpoly

def read_data(filepath, d=','):
    """ returns an numpy.array of the data """
    return numpy.genfromtxt(filepath, delimiter=d, dtype=None)


def plot_data(x, t):
    """
    Plot single input feature x data with corresponding response
    values t as a scatter plot
    :param x: sequence of 1-dimensional input data features
    :param t: sequence of 1-dimensional responses
    :return: None
    """
    plt.figure()  # Create a new figure object for plotting
    plt.scatter(x, t, edgecolor='b', color='w', marker='o')
    plt.xlabel('x')
    plt.ylabel('t')
    plt.title('Data')
    plt.pause(.1)  # required on some systems so that rendering can happen


def plot_model(x, w, color='r'):
    """
    Plot the curve for an n-th order polynomial model:
        t = w0*x^0 + w1*x^1 + w2*x^2 + ... wn*x^n
    This works by creating a set of x-axis (plotx) points and
    then use the model parameters w to determine the corresponding
    t-axis (plott) points on the model curve.
    :param x: sequence of 1-dimensional input data features
    :param w: n-dimensional sequence of model parameters: w0, w1, w2, ..., wn
    :param color: matplotlib color to plot model curve
    :return: the plotx and plott values for the plotted curve
    """
    # NOTE: this assumes a figure() object has already been created.
    plotx = numpy.linspace(min(x) - 0.25, max(x) + 0.25, 100)
    plotX = numpy.zeros((plotx.shape[0], w.size))
    for k in range(w.size):
        plotX[:, k] = numpy.power(plotx, k)
    plott = numpy.dot(plotX, w)
    plt.plot(plotx, plott, color=color, linewidth=2)
    plt.pause(.1)  # required on some systems so that rendering can happen
    return plotx, plott


# -------------------------------------------------------------------------
# Synthetic data generation

def generate_synthetic_data(N, w, xmin=-5, xmax=5, sigma=150):
    """
    Generate some synthetic data
    :param N: Number of sample points
    :param w: numpy array (1d) representing generating model parameters
    :param xmin: x minimum
    :param xmax: x maximum
    :param sigma: standard deviation
    :return:
    """
    # generate N random input x points between [xmin, xmax]
    x = (xmax - xmin) * numpy.random.rand(N) + xmin

    # generate response with Gaussian random noise
    X = numpy.zeros((x.size, w.size))
    for k in range(w.size):
        X[:, k] = numpy.power(x, k)
    t = numpy.dot(X, w) + sigma * numpy.random.randn(x.shape[0])

    return x, t


def plot_data_and_model(x, t, w,
                        title='Plot of synthetic data; green curve is original generating function',
                        filepath=None):
    plot_data(x, t)
    plt.title(title)
    plot_model(x, w, color='g')
    if filepath:
        plt.savefig(filepath, format='pdf')




# -------------------------------------------------------------------------

def plot_cv_results(train_loss, cv_loss, ind_loss=None, log_scale_p=False,
                    plot_title='Mean Square Error Loss', filepath=None):
    """
    Helper function to plot the results of cross-validation.
    You can use this when you have all three types of loss, or
    if you just have train and cv loss (in this case, set ind_loss to None)
    :param train_loss:
    :param cv_loss:
    :param ind_loss: If None, only display train_loss and cv_loss
    :param log_scale_p: Whether the plots are in log-scale
    :param plot_title: Title for the plot
    :param filepath: If specified, save pdf file
    :return:
    """

    if ind_loss is not None:
        figw, figh, mydpi = 1200, 420, 96
        plt.figure(figsize=(figw / mydpi, figh / mydpi), dpi=mydpi)
    else:
        figw, figh, mydpi = 800, 420, 96
        plt.figure(figsize=(figw / mydpi, figh / mydpi), dpi=mydpi)

    # plt.figure()
    plt.suptitle(plot_title)

    if log_scale_p:
        ylabel = 'Log MSE Loss'
    else:
        ylabel = 'MSE Loss'

    x = numpy.arange(0, train_loss.shape[0])

    # put y-axis on same scale for all plots
    if ind_loss is not None:
        min_ylim = min(min(train_loss), min(cv_loss), min(ind_loss))
    else:
        min_ylim = min(min(train_loss), min(cv_loss))
    min_ylim = int(numpy.floor(min_ylim))
    if ind_loss is not None:
        max_ylim = max(max(train_loss), max(cv_loss), max(ind_loss))
    else:
        max_ylim = max(max(train_loss), max(cv_loss))
    max_ylim = int(numpy.ceil(max_ylim))

    # Plot training loss
    if ind_loss is not None:
        plt.subplot(131)
    else:
        plt.subplot(121)
    plt.plot(x, train_loss, linewidth=2)
    plt.xlabel('Model Order')
    plt.ylabel(ylabel)
    plt.title('Train Loss')
    plt.pause(.1) # required on some systems so that rendering can happen
    plt.ylim(min_ylim, max_ylim)

    # Plot CV loss
    if ind_loss is not None:
        plt.subplot(132)
    else:
        plt.subplot(122)
    plt.plot(x, cv_loss, linewidth=2)
    plt.xlabel('Model Order')
    plt.ylabel(ylabel)
    plt.title('CV Loss')
    plt.pause(.1) # required on some systems so that rendering can happen
    plt.ylim(min_ylim, max_ylim)

    # Plot independent-test loss
    if ind_loss is not None:
        plt.subplot(133)
        plt.plot(x, ind_loss, linewidth=2)
        plt.xlabel('Model Order')
        plt.ylabel(ylabel)
        plt.title('Independent Test Loss')
        plt.pause(.1) # required on some systems so that rendering can happen
        plt.ylim(min_ylim, max_ylim)

    if ind_loss is not None:
        plt.subplots_adjust(right=0.95, wspace=0.4)
    else:
        plt.subplots_adjust(right=0.95, wspace=0.25, bottom=0.2)

    plt.draw()

    if filepath:
        plt.savefig(filepath, format='pdf')


# -------------------------------------------------------------------------

def run_cv( K, maxorder, x, t, testx, testt, randomize_data=False, title='CV' ):
    """

    :param K: Number of folds
    :param maxorder: Integer representing the highest polynomial order
    :param x: input data (1d observations)
    :param t: target data
    :param testx: independent test input data
    :param testt: independent test target data
    :param randomize_data: Boolean (default False) whether to randomize the order of the data
    :param title: Title for plots of results
    :return:
    """

    N = x.shape[0]  # number of data points

    # Use when you want to ensure the order of the data has been
    # randomized before splitting into folds
    # Note that in the simple demo here, the data is already in
    # random order.  However, if you use this function more generally
    # for new data, you may need to ensure you're randomizing the
    # order of the data!
    if randomize_data:
        # use the same permutation P on both x and t, otherwise they'll
        # each be in different orders!
        P = random_permutation_matrix(x.size)
        x = permute_rows(x, P)
        t = permute_rows(t, P)

    # Storage for the design matrix used during training
    # Here we create the design matrix to hold the maximum sized polynomial order
    # When computing smaller model polynomial orders below, we'll just use
    # the first 'k+1' columns for the k-th order polynomial.  This way we don't
    # have to keep creating new design matrix arrays.
    X = numpy.zeros((x.shape[0], maxorder + 1))

    # Design matrix for independent test data
    testX = numpy.zeros((testx.shape[0], maxorder + 1))

    # Create approximately equal-sized fold indices
    # These correspond to indices in the design matrix (X) rows
    # (where each row represents one training input x)
    fold_indices = list(map(lambda x: int(x), numpy.linspace(0, N, K + 1)))

    # storage for recording loss across model polynomial order
    # rows = fold loss (each row is the loss for one fold)
    # columns = model polynomial order
    cv_loss = numpy.zeros((K, maxorder + 1))     # cross-validation loss
    train_loss = numpy.zeros((K, maxorder + 1))  # training loss
    ind_loss = numpy.zeros((K, maxorder + 1))    # independent test loss

    # iterate over model polynomial orders
    for p in range(maxorder + 1):

        # Augment the input data by the polynomial model order
        # E.g., 2nd-order polynomial model takes input x to the 0th, 1st, and 2nd power
        X[:, p] = numpy.power(x, p)

        # ... do the same for the independent test data
        testX[:, p] = numpy.power(testx, p)

        # iterate over folds
        for fold in range(K):
            # Partition the data
            # foldX, foldt contains the data for just one fold being held out
            # trainX, traint contains all other data

            foldX = X[fold_indices[fold]:fold_indices[fold+1], 0:p+1]
            foldt = t[fold_indices[fold]:fold_indices[fold+1]]

            # safely copy the training data (so that deleting doesn't remove the original
            trainX = numpy.copy(X[:, 0:p + 1])
            # remove the fold x from the training set
            trainX = numpy.delete(trainX, numpy.arange(fold_indices[fold], fold_indices[fold + 1]), 0)

            # safely copy the training data (so that deleting doesn't remove the original
            traint = numpy.copy(t)
            # remove the fold t from the training set
            traint = numpy.delete(traint, numpy.arange(fold_indices[fold], fold_indices[fold + 1]), 0)

            # find the least mean squares fit to the training data
            ### YOUR CODE HERE
            w = None  # Calculate w vector (as an numpy.array)

            # calculate and record the mean squared losses

            train_pred = numpy.dot(trainX, w)  # model predictions on training data
            train_loss[fold, p] = numpy.mean(numpy.power(train_pred - traint, 2))

            fold_pred = numpy.dot(foldX, w)  # model predictions on held-out fold
            cv_loss[fold, p] = numpy.mean(numpy.power(fold_pred - foldt, 2))

            ind_pred = numpy.dot(testX[:, 0:p + 1], w)   # model predictions on independent test data
            ind_loss[fold, p] = numpy.mean(numpy.power(ind_pred - testt, 2))

    # The loss values can get quite large, so take the log for display purposes

    # Ensure taking log of the mean (not mean of the log!)
    mean_train_loss = numpy.mean(train_loss, 0)
    mean_cv_loss = numpy.mean(cv_loss, 0)
    mean_ind_loss = numpy.mean(ind_loss, 0)

    log_mean_train_loss = numpy.log(mean_train_loss)
    log_mean_cv_loss = numpy.log(mean_cv_loss)
    log_mean_ind_loss = numpy.log(mean_ind_loss)

    print('\n----------------------\nResults for {0}'.format(title))
    print('log_mean_train_loss:\n{0}'.format(log_mean_train_loss))
    print('log_mean_cv_loss:\n{0}'.format(log_mean_cv_loss))
    print('log_mean_ind_loss:\n{0}'.format(log_mean_ind_loss))

    min_mean_log_cv_loss = min(log_mean_cv_loss)
    # TODO: has to be better way to get the min index...
    best_poly = [i for i, j in enumerate(log_mean_cv_loss) if j == min_mean_log_cv_loss][0]

    print('minimum mean_log_cv_loss of {0} for order {1}'.format(min_mean_log_cv_loss, best_poly))

    # Plot log scale loss results
    plot_cv_results(log_mean_train_loss, log_mean_cv_loss, log_mean_ind_loss,
                    log_scale_p=True, plot_title=title)

    # Uncomment to plot direct-scale mean loss results
    # plot_cv_results(mean_train_loss, mean_cv_loss, mean_ind_loss, log_scale_p=False)

    return best_poly, min_mean_log_cv_loss


# -------------------------------------------------------------------------


def run_demo():
    """
    Top-level script to run the cv demo
    """

    # Parameters for synthetic data model
    # t = x - x^2 + 5x^3 + N(0, sigma)
    w = numpy.array([0, 1, 5, 2])
    # t = x + 5x^2 + 2x^3 + N(0, sigma)
    xmin = -6
    xmax = 6
    sigma = 50

    x, t = generate_synthetic_data(25, w, xmin=xmin, xmax=xmax, sigma=sigma)
    testx, testt, = generate_synthetic_data(1000, w, xmin=xmin, xmax=xmax, sigma=sigma)

    plot_data_and_model(x, t, w)

    K = 10

    run_cv( K, 7, x, t, testx, testt, randomize_data=False, title='{0}-fold CV'.format(K) )


# -------------------------------------------------------------------------
# SCRIPT
# -------------------------------------------------------------------------


run_demo()
plt.show()


