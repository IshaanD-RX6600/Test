import random
import time

def generate_random_number(min_val, max_val):
    """Generate a random number between min_val and max_val (inclusive)"""
    return random.randint(min_val, max_val)

def guess_the_number():
    """Simple number guessing game"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    
    secret_number = generate_random_number(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                return True
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"Game over! The secret number was {secret_number}.")
    return False

def create_random_list(size, min_val=1, max_val=100):
    """Create a list of random integers"""
    return [random.randint(min_val, max_val) for _ in range(size)]

def calculate_average(numbers):
    """Calculate the average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    print("Random Code Examples")
    print("-" * 20)
    
    # Example 1: Generate and print random numbers
    print("Generating 5 random numbers between 1 and 100:")
    for i in range(5):
        print(f"Random number {i+1}: {generate_random_number(1, 100)}")
    
    # Example 2: Create and process a random list
    random_list = create_random_list(10, 1, 50)
    print(f"\nRandom list: {random_list}")
    print(f"Sorted list: {sorted(random_list)}")
    print(f"List average: {calculate_average(random_list):.2f}")
    
    # Example 3: Simple countdown timer
    print("\nStarting a 3-second countdown:")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("Done!")
    
    # Example 4: Optional number guessing game
    play_game = input("\nWould you like to play a number guessing game? (y/n): ")
    if play_game.lower() == 'y':
        guess_the_number()

if __name__ == "__main__":
    main()