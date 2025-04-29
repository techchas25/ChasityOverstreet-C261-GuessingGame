#chasity Overstreet, C261 guessing game 2.1lab

import random
def display_heading():
    print("You have arrived to the number guessing game")
  
def play_game(limit):
    number_to_guess = random.randint(1, limit)
    print(f"Guess a number between 1 and {limit}")
    
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
       try:
         guess = int(input("Enter your guess, you will have 3 attempts: "))
         attempts += 1
         if guess > number_to_guess:
            print("Too high!")
         elif guess < number_to_guess:
            print("Too low!")
         else:
            print("Correct!")
            return
       except ValueError:
            print("Invalid Input. Please enter a number.")
    print(f"Out of guesses! The correct number was {number_to_guess}.\n")
        
while True:
    display_heading()
    limit = 50
    play_game(limit)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break