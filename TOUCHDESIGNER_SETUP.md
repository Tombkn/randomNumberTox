# TouchDesigner Random Number Generator Setup Guide

## Overview
This TouchDesigner .tox component generates random numbers within a configurable range and outputs them to a DAT table. Each row contains one random number rounded to two decimal places.

## Setup Instructions

### 1. Create the TouchDesigner Component

1. Open TouchDesigner
2. Create a new Component (right-click > Operators > Component)
3. Enter the component and set up the following structure:

### 2. Add Parameters to the Component

In the Component's parameters, add the following custom parameters:

**Page: Random Generator**
- **Minrange** (Float)
  - Name: `Minrange`
  - Label: `Min Range`
  - Default: `0.0`
  - Description: Minimum value for random number generation

- **Maxrange** (Float)
  - Name: `Maxrange`
  - Label: `Max Range`
  - Default: `100.0`
  - Description: Maximum value for random number generation

- **Numrows** (Integer)
  - Name: `Numrows`
  - Label: `Number of Rows`
  - Default: `10`
  - Description: Number of random numbers to generate

- **Generate** (Pulse)
  - Name: `Generate`
  - Label: `Generate Numbers`
  - Description: Execute random number generation

### 3. Create the DAT Network

Inside the component, create the following operators:

1. **Text DAT** (name it `randomNumbers`)
   - This will hold the generated random numbers
   - Copy the code from `touchdesigner_dat_script.py` into this DAT

2. **Execute DAT** (name it `executeGenerator`)
   - Set the Execute parameter to monitor `parent().par.Generate`
   - In the Execute script, add: `op('randomNumbers').run()`

### 4. Script Setup

Copy the contents of `touchdesigner_dat_script.py` into the Text DAT operator. This script will:

- Read the component's parameters (Min Range, Max Range, Number of Rows)
- Generate random numbers within the specified range
- Round all numbers to 2 decimal places
- Populate the DAT table with one number per row

### 5. Usage

1. Set your desired **Min Range** and **Max Range** values
2. Set the **Number of Rows** to specify how many random numbers to generate
3. Click the **Generate Numbers** button to execute the script
4. View the results in the `randomNumbers` DAT table

## Features

- **Configurable Range**: Set minimum and maximum values for random number generation
- **Variable Output Size**: Configure how many random numbers to generate
- **Precision Control**: All numbers are automatically rounded to 2 decimal places
- **Error Handling**: Validates parameters and provides error messages for invalid inputs
- **Real-time Generation**: Execute anytime by clicking the Generate button

## Example Output

With Min Range: 10.0, Max Range: 50.0, Number of Rows: 5, the output might look like:

```
Random Numbers
23.45
41.78
15.92
38.14
29.67
```

## File Structure

- `touchdesigner_dat_script.py` - The main script to copy into TouchDesigner DAT
- `random_number_generator.py` - Standalone Python version for testing
- `TOUCHDESIGNER_SETUP.md` - This setup guide
- `README.md` - General project information

## Notes

- The script uses Python's `random.uniform()` function for floating-point number generation
- Parameters are automatically read from the component's custom parameters
- The DAT table is cleared each time the script runs to ensure fresh output
- Error messages are displayed in the DAT table if invalid parameters are provided