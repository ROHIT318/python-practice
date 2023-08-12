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