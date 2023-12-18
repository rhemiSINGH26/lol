import random

def generate_number():
    return random.randint(1, 100)

def check_guess(secret_number, guess):
    if guess < secret_number:
        return "Too low!"
    elif guess > secret_number:
        return "Too high!"
    else:
        return "Congratulations! You guessed it!"

def main():
    secret_number = generate_number()
    attempts = 0
    max_attempts = 7
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while attempts < max_attempts:
        print(f"You have {max_attempts - attempts} attempts left.")
        try:
            guess = int(input("Enter your guess: "))
            result = check_guess(secret_number, guess)
            print(result)
            attempts += 1

            if result == "Congratulations! You guessed it!":
                break
        except ValueError:
            print("Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    main()


