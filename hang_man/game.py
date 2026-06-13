import word_list

word_to_guess = word_list.random_word()
print(word_to_guess)

brackets = ["_"] * len(word_to_guess)

print(brackets)
user_lives = 6
print(user_lives)

print(" ".join(brackets))

word_to_guess_letters = list(word_to_guess)
print(word_to_guess_letters)

while "_" in brackets and user_lives > 0: 

    print("Type a single letter!")
    user_guess = input("> ")
    if not user_guess.isalpha() or not len(user_guess) == 1:
        print("I said a single letter!")

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
            brackets[count] = user_guess
        count += 1

    print(" ".join(brackets))
