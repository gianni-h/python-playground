import random
import os
import hangman_art
import hangman_words
# assign variables
stages = hangman_art.stages
word_list = hangman_words.word_list
logo = hangman_art.logo
index = 0 #index count in for loop
display = [] # empty list to store '_'
guess = "" # character guess from user input
lives = 6 # lives player starts with
feedback = ""
command = 'cls' if os.name == 'nt' else 'clear' # check OS and use appropriate command to clear
total_wrong_guesses = []

chosen_word = random.choice(word_list) # choose random word from word_list
char_list = list(chosen_word) # splits chosen words in separate characters and saves them in list

# add '_' for each char in chosen word
for _ in chosen_word: # or use for _ in range(len(chosen_word)). for loop runs the range of chosen_word
    display += "_" # adds '_' for each char in the chosen_word

print(logo)

# run game until word guessed or user has lives
while display != char_list and lives > 0: 
    # user input
    guess = input("Guess a letter: ") 
    os.system(command) # clear screen
    guess = guess.lower() # turns input to lower case
    already_guessed = False # reset guess history checker
    print(f"You guessed {guess}")

    # check if (wrong) guessed letter is already guessed. Let user know. Forgive
    for char in total_wrong_guesses:
        if guess == char:
            print(f"That's not in the word.\nBtw, you already guessed this letter.")
            already_guessed = True
    
    # check if (correct) guessed letter is already guessed
    for char in display: # run through guessed letters
        if guess == char: # if input has already been guessed
            feedback = f"Hey, you've already guessed this letter!" # let user know
            print(feedback)
    
    # is guessed letter in the chosen word?
    for char in chosen_word: # no need to turn string into list with chars 
        # yes!
        if guess == char:  
            display[index] = guess # replace '_' with guessed letter
        index += 1 # increase index with each iteration
    index = 0 # reset index for next iteration
    
    # Let user know he/she guessed wrong
    if guess not in chosen_word and already_guessed == False: # guess char is not in chosen_word and hasn't been already guessed.
        lives -= 1 # reduces lives for mistake
        total_wrong_guesses += guess # add guess to the already (wrong) guessed letters
        feedback = f"Hmm, that's not in the word. Too bad, you lose a life... :'(" # user feedback
        print(feedback)
    
    print(stages[lives]) # Graphic representation of lives left. Index of stages is equal to lives left.
    
    ## check code ##
    # print(lives)
    
    # print(total_wrong_guesses)
    # print(f"Word to guess as list: {char_list}")
    # print(f"Word to guess(str): {chosen_word}", type(chosen_word))
    # print(f"Lives left(int): {lives}")
    # print(f"Guessed letters that are RIGHT(list): {display}")
    # print(f"Guessed letters that are WRONG(list): {total_wrong_guesses}")
    
    # put display list into single string to compare against chosen word
    display_string = ' '.join(display) # ' ' acts as separator between items in list when put together. 
    print(display_string)

# check code
# print(display_string, type(display_string))
# print(chosen_word, type(chosen_word))
if display == char_list:
    print("You win! :D")
else:
    print("You hang... D:")