import random

def guessing_game():
    # Generate a random number between 1 and 50
    number_to_guess = random.randint(1, 50)
    
    print("Welcome to the guessing game!")
    print("Guess a number between 1 and 50.")
    
    while True:
        try:
            # Ask the user for their guess
            guess = int(input("Enter your guess: "))
            
            # Check if the guess is too high, too low, or correct
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the correct number.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guessing_game()
