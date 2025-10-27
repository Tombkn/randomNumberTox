# Example Parameter Configurations

This file contains example parameter configurations for different use cases of the TouchDesigner Random Number Generator.

## Configuration Examples

### Basic Integer-like Numbers (0-100)
```
Min Range: 0.0
Max Range: 100.0
Number of Rows: 10
```
Example Output: 23.45, 67.89, 12.34, 89.01, 45.67

### Percentage Values (0-1)
```
Min Range: 0.0
Max Range: 1.0
Number of Rows: 5
```
Example Output: 0.23, 0.78, 0.45, 0.91, 0.12

### Temperature Range (Celsius)
```
Min Range: -30.0
Max Range: 40.0
Number of Rows: 7
```
Example Output: -12.45, 23.78, 35.92, -5.14, 18.67

### Audio Level Simulation (dB)
```
Min Range: -60.0
Max Range: 0.0
Number of Rows: 8
```
Example Output: -45.23, -12.78, -38.45, -5.91, -52.12

### Small Decimal Range
```
Min Range: 0.1
Max Range: 0.9
Number of Rows: 6
```
Example Output: 0.34, 0.78, 0.23, 0.65, 0.41

### Large Number Range
```
Min Range: 1000.0
Max Range: 10000.0
Number of Rows: 4
```
Example Output: 3456.78, 7891.23, 2345.67, 8901.45

## Parameter Guidelines

### Min Range and Max Range
- Min Range must be less than Max Range
- Can be positive, negative, or mixed
- Supports decimal values
- No specific limits on range size

### Number of Rows
- Must be a positive integer (greater than 0)
- Determines how many random numbers are generated
- Each number appears in its own row in the DAT table
- Typical values: 1-100 (depending on use case)

## Common Use Cases

1. **Animation Controllers**: Generate random values for position, rotation, or scale
2. **Audio Visualization**: Create random amplitude or frequency values
3. **Color Generation**: Generate RGB component values (0.0-1.0)
4. **Particle Systems**: Random positions, velocities, or lifetimes
5. **Generative Art**: Random parameters for artistic algorithms
6. **Testing/Debugging**: Generate test data with known ranges