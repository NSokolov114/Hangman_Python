# RPOJECT HANGMAN
import random      # random
import dictionary  # words and letters
import pictures    # welcome picture and gallows

# 1 print HANGMAN logo
print(pictures.welcome_msg)

# 2 choose the word (from the list in dictionary.py)
the_word = '0'
while len(the_word) < 10:                       # BONUS difficulty level - min length
    the_word = random.choice(dictionary.words)  # chooses a new one
    length = len(the_word)                      # calculates word's length
    
# print(f"The word is: {the_word}, it's length is {len(the_word)}.")
print(f'\nWelcome to the HANGMAN! Your word has {length} letters!\n')

# 3 list made of _ _ _ _ _ using calculated length
dashes = []                         # a list
dashes_str = ''                     # a string
for i in range (0,length):          # 
    dashes.append('_')              # adds _ for each letter in the word
    dashes_str += dashes[i] + ' '   # prepares a string for printing, adding spaces
print(dashes_str)                   # first time printing _ _ _ _ _
print()

# 4 list made of l e t t e r s of the word
w_o_r_d = []
w_o_r_d_str = ''
for i in range (0,length):
    w_o_r_d.append(the_word[i])

# 5 health, how many times a user can fail
health = 6 # can't go over 6 w/o adding items to the list in pictures.py

# 6 creating the while loop
guesses = []                                    # a list of all user inputs

while health > 0 and '_' in dashes:             # breaks when health == 0 or the word is revealed
    guess = input('Please, choose a letter.\n') # input 
    if guess not in dictionary.letters:         # check if input is correct, 1 English letter
        print('Wrong input')                    # wrong input, proceed to losing health
    else:
        guess = guess.upper()                   # converting to UPPERcase
        if guess not in guesses:                #
            guesses.append(guess)               # list of all user inputs
        if guess in w_o_r_d:                    # check if the word has this letter
            dashes_str = ''                     # clearing the dashes string
            for i in range(0, length):          #
                if guess == w_o_r_d[i]:         # looking for position of discovered letter
                    dashes[i] = w_o_r_d[i]      # replacing _ for this letter
                dashes_str += dashes[i] + ' '   # recreating _ X _ _ _ string, with letters
        else:
            health -= 1                         # bad guess, health decreases
            print(f"You chose letter {guess}, that's not in the word. You lose a life.")    
            print(pictures.gallows[health])     # printing gallows based on health
        print('')                               # empty line
        print(dashes_str)                       # _ X _ _ _
        print(f"\nYou checked the following letters: {guesses}") # showing which letters have been used
if health <= 0:                                 # hangman is hanging
    print(pictures.fail_msg)
    print(f"\nSorry, you lost! Your word was '{the_word}'.")
elif '_' not in dashes:                         # the word is revealed
    print(pictures.win_msg)
    print(f"\nCongratulations! Your word is '{the_word}'.")
else:
    print("If you see this, you broke the game")# in case something is wrong