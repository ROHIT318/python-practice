# Operators are symbols or special characters that are used to perform various operations on data.

var_one = 10
var_two = 5

# 1. Arithmetic Operators:
# Addition +: Adds two operands together.
res = var_one + var_two
print(res) # 15

# Subtraction -: Subtracts the right operand from the left operand.
res = var_one - var_two
print(res) # 5

# Multiplication *: Multiplies two operands.
res = var_one * var_two
print(res) # 50

# Division /: Divides the left operand by the right operand, resulting in a float value.
res = var_one / var_two
print(res) # 2.0 (float division)

# Modulus %: Returns the remainder after the division of the left operand by the right operand.
res = var_one % var_two
print(res) # 0

# Floor Division //: Divides the left operand by the right operand and returns the integer result (rounding down).
res = var_one // var_two
print(res) # 2

# Exponentiation **: Raises the left operand to the power of the right operand.
res = var_one ** var_two
print(res) # 100000

# 2. Comparison Operators (Relational Operators): Comparison operators (also known as relational operators) are used to compare values and determine the relationship between them. These operators return a Boolean value (True or False).
# Equal to ==: Checks if the left operand is equal to the right operand.
print(var_one == var_two) # False

# Not equal to !=: Checks if the left operand is not equal to the right operand.
print(var_one != var_two) # True

# Less than <: Checks if the left operand is less than the right operand.
print(var_one < var_two) # False

# Greater than >: Checks if the left operand is greater than the right operand.
print(var_one > var_two) # True

# Less than or equal to <=: Checks if the left operand is less than or equal to the right operand.
print(var_one <= var_two) # False

# Greater than or equal to >=: Checks if the left operand is greater than or equal to the right operand.
print(var_one >= var_two) # True

# 3. Assignment Operators: Assignment operators are used to assign values to variables. It combines the assignment of a value with a specific operation, making it convenient to update the value of a variable in a single statement.
# =: Assigns the value on the right to the variable on the left.
var_one = 10

# +=: Adds the value on the right to the variable on the left and updates the variable with the result.
var_one += 3
print(var_one) # 13

# -=: Subtracts the value on the right from the variable on the left and updates the variable with the result.
var_one -= 2
print(var_one) # 11

# *=: Multiplies the variable on the left by the value on the right and updates the variable with the result.
var_one *= 6
print(var_one) # 66

# /=: Divides the variable on the left by the value on the right and updates the variable with the result.
var_one /= 3
print(var_one) # 22

# //=: Performs floor division of the variable on the left by the value on the right and updates the variable with the integer result.
var_one //= 5
print(var_one) # 4

# %=: Calculates the modulus of the variable on the left with the value on the right and updates the variable with the result.
var_one %= 3
print(var_one) # 4

# **=: Raises the variable on the left to the power of the value on the right and updates the variable with the result.
var_one **= 4
print(var_one) # 256

# 4. Logical Operators: Logical operators are used to perform logical operations on Boolean values (True or False) and evaluate the truthiness or falsiness of expressions.
# Logical AND (and): Returns True if both operands are True, otherwise, it returns False.
var_one = 1
var_one = 2
print(var_one > 0 and var_two > 0) # True
print(x > 0 and y < 0) # False

# Logical OR (or): Returns True if at least one of the operands is True, otherwise, it returns False.
print(x > 0 or y > 0) # True
print(x > 0 or y < 0) # True

# Logical NOT (not): Returns the opposite Boolean value of the operand. If the operand is True, not returns False, and if the operand is False, not returns True.
print(not (x > 0 or y < 0)) # False

# 5. Bitwise Operators: Bitwise operators are used to perform operations on individual bits of integers. 
var_one = 5
var_two = 3

# Bitwise AND (&): Performs a bitwise AND operation between two integers.
res = var_one & var_two
print(res) # 1

# Bitwise OR (|): Performs a bitwise OR operation between two integers.
res = var_one | var_two
print(res) # 7

# Bitwise XOR (^): Performs a bitwise XOR (exclusive OR) operation between two integers.
res = var_one ^ var_two
print(res) # 6

# Bitwise NOT (~): Performs a bitwise NOT operation on a single integer.
res = ~var_one
print(res) # -6

# Left Shift (<<): Shifts the bits of an integer to the left by a specified number of positions.
res = var_one << 2
print(res) # 20

# Right Shift (>>): Shifts the bits of an integer to the right by a specified number of positions.
res = var_one >> 2
print(res) # 1

# 6. Membership Operators: This operators are used to test for the membership of a value in a sequence, such as a string, list, tuple, set, or dictionary. Return either `True` or `False`.
# `in`: Evaluates to True if the value is found in the sequence.
# `not in`: Evaluates to True if the value is not found in the sequence.

# Using membership operator with list
languages = ["English", "Hindi", "Bengali", "Marathi"]
print("Python" in languages) # False
print("Python" not in languages) # True

# Using membership operator with strings
str = "My name is Rohit Sharma."
print("Rohit" in str) # True
print("Rohit" not in str) # False

# Using memberhip operator with dictionary
my_detail = {"name": "Rohit Sharma", "has_car": False, "project_code": 410002841.004}
print("name" in my_detail) # True
print("company_name" not in my_detail) # True

# 7. Identity Operators








