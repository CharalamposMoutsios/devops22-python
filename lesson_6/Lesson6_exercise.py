## `Exercise 1` Dataset

# Todays exercises requires that you generate test data. You can generate data in multiple ways i.e manually through loops, using `random` module or list comprehension. See examples in `8_data.py`.

# 1. Generate a list containing the numbers 1, 2, 3 to 100.
# 2. Generate a list of all even numbers from 2 to 60
# 3. Generate a list of all odd numbers from 1 to 77
# 4. Generate a list of 100 numbers between 1 - 300
#     1. The numbers must be unique
#     2. The numbers are selected randomly (not unique)
# 5. create a list containing five colors (not containing red)
#    1. Create a new list containing "red" and also add two colors by random with `choice`, `choices` or `sample` from the list.
#    2. Generate a list of random colors from the list of 3, the list should be of length 50.
#    3. Print the length of all three lists and the unique colors in each list

# ----exercise1---
# list_num =[]
# list_num = [x for x in range(1, 101)]
# print(list_num)

#alternative svar

# list(range(1,101))
# print(list)


#------Even number------

# for i in range(0,62,2):
#   print(i, end = " ")

#alternative svar

# list(range(1,61,2))
# print(list)


# #-----Odd number------

# start, end = 1, 77
# for num in range(start, end + 1):
#     if num % 2 != 0:
#         print(num, end = " ")

#alternative svar

# list(range(1,78,2))
# print(list)

#-----100 unique numbers-----

# from random import sample
# total_numbers = list(range(1, 301))
# list_of_a_hundred = sample(total_numbers, k=100)
# print(list_of_a_hundred)

#-----100 random numbers--------

# from random import choices
# population = list(range(1, 301))
# hundred_numbers = choices(population, k=100)
# print(hundred_numbers)

# 5 color list

# from random import Random, sample
# from random import choice
# from random import choices
# from xmlrpc.server import list_public_methods

# list_color = ["blue","white","black","grey","green"]
# new_colors =["red"]
# new_colors.extend(sample(list_color, k=2))
# # print(new_colors)
# random_colors = choices((new_colors),k=50)
# # print(random_colors)
# unique_colors = set(list_color)
#----------------> ???
# colors_string = ", ".join()
#----------------> ???
# print(f'{len(list_color)} {unique_colors}')
# print(f'{len(new_colors)} {", ".join(set(new_colors))}')
# print(f'{len(random_colors)} {", ".join(set(random_colors))}')



# ## `Exercise 2` Name Counter

# 1. Generate a list with 100 elements, i.e ["johan", "lisa", "johan", "tove"...]
# 2. Count the names i.e ('lisa', 1), ('johan',2)
# 3. Print the top 3 most popular names
# 4. Print the least popular name[s]
# 5. Print all unique names
#    1. In alphabetical order
#    2. Shuffled
#    3. In reversed alphabetical order

#First

from random import choices
from unicodedata import name
names = choices(["johan","lisa","johan","tove"], k=100)
# print(names)
#Second
from collections import Counter
name_counter = Counter(names)
print(name_counter)
#Third
print(name_counter.most_common(3))
#Forth
print(name_counter.most_common()[-1])
#Fifth
#1.
unique_names=sorted(list(set(names)))
print(unique_names)
#2.
from random import shuffle
shuffle(unique_names)
print(unique_names)
#3
unique_names.sort(reverse=True)
print(unique_names)
