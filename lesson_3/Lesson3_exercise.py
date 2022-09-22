# # Lesson 3
# # UPPGIFT A extra
# # exercise 2

# X = 1
# Y = 4

# addresses = {"Adam": "Ormvägen 5",
#              "Bella": "Klockgatan 1",
#              "Cornelia": "Vikingagatan 3"}

# cars = ["Volvo", "Opel", "Bmw"]
# numbers1 = {1,2,3,X,6}
# numbers2 = {Y,2,3,4,7}

# # 1. Vilken datatyp har variablerna X och Y?
# # Svar: integer variables

# # 2. Vilken datatyp har variabeln addresses?
# # Svar: string variables

# # 3. Hur kan man få ut bellas adress ur variabeln addresses?
# X = 1
# Y = 4

# addresses = ["Adam", "Ormvägen 5",
#              "Bella", "Klockgatan 1",
#              "Cornelia", "Vikingagatan 3"]

# cars = ["Volvo", "Opel", "Bmw"]
# numbers1 = {1,2,3,X,6}
# numbers2 = {Y,2,3,4,7}


# print (addresses[2])

# # 4. Vad händer om man skriver addresses[“Daniel”] = “Prinsgränd 2”?

# #Svar:
# # om jag ändrar koden  från: addresses[“Daniel”] = “Prinsgränd 2”
# # till: addresses["Daniel"] = "Prinsgränd 2" det fungerar bra.
# # Dokumentet Cittatecken funkar inte i python.
# addresses = {"Adam": "Ormvägen 5",
#              "Bella": "Klockgatan 1",
#              "Cornelia": "Vikingagatan 3"}
# addresses["Daniel"] = "Prinsgränd 2"

# print(addresses)


# #5. Få ditt program att skriva ut hur många keys addresses har

# addresses = {"Adam": "Ormvägen 5",
#              "Bella": "Klockgatan 1",
#              "Cornelia": "Vikingagatan 3"}

 

# print(addresses.keys())

# # 5.1. Utöka programmet så att adressen skrivs ut till den personen som
# # kommer sist i bokstavsordning.

# addresses = {"Adam": "Ormvägen 5",
#              "Bella": "Klockgatan 1",
#              "Cornelia": "Vikingagatan 3"}


# print(sorted(addresses, reverse=True))


# # 5.2 Utöka programmet så att namnet skrivs ut på den personen som bor
# # på adressen som kommer först i bokstavsordning. Tips: följande rad
# # byter plats på keys och values i my_dict:
# # my_dict = {v: k for k, v in my_dict.items()}
# # Förklaring kommer nästa lektion!


# addresses = {"Adam": "Ormvägen 5",
#              "Bella": "Klockgatan 1",
#              "Cornelia": "Vikingagatan 3"}

# print(addresses['Adam'])
# print(addresses['Bella'])
# print(addresses['Cornelia'])
# addresses.sort()
# print(addresses)

# # 6. Vilken datatyp har variabeln cars?
# # Svar: integers

# # 7. Vad returneras om man skriver cars[X]?
# # Svar: NameError: name 'cars' is not defined

# # 8. Vad returneras om man skriver cars[Y], varför?
# # Svar: NameError: name 'cars' is not defined
# # cars[Y] position belongs to number 4, which makes the list index out of range.
# # X = 1
# # Y = 4 
# # cars = ["Volvo", "Opel", "BMW"]
# # numbers1 = {1, 2, 3, X, 6}
# # numbers2 = {Y, 2, 3, 4, 7}
# # cars[Y]
# # print(cars)

# # 9. Vad returneras om man först skriver cars.sort() och på nästa rad skriver cars[0]?
# # Svar: ['BMW', 'Opel', 'Volvo']


# #10. Skapa en ny variabel genom att skriva cars_2 = cars, och på följande rad ska
# # strängen “Saab” läggas till cars med hjälp av append(). Notera att det alltså
# # bara är ena variabeln som ska utökas. Vad innehåller variablerna cars_2 och
# # cars nu? Förklara!

# # Svar: We created a new variable which we made it equal to the cars and then we added an extra string to the variable , its always added in the last position.
# # Prints: ['Volvo', 'Opel', 'Bmw', 'saab']


# # 10.1. Skapa ytterligare en variabel cars_3 som får sina element av cars
# # men som inte påverkas av vad som läggs till i cars
# # Svar: 
# cars = ["Volvo", "Opel", "Bmw"]
# cars_2 = cars
# cars_3 =  cars[:]
# cars_2.append("saab")
# print(cars)
# print(cars_2)
# print(cars_3)

# # 10.2. Utöka variabeln cars så att den innehåller dubbletter av varje bilmärke
# # sorterat i omvänd bokstavsordning.
# # Svar:
# cars = ["Volvo", "Opel", "Bmw"]
# cars_dublicate = cars * 2
# cars_dublicate.sort()
# cars_dublicate.reverse()
# print(cars_dublicate)

