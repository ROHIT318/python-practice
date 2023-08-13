# 1) Reverse strings program (starts)
num = 190241

# Easiest method
num_str = str(num)
rev_num_str = num_str[::-1]
print(rev_num_str)

rev_num = 0
while num > 0:
    rev_num = (rev_num*10) + num%10
    num //= 10 

print(rev_num)
# 1) Reverse strings program (ends)

# 2) Whether an armstrong number? (Starts)
num = 153
temp_var = num
num_len = len(str(num)) 

cal_num = 0
while temp_var>0:
    cal_num += ((temp_var%10) ** num_len) 
    temp_var //= 10

if cal_num == num:
    print("ArmStrong Number ....")
else:
    print("Random Number .....")
# 2) Whether an armstrong number? (ends)


# 3) Calculate radius of a circle (starts)
rad = 5
pi = 3.141
area = pi * (rad**2)
print(area)
# 3) Calculate radius of a circle (ends)

# 4) Genarate a list from a string separated by commas (starts)
var = "1,2,3,4"
var_list = var.split(",")
print(var_list)
print(type(var_list))
# 4) Genarate a list from a string separated by commas (ends)

# 5) Write a Python program that accepts a filename from the user and prints the extension of the file. (starts)
file_name = "some file.cpp"
file_ext = file_name.split(".")
print(file_ext[-1])
# 5) Write a Python program that accepts a filename from the user and prints the extension of the file. (ends)

# 6) To insert element in the middle of the list (starts)
list = [0,1,2,4,5]
print(list)
to_ins = 3
index_num = len(list)//2 + 1
list.insert(index_num,3)
print(list)
# 6) To insert element in the middle of the list (ends)	

# 7) Difference between number and 100, negative result then twice and absolute of result otherwise difference itself. (starts)
var = 10
diff = var - 100

if diff > 0:
    print(diff)
else:
    print(abs(diff)*2)
# 7) Difference between number and 100, negative result then twice and absolute of result otherwise difference itself. (ends)