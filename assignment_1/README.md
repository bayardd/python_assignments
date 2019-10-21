# Python file which converts decimal numbers to their binary equivelance.

# Requirements:
    - Python 3.6
    - sys module
    - f"..." syntax introduced in Python 3.6.

# Constraints:
    This file will only converts floating point decimals that exist within [0,1)
    will not produce correct results.

# Sample Execution and Output:

If run without command line arguments:

- python convert_base.py

# output:

If running with command line parameters:

    - python convert_base.py .5 .75 .25 

output similar to:

    
    | BASE 10 | BASE 2 | 
    |   .5    |    .1  |
    |   .75   |   .11  |
    |   .25   |   .01  | 

basic pydoc documentation to display main functions
    pydoc convert_base
