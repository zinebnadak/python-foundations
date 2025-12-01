# VARIABLES AND DATA TYPES (saturday 22.11)

"""Practice covers:
- numbers
- strings
- booleans
- simple input/output
- basic type conversion
- Exercise: mini calculator (add, subtract, multiply, divide) with error handling and type hints."""

#🔑 Key Concepts for Future Projects

#Once you have this fully understood:
#You can build games (score = numbers, input = strings, logic = booleans)
#You can perform data analysis (numbers + type conversion)
#You can write automation scripts (input/output + error handling)
#You can create small AI/ML examples later (arrays of numbers, logic, functions)



            ### NUMBER ###
a = 10
b = 3.5

print (a+b)
print (a*b)
print (a/b)
print (a//b) #integer division, only takes the integer!
print (a%b)  #modulus gives remainder from division



            ### STRINGS ###
name = "Zineb"
greeting = "Hello, " + name     #string concatenation

print(greeting)
print(name.upper())             #.upper() is a method of strings. The parentheses () after upper mean you are calling the method.
print(name.lower())
print(len(name))
print(name[0])

print(name.upper)           #you need to call it using () otherwise you´ll get <built-in method upper of str object at 0x100a48c30>



            ### BOOLEANS ###
is_happy = True
is_married = False

if is_happy and is_married:         # "and" is a logical operator. It returns True only if both conditions are True, and print text
    print("Ready to get married!")
else:
    print("Get rich Zineb!")



            ### Input/output (I/O) ###
# made to interact with the user

user_name = input("Enter your name: ")      #input for string
age = int(input("Enter your age: "))        #input for integers
confirmation = input (f"Hello {user_name}, can you just confirm you really are {age} years old?")



            ### Type_Conversion ###
num_str = "25"
num_int = int(num_str)       # str → int
num_float = float(num_str)   # str → float
str_num = str(num_int)       # int → str


######################## Mini Calculator ########################

# 1. definition (Type hints are present in the function signature: expression: str (input is a string) and -> float | str (output is either a float or a string) Type hints improve clarity, readability, and tooling support, making your code easier to understand and debug)
# 2. try + except (error handling)
# 3. user input
# 4. call function
# 5. print result


def mini_calculator(expression: str) -> float | str:    # "expression: str" user input expects a string, "-> float | str" : The function will return either a floating-point number or a string
    """
    Simple calculator that evaluates a mathematical expression from a string input.
    The expression should be in the form of 'operand operator operand' (e.g., '5 + 3').
    """

    try:        #The code inside the try block is doing multiple things that could potentially raise errors
        # Split the expression into parts
        parts = expression.split()

        # Check if the expression has exactly 3 parts: operand1, operator, operand2
        if len(parts) != 3:
            return "Invalid format. Please enter the expression as 'operand operator operand'."

        # Parse the operands and operator
        operand1 = float(parts[0])
        operator = parts[1]         #string
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

    except ValueError:#You're expecting that the user might enter invalid input that cannot be converted to a number
        return "Invalid numbers. Please enter valid numerical values."


# Ask User for an expression
expression = input("Enter a mathematical expression (e.g., '5 + 3'): ")

# Evaluate the expression
result = mini_calculator(expression)

# Display the result
print(result)













