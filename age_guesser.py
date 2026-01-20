import random

print("Hi! I'm going to try to guess your age.")

name = input("What's your name? ")

max_guesses = 3
guesses = 0

while guesses < max_guesses:
    age_guess = random.randint(0, 120)
    guesses += 1

    answer = input(f"Is your age {age_guess}? (y/n): ").strip().lower()

    if answer == "y":
        print(f"{name} is {age_guess} years old.")
        break
    else:
        print("Rats.")
else:
    print("I couldn't guess your age in 3 tries.")

