from hangman_arts import stages, logo
from hangman_words import rand_word
import random
from turtle import clear

print
rand_choice = random.choice(rand_word)

num_of_lives = 6
print(f'Psst, the solution is {rand_choice}')
display = []
for letter in rand_choice: 
    display += '_'
print(display, end='')
print()

i = 0
word_len = len(rand_choice)
while display != rand_choice:
    user_choice = input().lower()
    clear()
    if user_choice  == display[i]:
      print("You have entered " + user_choice + " before")
    for i in range(word_len):     
     letter = rand_choice [i]
     if user_choice == letter:
            display[i] = letter
    print(f"{' '.join(display)}")
           
    if user_choice not in rand_choice:
        num_of_lives -= 1
        print(stages[num_of_lives]) 
        if num_of_lives == 0:
            display = rand_choice
            print("Fuck you comrade You lose ")
            
            break
            


    if '_' not in display:
            display = rand_choice
            print("You win")
  
    