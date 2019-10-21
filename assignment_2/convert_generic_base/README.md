# Requirements:
    - Python 3.7
    - sys module
    - f"..." syntax introduced in Python 3.6.

# Constraints:
    
    - This file will only convert floating point decimals that exist within [0,1)


# Sample Execution and Output:

If run without command line arguments:

- python convert_base.py

# Output:

If running with command line parameters:

    - python convert_base.py .5 .75 .25

output similar to:

    |  BASE 10   |        BASE 60          |
    |------------|-------------------------|
    | .5         |    .30                  |
    | .25        |    .15                  |
    | .16666     |    .9;59;58;33;36       |

    |  BASE 10   |        BASE 2          |
    |------------|-------------------------|
    | .5         |    .1                   |
    | .25        |    .0;1                 |
    | .75        |    .1;1                 |

# Basic Pydoc documentation to display main functions:
    
    -pydoc3.7 convert_base
