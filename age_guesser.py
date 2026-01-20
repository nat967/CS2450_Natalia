import random

print("Hi! I'm going to try to guess your age.")

name = input("What's your name? ")

while True:
    age_guess = random.randint(0, 100)
    answer = input(f"Is your age {age_guess}? (y/n): ").strip().lower()

    if answer == "y":
        print(f"{name} is {age_guess} years old.")
        break
    else:
        print("Rats.")

