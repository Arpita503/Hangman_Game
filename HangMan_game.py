import random
from art import logo, stages
from words import word_List
from termcolor import colored

end_of_game = False
chosen_word = random.choice(word_List)
word_length = len(chosen_word)
lives = 6

print(logo)

# create a blank display for the word
display = ["_"] * word_length

while not end_of_game:
    # User makes a guess
    guess = input(colored("Guess a letter: ", "yellow")).lower()

    if guess in display:
        print(colored(f"You've already guessed this letter {guess}!\n\n", "red"))
        continue

    #Flag to track whther the guess is correct 
    correct_guess = False

    # Update the display if the guess is correct
    for position in range(word_length):
        
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
    print(colored(f"{' ' .join(display)}", "cyan")) 

    # check if the user has won
    if "_" not in display:
        end_of_game = True
        print(colored("Hurray!! you've guessed correctly and won the game!!!", "yellow"))

print(colored(stages[lives], "green"))
    #You should print the solution     
