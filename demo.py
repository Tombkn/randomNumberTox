#!/usr/bin/env python3
"""
Demonstration script for the TouchDesigner Random Number Generator.
This shows the functionality without requiring TouchDesigner.
"""

import random

class SimulatedDAT:
    """Simulates TouchDesigner DAT functionality for demonstration"""
    
    def __init__(self):
        self.table_data = []
        self.headers = []
        
    def clear(self):
        """Clear all data from the table"""
        self.table_data = []
        self.headers = []
        
    def appendCol(self, col_headers):
        """Add column headers"""
        self.headers.extend(col_headers)
        
    def appendRow(self, row_data):
        """Add a row of data"""
        self.table_data.append(row_data)
        
    def display(self):
        """Display the table contents"""
        if self.headers:
            print(f"{'='*20}")
            for header in self.headers:
                print(f"{header:>15}")
            print(f"{'='*20}")
            
        for row in self.table_data:
            for item in row:
                print(f"{item:>15}")
        
        if self.table_data:
            print(f"{'='*20}")
            print(f"Total rows: {len(self.table_data)}")

def generate_random_numbers_demo(min_range, max_range, num_rows):
    """
    Demonstrate the random number generation functionality.
    
    Args:
        min_range (float): Minimum value for random numbers
        max_range (float): Maximum value for random numbers
        num_rows (int): Number of random numbers to generate
    """
    print(f"\nGenerating {num_rows} random numbers between {min_range} and {max_range}")
    print(f"All numbers will be rounded to 2 decimal places")
    
    # Create simulated DAT table
    me = SimulatedDAT()
    
    # Validate parameters
    if min_range >= max_range:
        print("Error: min_range must be less than max_range")
        me.clear()
        me.appendCol(['Error'])
        me.appendRow(['Invalid range parameters'])
        me.display()
        return
    
    if num_rows <= 0:
        print("Error: num_rows must be greater than 0")
        me.clear()
        me.appendCol(['Error'])
        me.appendRow(['Invalid number of rows'])
        me.display()
        return
    
    # Clear and set up the table
    me.clear()
    me.appendCol(['Random Numbers'])
    
    # Generate random numbers
    generated_numbers = []
    for i in range(num_rows):
        # Generate random number within range
        random_num = random.uniform(min_range, max_range)
        # Round to 2 decimal places
        rounded_num = round(random_num, 2)
        generated_numbers.append(rounded_num)
        
        # Add to DAT table
        me.appendRow([str(rounded_num)])
    
    # Display results
    me.display()
    
    # Show statistics
    print(f"\nStatistics:")
    print(f"Average: {round(sum(generated_numbers) / len(generated_numbers), 2)}")
    print(f"Minimum: {min(generated_numbers)}")
    print(f"Maximum: {max(generated_numbers)}")
    
    return generated_numbers

def main():
    """Run demonstration with various parameter sets"""
    print("TouchDesigner Random Number Generator - Demonstration")
    print("=" * 60)
    
    # Test cases to demonstrate functionality
    test_cases = [
        (0.0, 100.0, 10),      # Basic case
        (-50.0, 50.0, 5),      # Negative to positive range
        (10.5, 20.5, 8),       # Decimal range
        (0.1, 0.9, 6),         # Small decimal range
        (1000.0, 2000.0, 4),   # Large numbers
    ]
    
    for i, (min_range, max_range, num_rows) in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i} ---")
        generate_random_numbers_demo(min_range, max_range, num_rows)
    
    # Demonstrate error handling
    print(f"\n--- Error Handling Demonstration ---")
    print("\nTesting invalid range (min >= max):")
    generate_random_numbers_demo(100.0, 50.0, 5)
    
    print("\nTesting invalid number of rows (0):")
    generate_random_numbers_demo(0.0, 100.0, 0)
    
    print("\n" + "=" * 60)
    print("Demonstration complete!")
    print("\nTo use in TouchDesigner:")
    print("1. Copy the code from 'touchdesigner_dat_script.py' into a Text DAT")
    print("2. Set up component parameters as described in TOUCHDESIGNER_SETUP.md")
    print("3. Execute the script to generate random numbers")

if __name__ == "__main__":
    main()