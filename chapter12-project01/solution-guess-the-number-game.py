
import random

def guess_the_number(difficulty):
    # Set the number of guesses based on difficulty
    if difficulty == "easy":
        max_guesses = 10
    elif difficulty == "medium":
        max_guesses = 8
    elif difficulty == "hard":
        max_guesses = 5
    else:
        print("Invalid difficulty level. Please choose from easy, medium, or hard.")
        return
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print(f"Welcome to the Guess the Number Game (Difficulty: {difficulty.capitalize()})")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_guesses} guesses.")

    # Loop for the player's guesses
    for guess_count in range(max_guesses):
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number ({secret_number}) in {guess_count + 1} guesses!")
            return
    
    print(f"Sorry, you've run out of guesses. The number was {secret_number}.")

# Main program
if __name__ == "__main__":
    difficulty_level = input("Choose difficulty level (easy, medium, hard): ").lower()
    guess_the_number(difficulty_level)




