# TouchDesigner DAT Script - Random Number Generator
# Place this code directly in a DAT operator (Text DAT or Script DAT)

import random

# Get parameters from parent component
min_range = parent().par.Minrange.eval() if hasattr(parent(), 'par') and hasattr(parent().par, 'Minrange') else 0.0
max_range = parent().par.Maxrange.eval() if hasattr(parent(), 'par') and hasattr(parent().par, 'Maxrange') else 100.0
num_rows = int(parent().par.Numrows.eval()) if hasattr(parent(), 'par') and hasattr(parent().par, 'Numrows') else 10

# Clear the DAT table
me.clear()

# Set table header
me.appendCol(['Random Numbers'])

# Validate parameters
if min_range < max_range and num_rows > 0:
    # Generate random numbers and populate DAT table
    for i in range(num_rows):
        # Generate random number within range
        random_num = random.uniform(min_range, max_range)
        # Round to 2 decimal places
        rounded_num = round(random_num, 2)
        # Add to DAT table
        me.appendRow([str(rounded_num)])
else:
    # Add error message to table
    me.appendRow(['Error: Invalid parameters'])
    if min_range >= max_range:
        me.appendRow(['Min range must be less than max range'])
    if num_rows <= 0:
        me.appendRow(['Number of rows must be greater than 0'])