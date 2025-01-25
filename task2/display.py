def show_welcome_message():
    print("\n===== Welcome to Hangman! =====")
    print("Guess the letters to complete the word.")
    print("🤩🤩 You have limited attempts. Good luck! 🤩🤩\n")

def show_hint(hint):
    print(f"HINT: {hint}")
 
def show_attempts_left(attempts_left):
    print(f"\nRemaining Attempts: {attempts_left}")

def show_game_over(word):
    print("\nGame Over! The correct word was:", word)
    print("😕😕 Better luck next time! 😕😕\n")

def show_congratulations(word):
    print("\n🥳🥳 Congratulations! You guessed the word " + word + " correctly! 🥳🥳\n")