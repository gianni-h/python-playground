import random
#defines images
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
fire = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣿⣿⣧⠀⠀⠀⠀⣰⠀⠀⠀⠀⠀⠀⠀⢳⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣷⣤⣤⣶⣿⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⢀⣿⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣟⠛⠿⢿⣿⣿⣦⣀⠀⠀⠀⣠⣾⣿⡿⢿⣷⡀⠀⠀
⠀⠀⣦⠀⠀⠀⠀⠀⠘⣿⣿⣆⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⡇⠈⢿⣷⠀⠀
⠀⢸⣿⡀⠀⠀⠀⠀⠀⢹⣿⣿⣆⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⡟⠀⠀⢸⣿⡇⠀
⠀⢸⣿⣧⠀⠀⠀⠀⠀⢸⣿⣿⣿⡀⠀⠀⣀⡀⠀⠀⠈⠻⠏⠀⠀⠀⢸⣿⣿⠀
⠀⢸⣿⣿⣷⣄⡀⢀⣠⣿⣿⣿⣿⡇⠀⠀⠈⣿⣷⣦⡀⠀⠀⠀⠀⠀⢸⣿⣿⠀
⠀⠘⣿⣿⣿⣿⣿⣿⡿⠟⠋⣿⡿⠀⠀⠀⠀⣿⣿⣿⣷⠀⠀⠀⠀⠀⣼⣿⡏⠀
⠀⠀⠹⣿⣿⣿⣿⠋⠀⠀⠀⠋⠀⠀⠀⠀⣰⣿⣿⣿⣿⠀⠀⠀⠀⣴⣿⡿⠁⠀
⠀⠀⠀⠙⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⡿⠃⠀⠀⣠⣾⡿⠛⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠛⠓⠀⠀⠀⠀⠐⠚⠛⠛⠛⠛⠉⠀⠀⠐⠛⠉⠁⠀⠀⠀⠀⠀                                                                                                                                             
'''
#request user for input
your_choice = input("What do you choose? R for Rock, P for paper or S for scissors.\n ").lower()

#Your choice
if your_choice == "r" or your_choice == "rock":
    your_choice_text = "You chose: Rock\n"
    your_choice_image = rock
elif your_choice == "p" or your_choice == "paper":
    your_choice_text = "You chose: Paper\n"
    your_choice_image = paper
elif your_choice == "s" or your_choice == "scissors":
    your_choice_text = "You chose: Scissors\n"
    your_choice_image = scissors
elif your_choice == "fire" or your_choice == "f":
    your_choice_text = "You chose: Fire\n"
    your_choice_image = fire
else:
    input = 0
    your_choice_text="This tool is not used in the game."
    your_choice_image = ""

print(your_choice_text)
print(your_choice_image)

#generates random number for computer choice
computer_choice = random.randint(0,2)

#Computer choice
if computer_choice == 0:
    computer_choice_text = "Computer Chooses: Rock\n"
    computer_choice_image = rock
elif computer_choice == 1:
    computer_choice_text = "Computer chooses: Paper\n"
    computer_choice_image = paper
elif computer_choice == 2:
    computer_choice_text = "Computer chooses: Scissors\n"
    computer_choice_image = scissors
print(computer_choice_text)
print(computer_choice_image)

#Result
#output for computer_choice = rock
if computer_choice == 0 and (your_choice == "r" or your_choice == "rock"):
    result="It's a draw °__°"
elif computer_choice == 0 and (your_choice == "p" or your_choice == "paper"):
    result="You Win :D"
elif computer_choice == 0 and (your_choice == "s" or your_choice == "scissors"):
    result="You lose :c"
elif your_choice == "fire" or your_choice == "f":
    result = "Fire beats everything, always and ever. You win!"
elif input == 0:
    result = "This game can only be played with Rock, Paper or Scissors.\nPlease try again."

#output for computer_choice = paper
if computer_choice == 1 and (your_choice == "r" or your_choice == "rock"):
    result="You lose :c"
elif computer_choice == 1 and (your_choice == "p" or your_choice == "paper"):
    result="It's a draw °__°"
elif computer_choice == 1 and (your_choice == "s" or your_choice == "scissors"):
    result="You Win :D"
elif your_choice == "fire" or your_choice == "f":
    result = "Fire beats everything, always and ever. You win!"
elif input == 0:
    result = "This game can only be played with Rock, Paper or Scissors.\nPlease try again."

#output for computer_choice = scissors
if computer_choice == 2 and (your_choice == "r" or your_choice == "rock"):
    result="You Win :D"
elif computer_choice == 2 and (your_choice == "p" or your_choice == "paper"):
    result="You lose :c"
elif computer_choice == 2 and (your_choice == "s" or your_choice == "scissors"):
    result="It's a draw °__°"
elif your_choice == "fire" or your_choice == "f":
    result = "Fire beats everything. You win!"
elif input == 0:
    result = "This game can only be played with Rock, Paper or Scissors.\nPlease try again."

#prints result
print(result)