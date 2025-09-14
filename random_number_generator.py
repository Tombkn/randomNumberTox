"""
TouchDesigner DAT Script for Random Number Generation

This script generates random numbers within a configurable range and outputs
them to a DAT table with each row containing one random number rounded to
two decimal places.

Parameters to configure:
- min_range: Minimum value for random number generation
- max_range: Maximum value for random number generation  
- num_rows: Number of random numbers to generate

Usage:
1. Place this script in a DAT operator in TouchDesigner
2. Configure the parameters below
3. Execute the script to generate random numbers
4. The output will be written to the DAT table
"""

import random

# Configuration Parameters
# These would typically be exposed as TouchDesigner parameters
min_range = 0.0      # Minimum value for random numbers
max_range = 100.0    # Maximum value for random numbers
num_rows = 10        # Number of random numbers to generate

def generate_random_numbers():
    """
    Generate random numbers within the specified range and write to DAT table.
    
    Returns:
        list: List of generated random numbers rounded to 2 decimal places
    """
    # Clear the DAT table first
    me.clear()
    
    # Set table headers
    me.appendCol(['Random Numbers'])
    
    # Generate random numbers
    random_numbers = []
    for i in range(num_rows):
        # Generate random number within range
        random_num = random.uniform(min_range, max_range)
        # Round to 2 decimal places
        rounded_num = round(random_num, 2)
        random_numbers.append(rounded_num)
        
        # Add to DAT table
        me.appendRow([str(rounded_num)])
    
    return random_numbers

def get_parameters():
    """
    Get parameters from TouchDesigner parent component.
    This function would be used to read parameter values in actual TouchDesigner environment.
    """
    # In actual TouchDesigner, these would be:
    # min_range = parent().par.Minrange.eval()
    # max_range = parent().par.Maxrange.eval()
    # num_rows = parent().par.Numrows.eval()
    
    global min_range, max_range, num_rows
    
    # For now, return the configured values
    return min_range, max_range, num_rows

def main():
    """
    Main execution function for the TouchDesigner DAT script.
    """
    # Get current parameters
    global min_range, max_range, num_rows
    min_range, max_range, num_rows = get_parameters()
    
    # Validate parameters
    if min_range >= max_range:
        print("Error: min_range must be less than max_range")
        return
    
    if num_rows <= 0:
        print("Error: num_rows must be greater than 0")
        return
    
    # Generate and display random numbers
    random_numbers = generate_random_numbers()
    
    print(f"Generated {len(random_numbers)} random numbers between {min_range} and {max_range}")
    print(f"Numbers: {random_numbers}")

# Execute the main function when script is run
if __name__ == "__main__":
    main()