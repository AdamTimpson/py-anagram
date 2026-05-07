import random

def load_word_file(word_file_path: str) -> list[str]:
    """
    Load the list of words from the given file and return

    :param str word_file_path: The path to the list of words to load
    :return: The list of words 
    :rtype: list[str]
    """
    result: list[str] = []
    with open(word_file_path) as file: 
        for line in file: 
            result.append(line.strip().upper())

    return result

def fetch_answer(word_list: list[str]) -> str:
    """
    Choose from the `word_list` a random word as the answer
    
    :param str word_list: The list of words to choose from
    :return: the chosen random answer
    :rtype: list[str]
    """
    answer = word_list[random.randint(0, len(word_list) - 1)]
    return answer



