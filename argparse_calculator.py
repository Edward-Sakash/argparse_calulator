import argparse

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Simple Command-Line Calculator")

    # Add arguments
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Arithmetic operation")
    parser.add_argument("operand1", type=float, help="First operand")
    parser.add_argument("operand2", type=float, help="Second operand")

    # Parse the command line arguments
    args = parser.parse_args()

    # Perform the selected operation
    if args.operation == "add":
        result = add(args.operand1, args.operand2)
    elif args.operation == "subtract":
        result = subtract(args.operand1, args.operand2)
    elif args.operation == "multiply":
        result = multiply(args.operand1, args.operand2)
    elif args.operation == "divide":
        try:
            result = divide(args.operand1, args.operand2)
        except ValueError as e:
            print(f"Error: {e}")
            return

    # Print the result
    print(f"Result: {result:.2f}")

if __name__ == "__main__":
    main()
