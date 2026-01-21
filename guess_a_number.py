import random

number = random.randint(1,100)
print("Guess the number:")
print("You should guess what number the computer has chosen. The number is between 1 and 100.")
print("Mind that you have only 10 tries. After them the game will stop automatically!!! ")
guesses = 0
while True:
    try:
        guess = int(input())
        guesses += 1
        if guesses == 10:
            print("You have reached your maximum guesses. Good luck next time!!!")
            break
        if guess < 1 or guess > 100:
            print("Your guess is not in the wanted range. Try again!")
            continue
        if guess < number:
            print(f"You guessed wrong. The number should be higher than {guess}")
        elif guess > number:
            print(f"You guessed wrong. The number should be lower than {guess}")
        elif guess == number:
            print("You have guessed the number. Congratulations!")
            break
    except ValueError:
            print("Your input is invalid. You should only type numbers!")

