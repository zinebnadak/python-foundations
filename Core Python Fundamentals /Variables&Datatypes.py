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

def mini_calculator (a:float, b:float, op: str) -> float | str:             #parameters (inputs) the function accepts. The : after each parameter is called a type hint, it doesn’t enforce the type but helps readability and tools. | means “or”. It tells Python (and humans reading your code) that the function will return either a float OR a string. This is the return type hint.
    """
        Simple calculator
        a, b: numbers
        op: '+', '-', '*', '/'
    """

    try:
        if op == "+":
            return a+b
        elif op == "-":
            return a-b
        elif op == "*":
            return a*b
        elif op == "/":
            return a/b
        else:
            return "Invalid operator"
    except ZeroDivisionError:       #ZeroDivisionError happens when you try to divide a number by zero
        return "Cannot divide by zero"

#Test
print (mini_calculator(5,2, "+"))
print (mini_calculator(5,0,"/"))

#Ask User
# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")




#UPGRADE and fix ask user: like a real calculator, where the user types a full expression (e.g., 5/6 or 12+3) and the program evaluates it.












