"""
TODO:
- Ta bort debugg statements
- Grafik

"""

import word_list

word_to_guess = word_list.random_word()
print(word_to_guess)

user_word = ["_"] * len(word_to_guess)

user_lives = 6
already_guessed = []

print(" ".join(user_word))

word_to_guess_letters = list(word_to_guess)
print(word_to_guess_letters)


while True: 

    print("Type a single letter!")
    user_guess = input("> ")

    if not user_guess.isalpha() or not len(user_guess) == 1:
        print("I said a single letter!")
    elif user_guess in already_guessed:
        print(f"You already tried {user_guess}")
    else:
        for counter, i in enumerate(word_to_guess_letters):
            if not user_guess in word_to_guess_letters:
                user_lives -= 1
                if user_lives > 1:
                    print(f"Guess again! You have {user_lives} tries left!")
                    break
                if user_lives > 0:
                    print(f"Guess again! You have {user_lives} try left!")
                    break                
            if i == user_guess:
                user_word[counter] = user_guess

        already_guessed.append(user_guess)

    if not "_" in user_word:
        solution = "".join(user_word)
        print(f'You successfully guessed the word: "{solution}". You WIN!')
        break

    if user_lives == 0:
        print("You got hung!")
        break

    print(" ".join(user_word))


