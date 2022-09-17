"""
This program runs the "Memory Game". The default of the board
is 4x4, however this can be changed by solely changing the values
of the constants at the beginning.

Name: Eduardo Pareja Lema
"""

import random
import string
import time

NUM_ROWS = 4
NUM_COLUMNS = 4


ordered_nums = [i for i in range(1, NUM_ROWS*NUM_COLUMNS+1)]
nums = [i for i in range(1, NUM_ROWS*NUM_COLUMNS+1)]
letters = list(string.ascii_uppercase)[0:(NUM_ROWS*NUM_COLUMNS//2)]*2
random.shuffle(letters)

        
def random_board():
    """Displays the board of numbers"""
    for i in range(len(nums)):
        print(str(nums[i]).ljust(3), end='')
        if ordered_nums[i]%NUM_COLUMNS == 0:
            print()
            

def play_game():
    """Runs the memory game"""
    random_board()
    count = 0
    num_stops = 0
    correct_guesses = []
    initial_time = time.time()
    while True:

        
        guesses = input("Guess two squares: ")
        guess1 = guesses.split()[0]
        guess2 = guesses.split()[1]

        if (int(guess1)>int(ordered_nums[-1]) or int(guess2)>int(ordered_nums[-1])
            or guess1 in correct_guesses or guess2 in correct_guesses
            or guess1 == guess2):
            print("Invalid number(s). ")
            
        elif letters[int(guess1)-1] == letters[int(guess2)-1]: #If letters are equal
            nums[int(guess1)-1] = letters[int(guess1)-1] 
            nums[int(guess2)-1] = letters[int(guess2)-1] #Update the nums list 
            correct_guesses.append(guess1)
            correct_guesses.append(guess2)
            random_board()
            count += 1
            
        else:
            nums[int(guess1)-1] = letters[int(guess1)-1]
            nums[int(guess2)-1] = letters[int(guess2)-1] 
            
            random_board()
            time.sleep(2)
            #Updates the nums list for 2 seconds
            for _ in range(50):
                print()
            
            nums[int(guess1)-1] = ordered_nums[int(guess1)-1]
            nums[int(guess2)-1] = ordered_nums[int(guess2)-1]#Undo after 2 seconds
            
            random_board()
            count += 1
            num_stops += 1
            
        if nums == letters:
            final_time = time.time()
            game_duration = final_time - initial_time
            for _ in range(50):
                print() 
            print("You win!")
            random_board()
            print("It took you " + str(count) + " guesses and "
                         + str(int(game_duration)) + " seconds.")
            break
    
            
          
if __name__ == '__main__':
    play_game()   
            
            
    

