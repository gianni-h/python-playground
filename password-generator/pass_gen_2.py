#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# user input
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# define variables
random_characters = ""
random_numbers = ""
random_symbols = ""
password = ""
shuffled_password = ""

# get random characters
for char in range(0, nr_letters):
    # random.choice() 
    # selects random item from specified list
    random_characters += random.choice(letters)

# get random numbers 
for num in range(0, nr_numbers):
    random_numbers += random.choice(numbers)

# get random symbols
for sym in range(0, nr_symbols):
    random_symbols += random.choice(symbols)
    # line 34 can be simplified. No need for line 40
    


# put all generated characters into 1 string 
password += random_characters + random_numbers + random_symbols
# print(password)
# shuffle password 
# makes list of all characters inside variable password
char_list = list(password)
# shuffles all characters inside char_list
random.shuffle(char_list)
# turns char_list back into 1 string
shuffled_password = ''.join(char_list) # can also be done with for loop
# prints shuffled password
print(shuffled_password)