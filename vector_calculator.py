import argparse
import numpy as np

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Vector Calculator")

    # Add arguments for vector components
    parser.add_argument("--vector1", type=float, nargs="+", required=True, help="Components of vector 1")
    parser.add_argument("--vector2", type=float, nargs="+", required=True, help="Components of vector 2")

    # Parse the command line arguments
    args = parser.parse_args()

    # Convert input vectors to NumPy arrays
    vector1 = np.array(args.vector1)
    vector2 = np.array(args.vector2)

    # Check if the vectors have the same shape
    if vector1.shape != vector2.shape:
        print("Error: Vectors must have the same shape")
        return

    # Calculate scalar product using NumPy's dot() function
    scalar_product = np.dot(vector1, vector2)

    # Print the result
    print(f"Scalar product: {scalar_product}")

if __name__ == "__main__":
    main()
