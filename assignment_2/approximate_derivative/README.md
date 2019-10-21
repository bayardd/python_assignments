# Requirements:

    - Python 3.7
    - sys module
    - f"..." syntax introduced in Python 3.6.
    - matplotlib, pyplot module - can be installed with pip3 install matplotlib
    - math modules cos and sin

# Description:

    - This script will compute the approximate error for the derivative of f(x), where f(x) is sin(x) and x = 1 for 2^-1 - 2^-30. The formula used is the finite difference formula.
    The approximate values calculated will be compared to the known derivative (cos(x)), and Absolute Errors will be calculated. A graph will be produced using the x axis as the h values (2^-1 to 2^-30)
    The y axis will be the calculated error, the graph will be drawn using a logarithmic scale for both the x and y values.

# Sample Execution and Output:

    - python3 approximateDerivative.py

Run

    - python convert_base.py

# Output similar to:

    |  h  |      x      |  Approx. f'(x)  |  Known f'(x)  |  Abs. Error  |
    ----------------------------------------------------------------------
    | 2^-0 | 1.00000000 |   0.31204800   |   0.540302   |   0.22825430    |
    | 2^-1 | 1.00000000 |   0.43005454   |   0.540302   |   0.11024777    |
    | 2^-2 | 1.00000000 |   0.48637287   |   0.540302   |   0.05392943    |


# Notes

    - Image of the graph is stored in the images directory
    - In order to prevent the world from falling into chaos, x and y axis labels have been added
    - In order to prevent the graph from being rendered, the generateGraph function in main needs to be commented

# Documentation

 - pydoc3.7 approximateDerivative

--- Does not take command line parameters ---

