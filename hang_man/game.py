"""
TODO:
- Grafik

"""

import word_list

def main():
    print("Are you ready for some kinky shit? \n Type: 1 for BDSM \n Type: 2 for vanilla stuff \n")
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
    
    # generate a word from word_list.py
    word_to_guess = word_list.random_word(difficulty)
   
    # make the brackets to display the length of the word and any found letters
    user_word = ["_"] * len(word_to_guess)


    user_lives = 6
    already_guessed_letters = []


    word_to_guess_letters = list(word_to_guess)

    run_game = True
    while run_game: 

        print(" ".join(user_word) + "\n")
        user_input_letter = (input("Type a single letter: ")).lower()

        # Validate user input as a single letter
        if not user_input_letter.isalpha() or not len(user_input_letter) == 1:
            print("I said a single letter!")

        elif user_input_letter in already_guessed_letters:
            print(f"You already tried {user_input_letter}\n")

        elif not user_input_letter in word_to_guess_letters:
            already_guessed_letters.append(user_input_letter)
            user_lives -= 1
            if user_lives > 1:
                print(f"Guess again! Smack! You have now only {user_lives} tries left!\n")
                continue
            elif user_lives == 1:
                print(f"Guess again! You have {user_lives} try left!\n")
                continue            
            else:
                print(f"You're liked it, didn't you? The word was {word_to_guess}!\n")
                break   
            
        else:
            already_guessed_letters.append(user_input_letter)
            for counter, i in enumerate(word_to_guess_letters):
                if i == user_input_letter: 
                    user_word[counter] = user_input_letter

        if not "_" in user_word:
            print(f'You successfully guessed the word: "{word_to_guess}". You WIN!')
            break

if __name__ == "__main__":
    main()
