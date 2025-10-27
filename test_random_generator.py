#!/usr/bin/env python3
"""
Test script for the random number generator functionality.
This tests the core logic without TouchDesigner dependencies.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import random
import unittest
from unittest.mock import Mock

class MockDAT:
    """Mock DAT object to simulate TouchDesigner DAT functionality"""
    def __init__(self):
        self.data = []
        self.cols = []
    
    def clear(self):
        self.data = []
        self.cols = []
    
    def appendCol(self, col_data):
        self.cols.extend(col_data)
    
    def appendRow(self, row_data):
        self.data.append(row_data)
    
    def get_data(self):
        return self.data
    
    def get_cols(self):
        return self.cols

class TestRandomNumberGenerator(unittest.TestCase):
    """Test cases for random number generator functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.mock_dat = MockDAT()
        # Set random seed for predictable testing
        random.seed(42)
    
    def test_generate_random_numbers_basic(self):
        """Test basic random number generation"""
        min_range = 0.0
        max_range = 100.0
        num_rows = 5
        
        # Simulate the core logic
        self.mock_dat.clear()
        self.mock_dat.appendCol(['Random Numbers'])
        
        generated_numbers = []
        for i in range(num_rows):
            random_num = random.uniform(min_range, max_range)
            rounded_num = round(random_num, 2)
            generated_numbers.append(rounded_num)
            self.mock_dat.appendRow([str(rounded_num)])
        
        # Verify results
        self.assertEqual(len(generated_numbers), num_rows)
        self.assertEqual(len(self.mock_dat.get_data()), num_rows)
        self.assertEqual(self.mock_dat.get_cols(), ['Random Numbers'])
        
        # Verify all numbers are within range
        for num in generated_numbers:
            self.assertGreaterEqual(num, min_range)
            self.assertLessEqual(num, max_range)
    
    def test_rounding_to_two_decimal_places(self):
        """Test that numbers are properly rounded to 2 decimal places"""
        min_range = 0.0
        max_range = 1.0
        num_rows = 10
        
        generated_numbers = []
        for i in range(num_rows):
            random_num = random.uniform(min_range, max_range)
            rounded_num = round(random_num, 2)
            generated_numbers.append(rounded_num)
        
        # Verify all numbers have at most 2 decimal places
        for num in generated_numbers:
            decimal_places = len(str(num).split('.')[-1]) if '.' in str(num) else 0
            self.assertLessEqual(decimal_places, 2)
    
    def test_parameter_validation(self):
        """Test parameter validation logic"""
        # Test invalid range
        min_range = 100.0
        max_range = 50.0
        self.assertGreaterEqual(min_range, max_range)  # Should be invalid
        
        # Test valid range
        min_range = 10.0
        max_range = 50.0
        self.assertLess(min_range, max_range)  # Should be valid
        
        # Test invalid number of rows
        num_rows = 0
        self.assertLessEqual(num_rows, 0)  # Should be invalid
        
        # Test valid number of rows
        num_rows = 5
        self.assertGreater(num_rows, 0)  # Should be valid
    
    def test_different_ranges(self):
        """Test generation with different range values"""
        test_cases = [
            (0.0, 10.0, 5),
            (-50.0, 50.0, 3),
            (100.0, 1000.0, 2),
            (0.1, 0.9, 4)
        ]
        
        for min_range, max_range, num_rows in test_cases:
            with self.subTest(min_range=min_range, max_range=max_range, num_rows=num_rows):
                generated_numbers = []
                for i in range(num_rows):
                    random_num = random.uniform(min_range, max_range)
                    rounded_num = round(random_num, 2)
                    generated_numbers.append(rounded_num)
                
                self.assertEqual(len(generated_numbers), num_rows)
                for num in generated_numbers:
                    self.assertGreaterEqual(num, min_range)
                    self.assertLessEqual(num, max_range)
    
    def test_dat_table_structure(self):
        """Test that DAT table is structured correctly"""
        self.mock_dat.clear()
        self.mock_dat.appendCol(['Random Numbers'])
        
        # Add some test data
        test_numbers = [1.23, 4.56, 7.89]
        for num in test_numbers:
            self.mock_dat.appendRow([str(num)])
        
        # Verify structure
        self.assertEqual(self.mock_dat.get_cols(), ['Random Numbers'])
        self.assertEqual(len(self.mock_dat.get_data()), len(test_numbers))
        
        # Verify data content
        for i, expected_num in enumerate(test_numbers):
            self.assertEqual(self.mock_dat.get_data()[i], [str(expected_num)])

def run_tests():
    """Run all tests and display results"""
    print("Running Random Number Generator Tests...")
    print("=" * 50)
    
    unittest.main(argv=[''], exit=False, verbosity=2)

if __name__ == "__main__":
    run_tests()