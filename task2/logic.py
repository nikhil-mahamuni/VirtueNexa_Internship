from words import get_random_word;

def displayWordStatus(word, guessed_letters):
  letters = [letter if letter in guessed_letters else "_" for letter in word]
  return " ".join(letters)

def game_progress(word, guess_letters, guess):
  if guess in guess_letters: 
    return False, "You already guess that Letter"
  guess_letters.add(guess)
  if guess in word:
    return True, "Correct Choice!"
  else:
    return False, "Incorrect guess!"
  
def is_word_guessed(word, guessed_letters):
  result = all(letter in guessed_letters for letter in word)
  return result