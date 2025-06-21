import random

def play_game():
    n = random.randint(1, 100)
    guesses = 0
    a = -1

    print("🎯 Welcome to The Perfect Guess!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while a != n:
        try:
            a = int(input("Enter your guess: "))
        except ValueError:
            print("❗ Please enter a valid number.")
            continue

        guesses += 1

        if a > n:
            print("🔻 Lower number please.")
        elif a < n:
            print("🔺 Higher number please.")

    print(f"✅ You guessed the number {n} correctly in {guesses} attempts!")

def main():
    while True:
        play_game()
        again = input("🔁 Do you want to play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("👋 Thanks for playing The Perfect Guess! Goodbye!")
            break

main()