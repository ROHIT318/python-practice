# Data types: 
# 1) None: When a value is not assigned to any variable, then it stores None (in other languages Null)
var = None
print(var)
print('----')
# 2) Numeric:
    # 1) int: An int data type variable is a variable that holds an integer value. Integers are whole numbers without any fractional part or decimal point. They can be positive, negative, or zero. Ex =>
var = 5
var = 0
var = -1
print(var)
print(type(var))
print('----')
    # 2) float: The float data type represents floating-point numbers, which are numbers with a decimal point.
var = 0.2
var = -0.1
print(var) 
print(type(var)) 
print('----')
    # 3) complex: The complex data type represents complex numbers, which are numbers with both real and imaginary parts.
var = complex(1,2)
var = complex(-1,-2)
print(var)
print(type(var))
print('----')
    # 4) bool: The bool data type represents Boolean values, which are a type of data with only two possible values: True or False.
var = True
var = False
print(var)
print(type(var))
print('----')
# ----------------------Sequence------------------ 
# 3) List: The list data type is used to represent a collection of items or elements in an ordered and mutable sequence. Items can be of different data types. 

# Declaration
var = [1,2,"Rohit", True]

# Indexing
print(var[0]) # 1
print(var[3]) # True

# Slicing
print(var[0:1]) # [1]
print(var[:2])  # [1,2]
print(var[2:])  # ['Rohit', True] 

# Nested list
var_one = [1,2,3]
var_two = ['one', 'two', 'three']
var_merge = [var_one, var_two]
print(var_merge)

# Working with functions
# Addition
var.append([1,2])
print(var)
var.extend([1,2])
print(var)
print(var.insert(3, 'Sharma'))

# Removing
print(var.pop(0))
print(var)
print(var.remove(2))
print(var)
print(var.pop())


print(var)
print(type(var))
print('----')
# 4) Tuple: A tuple is a data type used to represent an ordered and immutable collection of elements. Similar to lists, tuples can hold elements of different data types, such as integers, strings, floats, or even other tuples.
# Declaration
tpl = (1,"Rohit",True)
print(type(tpl)) # <class 'list'>
print(tpl)       # (1, 'Rohit', True)

# Indexing and slicing
print(tpl[1])  # Rohit
print(tpl[:1]) # (1, )
# tpl[1] = 2
print(type((1)))  # <class 'int'>
print(type((1,))) # <class 'tuple'>

# Nested tuple
nest_tpl = (1,2,3,(1,2))
print(nest_tpl) # (1,2,3,(1,2))

print('----')
# 5) Set: A set is a data type used to represent an unordered collection of unique elements.
set = {3, 3, 2, 0, True, "Rohit", False}
print(set)          # {0, True, 2, 3, "Rohit"}
print(type(set))    # <class 'set'>

# Add/Remove
set.add("Sharma")   
print(set)          # {0, True, 2, 3, "Rohit", "Sharma"}
set.remove(False)
print(set)          # {True, 2, 3, "Rohit", "Sharma"}

print('----')
# 6) String:  A string is a data type used to represent a sequence of characters.
var_str = "I am learning Python language"
print(var_str) # I am learning Python language
mult_str = """
    I am writing a story.
    Once upon a time....
"""
print(mult_str)
print(type(mult_str))
print(len(var_str))

# Indexing
print(var_str[0])
print(var_str[3])
print(var_str[-1])

# slicing
print(var_str[3:6])
print(var_str[:4])

# Comma issue
comma_str = "A comma' string"
print(comma_str)

# Formatted strings
ques = "What you doing?"
ans = "Learning Python"
ques_ans = ques + ans
# print(ques_ans)
print("{} {}".format(ques, ans))

# String Methods
print(comma_str.upper())
wrong_data = "   Hello Progrummers"
print(wrong_data)
print(wrong_data.strip())
print(wrong_data.find("Pro"))
print(wrong_data.replace("u", "a"))
print('----')


# 7) Range: 
# ----------------------Sequence--------------------
# 8) Dictionary: (or mapping) All the keys has to be unique. 
d = {'1': "Rohit", 2: "Rahul", 3: "Amit"}
print(d.keys())
print(d.values())
print(d['1'])
print(d.get(3))


# Typecasting:  Typecasting (also known as type conversion) refers to the process of changing the data type of a variable from one data type to another. 
