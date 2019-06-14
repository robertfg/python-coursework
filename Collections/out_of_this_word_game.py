# Imports
import random

# List of words to guess
WORDS = (
    "treehouse",
    "python",
    "learner"
)


# Prompt for a word
def prompt_for_words(challenge):
    guesses = set()
    print("What words can you find in the word '{}'".format(challenge))
    print("(Enter Q to Quit)")

    while(True):
        guess = input("{} words >  ".format(len(guesses)))
        if guess.upper() == 'Q':
            break
        guesses.add(guess.lower())

    return guesses


# Loop for results
def output_results(results):
    for word in results:
        print("*", word)


# Start game
challenge_word = random.choice(WORDS)

player1_words = prompt_for_words(challenge_word)
player2_words = prompt_for_words(challenge_word)

# Calculations
player1_unique = player1_words - player2_words
player2_unique = player2_words - player1_words
shared_words   = player1_words & player2_words

print("Player 1 Results:")
print("{} guesses, {} unique".format(len(player1_words), len(player1_unique)))
output_results(player1_unique)
print("-"*10)

print("Player 2 Results:")
print("{} guesses, {} unique".format(len(player2_words), len(player2_unique)))
output_results(player2_unique)
print("-"*10)

print("Shared Guesses:")
output_results(shared_words)
