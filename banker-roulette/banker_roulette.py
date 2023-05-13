import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# check code
# print(names)
# print("\n")
you_pay = random.choice(names)
print(f"{you_pay} is going to buy the meal today!")
print("\n")


########################### version without using random.choice()

# list_length = len(names)

# # check code
# # print(list_length)
# # print("\n")

# #my_list =         ["A", "B", "C"]
# #index of my_list    0    1     2
# #
# #
# #index starts at 0
# #if last item in list is 5th item, index nr is 4!!!
# random_list_nr = random.randint(0, (int(list_length)-1))

# # check code
# # print(random_list_nr)
# # print("\n")

# you_pay_2 = names[random_list_nr]
# print (f"{you_pay_2} is going to buy the meal today!")