# # 10.3. Från den utökade versionen av cars ifrån förra uppgiften, skapa
# # variabeln unique_cars som ska vara en lista där varje bilmärke finns
# # med exakt en gång
# # Svar:
# cars = ["Volvo", "Opel", "Bmw"]
# unique_cars = [cars]
# cars_dublicate = cars * 2
# cars_dublicate.sort()
# cars_dublicate.reverse()
# print(unique_cars)

# #11. Vilken datatyp har variablerna numbers1 och numbers2?
# # Svar:
# # strings och integers

# #12. Vilka värden finns lagrade i variablerna numbers1 och numbers2?
# # Svar:
# # numbers1 = {1, 2, 3, X, 6}
# # numbers2 = {Y, 2, 3, 4, 7}

# #13. Vad är snittet (intersection) mellan variablerna numbers1 och numbers2?
# # Svar:
# X = 1
# Y = 4
# numbers1 = {1,2,3,X,6}
# numbers2 = {Y,2,3,4,7}
# print(numbers1.intersection(numbers2)) 
# # {2,3} is the interection between numbers1 and numbers2

# #14. Vad är unionen mellan variablerna numbers1 och numbers2?
# # Svar:
# # De är båda variables.

# #15. Vilken är den symmetriska differensen mellan numbers1 och numbers2?
# # Svar:
# X = 1
# Y = 4
# numbers1 = {1,2,3,X,6}
# numbers2 = {Y,2,3,4,7}
# print(numbers1.symmetric_difference(numbers2))
# # {1, 4, 6, 7} is the symmetric difference



# ## `Exercise 3` Boolean Operations - and, or, not

# #Create a program that creates three variables x, y, z as booleans. You can modify these variables to test your expressions.

# #```python
# x = True
# y = False
# z = True
# #```

# # 1. Write a expression with Boolean Operations that:

# #1. result in True if any of x, y, z is True
# x or y or z
# #2. result in True if all x, y, z is True
# x and y and z
# #3. result in False if any of x, y, z is False
# x and y and z 
# #4. result in False if all of x, y, z is False
# x or y or z 
# #5. result in False if any of z, y, z is True
# not( x or y or z)
# #6. result in False if all of z, y, z is True
# not (x and y and z)




# ### `Exercise 4` Data Structure - List

# #1. Create a empty list
# new_list = []
# #2. Create a string that is a color e.g "red"
# string_color = "red"
# #3. Add the color to your list
# new_list.append(string_color)
# #4. Print the color from the list using [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) indexing for `0` i.e my_list[0]
# print(new_list[0])
# #5. Add two other color to the list
# new_list.append("green")
# new_list.append("blue")
# print(*new_list,sep = ",") 
# #6. Search for a color in the list using operation `x in s`
# for x in new_list:
#     print(x)

# #7. Verify that a color is not in the list using the operation `x not in s`
# not x in new_list

# #8. Create another list of colors and concatenate the two lists using the operation `s + t`
# list2 = ["yellow", "pink", "blue"] 
# lastlist = new_list + list2
# print(lastlist)

# #9. Create a list of two colors red, yellow with three of each color using the operation `s * n`

# twocolors_list = ["red", "yellow"]
# print(twocolors_list*3)

# #10. Print the first four colors in the list from (9) using the operation `s[i:j]`

# print(lastlist[0:4])

# #11. Count how many times "red" occur in the list using the operation `s.count(x)`

# print(lastlist.count("red"))
# #12. Print the index of the first occurrence of "yellow" in s using the operation `s.index("yellow")`
# print(lastlist.index("yellow"))

# #13. Print the total length of each array using the operation `len(s)`
# print(len(lastlist))

# #14. Create a list of 7 numbers
# list_numbs = [1, 2, 3, 4 ,6 ,7 ]


# # 1. Print the min value in the list

# print(min(list_numbs))

# # 2. Print the max value in the list

# print(max(list_numbs))

# ## `Exercise 5` Sorting
# #In LINKS_3.md there is a link Python guide how-to do [sorting](https://docs.python.org/3/howto/sorting.html). Create a list containing 10 car brand. i.e cars = ["volvo", ...]

# car_list = ["volvo", "audi", "mercedes", "toyota","ferrari", "ford", "lexus", "bmw", "mazda"]
# # 1. Sort the list with `sorted(cars)`
# sorted_cars = sorted(car_list)
# print(sorted_cars)
# # 2. Sort the list with `cars.sort()`
# car_list.sort()
# print(car_list)

# # 3. reverse the sort of both, read more about reversing in python docs [ascending-and-descending](https://docs.python.org/3/howto/sorting.html#ascending-and-descending)

# car_list.reverse()
# print(car_list)
