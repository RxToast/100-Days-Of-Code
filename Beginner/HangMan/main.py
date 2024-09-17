import random
import hangman_words
from hangman_art import stages
from hangman_art import logo

word_list = hangman_words.word_list
lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"**************************** {lives} LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess and letter in correct_letters:
            print(f"\nYou've already guessed the letter: {guess}\n")
            display += letter
        elif letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"**************************** YOU LOSE ****************************\n"
                  f"The correct word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    print(stages[lives])
