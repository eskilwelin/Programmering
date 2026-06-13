"""
TODO:
- Grafik

"""
import word_list


def main():
    print("Want a hard word or an easy word? \n 1. Hard \n 2. Easy \n")
    while True:
        try:
            difficulty = int(input("> "))
        except ValueError:
            print("1 or 2 bozo!")
            continue
        if difficulty > 2:
            print("1 or 2 bozo!")
            continue
        else:
            break
            
    word_to_guess = word_list.random_word(difficulty)

    user_word = ["_"] * len(word_to_guess)

    user_lives = 8
    already_guessed_letters = []

    print(" ".join(user_word))

    word_to_guess_letters = list(word_to_guess)

    run_game = True
    while run_game: 

        print("Type a single letter!")
        user_input_letter = input("> ")

        if not user_input_letter.isalpha() or not len(user_input_letter) == 1:
            print("I said a single letter!")
        elif user_input_letter in already_guessed_letters:
            print(f"You already tried {user_input_letter}")
        else:
            for counter, i in enumerate(word_to_guess_letters):
                if not user_input_letter in word_to_guess_letters:
                    user_lives -= 1
                    if user_lives > 1:
                        print(f"Guess again! You have {user_lives} tries left!")
                        break
                    elif user_lives == 1:
                        print(f"Guess again! You have {user_lives} try left!")
                        break            
                    else:
                        print(f"You got hung! The word was {word_to_guess}!")
                        run_game = False
                        break    
                # detta kan förmodligen vara else (?)
                if i == user_input_letter: 
                    user_word[counter] = user_input_letter
                    already_guessed_letters.append(user_input_letter)


        if not "_" in user_word:
            print(f'You successfully guessed the word: "{word_to_guess}". You WIN!')
            break

        print(" ".join(user_word))


if __name__ == "__main__":
    main()
