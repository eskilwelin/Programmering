import random

def random_word(difficulty):
    match difficulty:
        case 1:
            f = open("hangmanwords.txt")
        case _:
            f = open("easywords.txt") 
    word_list = []
    for word in f.readlines():
        word_list.append(word.strip())
    random_word = random.randint(0, len(word_list) -1)
    f.close()
    return(word_list[random_word])

