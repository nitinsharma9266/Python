import random

print("🎮 Welcome to the Number Guessing Game!")
print("👉 Guess a number between 1 and 100\n")

n = random.randint(1, 100)
a = -1
guesses = 1

while a != n:
    try:
        a = int(input("Guess the number: "))

        if a > n:
            print("Lower number please!\n")
            guesses += 1

        elif a < n:
            print("Higher number please!\n")
            guesses += 1

    except ValueError:
        print("❌ Please enter a valid number!\n")

print(f"🎉 Congratulations!")
print(f"You guessed the number {n} correctly in {guesses} attempts.")
