# Required Arguments: Function will throw an error if argument not provided. Position should remain same.
def req_arg_func(a: int,b: int) -> None:
    print(f'{a} and {b}')

req_arg_func(1,2)

# Keyword arguments: It is an argument which is passed to function using parameter name. Order in which arguments are passed doesn't matter.
def key_arg_func(c: int=None, d: int=None) -> None:
    print(f'{c} and {d}')

key_arg_func(d=5, c=10)

# Default arguments in Python. Non-default argument should be present before default arguments.
def def_arg_func(e: int, f: int, g: int = 5) -> None:
    print(f'{e}, {f}, {g}')

def_arg_func(4, 5)


# Arbitrary arguments/variable length in python: This is used when number of arguments to be passed are not known beforehand.
# 1. We are aware that number of arguments passed will be 3
def fixed_args_func(*args) -> None:
    print(args[0])
    print(args[1])
    print(args[2])

fixed_args_func('Rohit', 'Rahul', 'Amit')

# 2. Not sure about number of argumemts to be passed
def u_args_func(*args) -> None:
    for i in args:
        print(i, end=' ')

u_args_func('Rohit', 'Rahul', 'Amit')


# Arbitrary keyword arguments in python. When we don't know about number of argumets but are aware of keywords to be passed.
def kwargs_func(**kwargs) -> None:
    print(f'\n{kwargs["h"]} and {kwargs["i"]}')


kwargs_func(h=1, i=2)


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

