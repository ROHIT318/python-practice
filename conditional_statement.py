# is a fundamental control flow construct that allows you to make decisions in your code. It enables you to execute different blocks of code based on whether a specified condition is True or False.
condition_one = True
condition_two = True

if condition_one:
    print("I am inside if")
else:
    print("I am inside else")

print('----')

condition_one = False
if condition_one:
    print("I am inside if")
elif condition_two:
    print("I am inside else if")
else:
    print("I am inside else")
    
print('----')

condition_two = False
if condition_one:
    print("I am inside if")
elif condition_two:
    print("I am inside else if")
else:
    print("I am inside else")

print('----')

# It is a control flow statement that repeatedly executes a block of code as long as a specified condition is True.

count = 1 
while count <= 5:
    print(count)
    count += 1
print('----')

# It  is a control flow statement that iterates over a sequence such as a list, tuple, string, or range.

list = [1,2,3,4,5]
set = {'a', 'e', 'i'}
dict = {'name': "Rohit Sharma", 'has_bike': False}

for item in list:
    print(item)
print('----')
for item in set:
    print(item)
print('----')  
for item in dict.values():
    print(item)
print('----')

print('---')
# Terminates the loop, when a condition is met.
count = 1
while count <= 5:
    if count == 4:
        break
    print(count)
    count += 1

print('----')
# Skips the current iteration and moves to the next iteration.
list = [1,2,3,4,5]
for item in list:
    if item == 4:
        continue
    print(item)

# Acts as a placeholder to indicate that no action is required in a code block.
condition_one = False
if condition_one: 
    pass
else:
    print("I am inside else")