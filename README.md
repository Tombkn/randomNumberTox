# TouchDesigner Random Number Generator

This TouchDesigner .tox contains a DAT Script that allows you to configure a min and max range, as well as the number of rows. Each time it is executed, the script generates random numbers within the defined range. The output values are written into a DAT table, with each row containing one random number rounded to two decimal places.

## Features

- **Configurable Range**: Set minimum and maximum values for random number generation
- **Variable Output Size**: Configure how many random numbers to generate (number of rows)
- **Precision Control**: All numbers are automatically rounded to 2 decimal places
- **Error Handling**: Validates parameters and provides error messages for invalid inputs
- **TouchDesigner Integration**: Designed specifically for TouchDesigner DAT operators

## Files

- `touchdesigner_dat_script.py` - Main script to copy into TouchDesigner DAT operator
- `random_number_generator.py` - Standalone Python version for testing and development
- `TOUCHDESIGNER_SETUP.md` - Detailed setup instructions for TouchDesigner
- `demo.py` - Demonstration script showing functionality
- `test_random_generator.py` - Unit tests for validation

## Quick Start

1. See `TOUCHDESIGNER_SETUP.md` for detailed TouchDesigner setup instructions
2. Copy the code from `touchdesigner_dat_script.py` into a Text DAT in TouchDesigner
3. Set up component parameters for Min Range, Max Range, and Number of Rows
4. Execute the script to generate random numbers

## Example Output

With Min Range: 10.0, Max Range: 50.0, Number of Rows: 5:

```
Random Numbers
23.45
41.78
15.92
38.14
29.67
```

## Testing

Run the test suite:
```bash
python3 test_random_generator.py
```

Run the demonstration:
```bash
python3 demo.py
``` 
