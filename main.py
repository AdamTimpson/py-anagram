import word_manager
import random

WORD_FILE = "./words.txt"

def get_random_index(word, indexes_used):

    random_index = random.randint(0, len(word) - 1)
    if random_index in indexes_used:
        return get_random_index(word, indexes_used)

    indexes_used.append(random_index)
    return random_index


def scramble(word):
    result = ""

    used_indexes = []
    for char in word:
        random_index = get_random_index(word, used_indexes)
        result += word[random_index]


    print(used_indexes)
    return result
        

if __name__ == "__main__":
    words = word_manager.load_word_file(WORD_FILE)

    for word in words:
        print(f"{word} --- {scramble(word)}\n")
