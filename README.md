# argparse_calulator

**# Bonus :   Exercise 1(argparse calulator):**

1. * **Define Operations:** *
     Decide on the arithmetic operations your calculator will support, such as addition, subtraction, multiplication, and division. Define functions for each operation.
   * 2. * **Setup Argument Parsing:** *
   * Use the `argparse` module to set up command-line argument parsing. Define arguments for the operation, two operands, and other necessary options.
   * 3. * **Implement Operations:** *
          Inside your code, implement the logic for each operation based on the provided arguments.
   * 4. * **Handle Errors:** *
          Add error handling to deal with potential division by zero or invalid inputs.
   * 5. * **Print Result:** *
          After performing the operation, print the result.

# Bonus: Vector Calculator with Variable-Length Vectors

1. **Setup Argument Parsing** : Use the argparse module to set up command-line argument parsing. Define arguments for the components of the two vectors.
2. **Convert to NumPy Arrays** : Inside your code, convert the input vector components to NumPy arrays.
3. **Check Vector Shapes** : Ensure that both input vectors have the same shape before calculating the scalar product.
4. **Calculate Scalar Product** :Calculate the scalar product of the two vectors using NumPy's dot() function.
5. **Print Result** :After calculating the scalar product, print the result.

**Example Command Line Usage:**

```
python vector_calculator.py --vector1 2 3 4 --vector2 5 6 7
```
