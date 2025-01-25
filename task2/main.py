from display import show_welcome_message, show_hint, show_attempts_left, show_game_over, show_congratulations
from logic import displayWordStatus, game_progress, is_word_guessed, get_random_word
from words import get_random_word

def hangman(): 
  word, hint = get_random_word()
  guessed_letters = set()
  TOTAL_ATTEMPTS = 5

  show_welcome_message()
  show_hint(hint)

  while (TOTAL_ATTEMPTS > 0):
    print("Currennt Word: ", displayWordStatus(word, guessed_letters))
    show_attempts_left(TOTAL_ATTEMPTS)

    guess = input('\nEnter a letter: ').lower()

    if(len(guess) != 1 or not guess.isalpha()):
      print("Invalid input! Please enter a single letter.")
      continue

    correct, message = game_progress(word, guessed_letters, guess)
    print(message)

    if not correct:
      TOTAL_ATTEMPTS -= 1

    if is_word_guessed(word, guessed_letters):
      show_congratulations(word)
      break

  else:
    show_game_over(word)

if __name__ == "__main__":
  hangman()