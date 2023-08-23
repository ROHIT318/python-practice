"""
Q1
Reverse each word of a string
Given:
str = 'My Name is Jessa'
Expected Output
yM emaN si asseJ
"""
# ------------------------
# str = 'My Name is Jessa'
# rev_str = ''
# list = str.split(' ')
# print(list)
# for element in list:
#     print(element[::-1], end=' ')
#     # rev_str = rev_str + ' ' + element[::-1]
#     # print(rev_str)
# # print(rev_str)
# ------------------------

"""
Q2
Filter dictionary to contain keys present in the given list
Given:
# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
# Filter dict using following keys
l1 = ['A', 'C', 'F']
Expected Output: -
new dict {'A': 65, 'C': 67, 'F': 70}
"""
# -------------------------------------
# d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
# l1 = ['A', 'C', 'F']
# for key in d1:
#     if key in l1:
#         print(d1[key], end=' ')
# # print(l1)
# -------------------------------------

"""
Q3
Read text file into a variable and replace all newlines with space
Given: Assume you have a following text file (sample.txt).
Line1
line2
line3
line4
line5
Expected Output:
Line1 line2 line3 line4 line5
"""
# ---------------------------------------
# import os
# res_content = ''
# with open('Desktop/Learning/PowerBI/PwC Assignment/sample.txt', 'r') as fh:
#     content_list = fh.read().split('\n')
# for item in content_list:
#     res_content = res_content + ' ' + item
# with open('Desktop/Learning/PowerBI/PwC Assignment/result.txt', 'w') as fh:
#     fh.write(res_content)
# ---------------------------------------

"""
Q4
In this question, You need to remove items from a list while iterating but without creating a different copy of a list.
Remove numbers greater than 50
Given:
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Expected Output: -
[10, 20, 30, 40, 50]
"""
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(number_list)
res_list = list()
for item in number_list:
    if item <= 50:
        res_list.append(item)
print(res_list)
