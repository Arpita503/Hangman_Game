#_ _ a _ _ 
"""
Suggestions to improve this 
1. Make use of regex to check if user has entered only alphabet
2. Introduce levels like easy/hard
3. create different categories which user can choose and the word belongs to that category: eg: animals, books etc
4. Improve the print messages
5. provide some interesting hints to the user!
"""
import random
from art import logo, stages
from words import word_List
from termcolor import colored

#  _ _ _ _ _  = display
#  _ _ a _ _
# user makes a guess -> if the user guesses correctly we fill in the blank
# if user makes an incorrect guess - we decrease life
# cotinue till the game ends

end_of_game = False
chosen_word = random.choice(word_List)
word_length = len(chosen_word)
lives = 6

print(logo)

# create a blank display for the word
display = ["_"] * word_length

# Main game loop
# for _ in range(word_length):
#     display += " "

while not end_of_game:
    # User makes a guess
    guess = input(colored("Guess a letter: ", "yellow")).lower()

    # if guess == int:
    # print("Not a valid letter. Please try again.")

    if guess in display:
        print(colored(f"You've already guessed this letter {guess}!\n\n", "red"))
        continue

    #Flag to track whther the guess is correct 
    correct_guess = False

    # Update the display if the guess is correct
    for position in range(word_length):
        # chosen word = bcadb
        # guess by user is a 
        # initially display _ _ _ _ _
        # after display _ _ a _ _ 
        letter = chosen_word[position]
        if letter.lower() == guess:
            print(colored("WOW!!. . .You've guessed it correctly", "green"))
            display[position] = letter 
            correct_guess = True
            

    # check if user has made a wrong guess
    if guess not in chosen_word:
        print(colored("You Guessed it incorrectly. You have lost a life!!!!", "red"))
        lives = lives-1
        print(stages[lives]) # print the current stage of the hangman.

        if lives == 0:
            end_of_game = True
            print("!!. ._YOU ARE HANG TILL DEATH_. .!!")
            print(colored("As You lost the game. . .You have 0 lives!!", "\nThe word was: ", chosen_word, "red"))

    # print the current display    
    print(colored(f"{' ' .join(display)}", "cyan")) #"seprator".join(list) [.join is use to convert a list to a string]

    # check if the user has won
    if "_" not in display:
        end_of_game = True
        print(colored("Hurray!! you've guessed correctly and won the game!!!", "yellow"))

print(colored(stages[lives], "green"))
    #You should print the solution     