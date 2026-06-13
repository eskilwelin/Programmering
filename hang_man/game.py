import word_list

word_to_guess = word_list.random_word()
print(word_to_guess)

user_word = ["_"] * len(word_to_guess)

user_lives = 6
already_guessed = []

print(" ".join(user_word))

word_to_guess_letters = list(word_to_guess)
print(word_to_guess_letters)

while "_" in user_word and user_lives > 0: 

    print("Type a single letter!")
    user_guess = input("> ")

    if not user_guess.isalpha() or not len(user_guess) == 1:
        print("I said a single letter!")
    elif user_guess in already_guessed:
        print(f"You already guessed {user_guess}")
    else:
        count = 0
        for i in word_to_guess_letters:
            if not user_guess in word_to_guess_letters:
                user_lives -= 1
                if user_lives > 1:
                    print(f"Guess again! You have {user_lives} tries left!")
                    break
                if user_lives > 0:
                    print(f"Guess again! You have {user_lives} try left!")
                    break
                print("You got hung!")
                break
            if i == user_guess:
                user_word[count] = user_guess
            count += 1
            
        already_guessed.append(user_guess)

    print(" ".join(user_word))
