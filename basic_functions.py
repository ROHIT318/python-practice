# First class function is a function that treats its function as first class citizen. A first class citizen in a programming language is an entity which supports all the operations available to other entities. Like being passed as an argument, return from a function and assigned to variable.
def a_func(name: str) -> str:
    return name.upper()
## Assigning function to a variable
new_func = a_func
# print(new_func("Rohit"))
## Our own map function to illustrate First-class function
def upper_map_func(func, names: list) -> list:
    names_upper = []
    for name in names:
        names_upper.append(func(name))
    return names_upper
## Passing function as an argument
name_caps = upper_map_func(a_func, ["Rohit", "amit", "raHul"])
# print(name_caps)

## Returning a function
def return_function(name: str) -> callable:
    print("Inside return function")
    def return_str_function(func) -> callable:
        return map(func, name)
    return return_str_function
# str_func_upper = return_function('rohit')
# results = str_func_upper(str.upper)
# for res in results:
#     print(res)
# str_func_lower = return_function('ROHIT')
# results = str_func_lower(str.lower)
# # for res in results:
#     print(res)


# A closure is a concept in which we store a function together with its variable.
def outer_func(msg):
    message = msg
    def inner_func():
        print(message, end=' ')
    return inner_func
# first_name_func = outer_func("Rohit")
# first_name_func()
# last_name_function = outer_func("Sharma")
# last_name_function()


# Decorator function: It is a function that is used to extend the functionality of an existing function without changing its actual code. It can be used in logging.
def logging_decorator(func: callable) -> callable:
    print("Logging has started....")
    
    def wrapper(*args, **kwargs) -> str:
        print("Create log file...")
        output = func(*args, **kwargs)
        print("Completed log file creation....")
        return output
    
    print("Logging is completed.")
    return wrapper

## Declaring original_function as a decorator function
@logging_decorator
def original_function(fname: str, lname: str) -> str:
    return f'{fname} {lname}'

# original_function(fname="Rohit", lname="Sharma")
fun = original_function
print(fun(fname="Rohit", lname="Sharma"))


# Required Arguments: Function will throw an error if argument not provided. Position should remain same.
def req_arg_func(a: int,b: int) -> None:
    print(f'{a} and {b}')
# req_arg_func(1,2)

# Keyword arguments: It is an argument which is passed to function using parameter name. Order in which arguments are passed doesn't matter.
def key_arg_func(c: int=None, d: int=None) -> None:
    print(f'{c} and {d}')
# key_arg_func(d=5, c=10)

# Default arguments in Python. Non-default argument should be present before default arguments.
def def_arg_func(e: int, f: int, g: int = 5) -> None:
    print(f'{e}, {f}, {g}')
# def_arg_func(4, 5)


# Arbitrary arguments/variable length in python: This is used when number of arguments to be passed are not known beforehand.
# 1. We are aware that number of arguments passed will be 3
def fixed_args_func(*args) -> None:
    print(args[0])
    print(args[1])
    print(args[2])
# fixed_args_func('Rohit', 'Rahul', 'Amit')

# 2. Not sure about number of argumemts to be passed
def u_args_func(*args) -> None:
    for i in args:
        print(i, end=' ')
# u_args_func('Rohit', 'Rahul', 'Amit')


# Arbitrary keyword arguments in python. When we don't know about number of argumets but are aware of keywords to be passed.
def kwargs_func(**kwargs) -> None:
    print(f'\n{kwargs["h"]} and {kwargs["i"]}')
# kwargs_func(h=1, i=2)

# Map: Apply a function to all elements of an iterable. map(function, iterable). It returns a map object, so type cast it into an iterable.
iter = [1,2,3,4,5,6]
print(list(map(lambda x: x**2, iter))) # [1, 4, 9, 16, 25, 36]

# Filter: Use to retain elements from a collection of elements. i.e. iterables. filter(condition, iterable). It returns a filter object, so type cast it into an iterable.
iter = [1,2,3,4,5,6]
print(list(filter(lambda x: x%2==0, iter))) # [2, 4, 6]

# Sorted: Used to sort an iterable, based on certain condition. Returns a list object, no type casting needed. sorted(iterable, key); key is the one on which sorting will be applied.
iter = [('a', 1), ('c', 2), ('d', 4), ('b', 3)]
print(sorted(iter, key=lambda x: x[1]))         # [('a', 1), ('c', 2), ('b', 3), ('d', 4)]
print(sorted(iter, key=lambda x: x[0]))         # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]


# exec: It is used to execute the code dynamically
iter = ['print(1, end=" ")', 'print(2, end=" ")', 'print(3, end=" ")']
for i in iter:          # 1 2 3
    exec(i)  


# Generators: They don't create the entire data in one go and store in memory. Instead they yield data as and when required. square_numbers returns a generator object need to pass it to 'next' in order to get the actual element
print()
def square_numbers(iter):
    for i in iter:
        yield i*i
iter = [1,2,3,4,5,6]
square = square_numbers(iter)
print(next(square)) # 1
print(next(square)) # 4
print(next(square)) # 9
print(next(square)) # 16
print(next(square)) # 25
print(next(square)) # 36
# print(next(square)) # Error: StopIteration, cause ran out of elements.



# Print function
# It is a built-in function used to display output or information to the console or standard output stream.
# print(arg1, arg2, arg3, ...., sep=' ', end='\n', file=sys.stdout, flush=False)
# arg1, arg2, arg3, ....: The values to be printed
# sep: To separate the arguements. Optional, default=' '
# end: Character to be printed at the end of statement. Optional, default='\n'
# flush: To force the output to flush immediately or not. Optional, default=False 

# Input function
# It  is a built-in function used to read user input from the console.
# var = input(prompt)
# prompt: The string argument provided to input() that serves as the prompt displayed to the user.

