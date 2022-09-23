# firstname = "john"
# lastname = "smith"
# tele = "00468123456789"

# ### `Exercise 1` Basic usage


# 1. Print first,  lastname and tele on the same line
# 2. Create a variable fullname
# 3. Assign to the new variable fullname, firstname and lastname separated with a space.
# 4. Print the length `len()` of fullname, firstname and lastname
# 5. Print a escape sequence `\n` so the first line contains fullname, and the second line tele.
# 6. Write the fullname and tele with the four different methods:
#    1. Only using print() and string concatenation i.e "firstname" + " " ..
#    2. Using f-string
#    3. Using format, i.e print('{}'.format(firstname))
#    4. Using printf (%) syntax, i.e print('A name %s' % firstname)

# print(f'{firstname} {lastname} {tele}')
# fullname = f'{firstname} {lastname}'
# print(len(fullname), len(lastname), len(tele))
# print(f'{fullname} \n{tele}')
# print("----------")
# print(fullname, tele)
# print(f'{fullname} {tele}')
# print('{first} {last} {telefon}'.format(first=firstname, last=lastname, telefon=tele))
# print('%s'% fullname + " " + tele)

# ### `Exercise 2` Slice

# Slice can be used to get a substring, i.e to get all but last letter my_string[:-1], to get all except the first letter my_string[1:], to get three first letters my_string[:3]

# Docs about [slice](https://docs.python.org/3/library/functions.html#slice)

# 1. Use slice to get the first 5 characters i fullname
# 2. Use slice to get all characters except the first and last one
# 3. Use slice to get every other character, i.e abcdef would print ace. Print the result in uppercase.
# 4. Use slice to print a word backwards.
# 5. Use slice to get the 5th character
# john_smith
# 0123456789

# print(fullname[0:6])           -> #1
# print(fullname[1:9])           -> #2
# print((fullname[::2]).upper()) -> #3
# print(fullname[:-1])           -> #4
# print(fullname[5:6])           -> #5


# ### `Exercise 3` Unicode

# How to write a euro sign can be found at [Currency Symbols](https://www.unicode.org/charts/PDF/U20A0.pdf). How to write emoji can be found at [emoji](https://unicode.org/emoji/charts/full-emoji-list.html), you can also check the formal charts for [symbols](https://www.unicode.org/charts/#symbols) you use either name or code: \N{money-mouth face}, or code \U0001F911

# print('\N{money-mouth face}')
# print('\U0001F921')

# Write a program that fulfills the specification

# 1. Let the user input a price, i.e Your new car cost: 1000000
# 2. Add a currency symbol (not dollar) to the input string. ie. Your new car cost [$]
# 3. Depending on the price, respond with a matching emoji (you decide which ones) i.e if cost below 50000 use one emoji, if is above another one

# car_cost = int(input("Enter a price\U0001F4B2: "))
# print(f'{car_cost}\U0001F4B2')
# if car_cost < 500:
#     print('\U0001F600')
# else:
#     print('\U0001F605')
