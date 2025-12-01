def mini_calculator(expression: str) -> float | str:
    """
    Simple calculator that evaluates a mathematical expression from a string input.
    The expression should be in the form of 'operand operator operand' (e.g., '5 + 3').
    """

    try:
        # Split the expression into parts
        parts = expression.split()

        # Check if the expression has exactly 3 parts: operand1, operator, operand2
        if len(parts) != 3:
            return "Invalid format. Please enter the expression as 'operand operator operand'."

        # Parse the operands and operator
        operand1 = float(parts[0])
        operator = parts[1]
        operand2 = float(parts[2])

        # Perform calculation based on the operator
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            if operand2 == 0:
                return "Cannot divide by zero"
            return operand1 / operand2
        else:
            return "Invalid operator. Use +, -, *, or /."

    except ValueError:
        return "Invalid numbers. Please enter valid numerical values."


# Ask User for an expression
expression = input("Enter a mathematical expression (e.g., '5 + 3'): ")

# Evaluate the expression
result = mini_calculator(expression)

# Display the result
print(result)
