import random

def random_word():

    f = open("hangmanwords.txt") 
    word_list = []
    for word in f.readlines():
        word_list.append(word.strip())
    random_word = random.randint(0, len(word_list) -1)
    f.close()
    return(word_list[random_word])

