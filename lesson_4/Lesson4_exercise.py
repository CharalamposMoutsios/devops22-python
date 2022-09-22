# ### `Exercise 1` even or odd

# # Write a program that fulfills the specification:

# # 1. Ask the user for a integer

# user_input = int(input("Enter a integer: "))
# print(user_input)

# 2. If the integer is even, print even

#------------1 alternative--------
# if user_input % 2  == 0:
#     print(" {0} is a even number" .format(user_input))
# # 3. If the integer is odd, print odd
# else:
#     print("{0} is an odd number" .format(user_input))

#------------2 alternative---------
# if user_input % 2:
#     print("this is an even number")
# else:
#     print("This is an odd number")
    
    


# # ### `Exercise 2` VIP

# # Write a program that fulfills the specification:

# # 1. Ask the user for a name

# ask_name = input("Enter your name: ")

# # 2. Create a tuple with at least five names

# names_list = ("John","Nick","Morgan","George","Oscar")

# 3. If the user input is in the tuple, print the text "Welcome {name} your are on the list".
#-----------1 alternative----------
# if ask_name in names_list:
#     print("Welcome " + ask_name + " you are on the list")
# # 4. If the user input is not in the tuple, print "Sorry, you are not on the list".
# else:
#     print("Sorry, you are not on the list")
# 
# #------------2 alternative------------
# if ask_name in names_list:
#     print(f' Welcome {ask_name} you are in the list ')
# else:
#     print(f'{ask_name} you are not in the list ')
### `Exercise 3` Repeat word1

# Write a program that fulfills the specification:

# 1. Ask the user for a word

# word_user = input("Write a word: ")

# # 2. Print the word x times, where x = len(word). i.e if the word is `hello` the program writes:


# #     ```text
# #     hello
# #     hello
# #     hello
# #     hello
# #     hello
# #     ```

# for _ in range(len(word_user)):
#     print(word_user)

# ### `Exercise 4` Sum

# # Write a program that fulfills the specification:

# # 1. Ask the user for a start and stop integer

# start_number = int(input("Write a start number: "))
# stop_number = int(input("Write a stop number: "))


# # 2. Print every integer between start and stop. i.e. start = 1, stop = 5 would print:

# total = range(start_number, stop_number)
# for every in total:
#     print(every)
# 1
# #     ```text
# #     1
# #     2
# #     3
# #     4  
# #     ```


# # # 3. Print the sum of all integers i.e
# sum_result = sum(total)
# print(sum_result)

# # #     ```text
# # #     Sum: 10
#     ```

### `Exercise 5` Until stop

# Write a program that fulfills the specification:

# 1. Create a while loop that runs forever
# 2. In each iteration, input a text
# 3. In each iteration, print a text "Enter `stop` to quit: "
# 4. If the text equals stop, break the while loop
# 5. If the text don't equals stop, print the text and the length of the text


# x = 0
# while True:
#     text = input(" Enter a text ")
#     print(x)
#     if text == 'stop':
#         break
#     else:
#         print(f'{text} has length {(len(text))}')