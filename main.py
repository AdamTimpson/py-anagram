import word_manager
import random

WORD_FILE = "./words.txt"

def scramble(word): 
    chars = list(word)
    random.shuffle(chars)
    result = "".join(chars)

    return result if result != word else scramble(word)

if __name__ == "__main__":
    words = word_manager.load_word_file(WORD_FILE)

    answer = words[random.randint(0, len(words) - 1)]
    print(f"{answer} --- {scramble(answer)}\n")

    guess = input("Guess: ")
    if guess == answer:
        print("WINNER")
    else:
        print("Try again!")
