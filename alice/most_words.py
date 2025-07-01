import sys

def get_vars():
    """
    Reads the number N from the command-line arguments and the input text from 'alice.txt'.
    
    Returns:
        tuple: (N (int), input_text (str)) where:
            - N is the number of top words to print
            - input_text is the full content of the file 'alice.txt'

    Exits the program with an error message if:
        - No valid integer is provided as a command-line argument
        - The file cannot be read
    """
    try:
        N = int(sys.argv[1])
    except Exception as e:
        print(e, "\nPlease provide a valid integer")
        sys.exit(1)
    
    file_path = 'alice.txt'
    
    try:
        with open(file_path, 'r') as f:
            input_text = f.read()
    except Exception as e:
        print(e, "\n please provide a valide text file")
        sys.exit(1)
    return N, input_text

def mk_words_dict(input_text):
    """
    Processes the input text into a dictionary of word frequencies.

    Steps:
        - Identifies unwanted (non-alphabetic) characters
        - Converts each letter in the word to it's lowercase
        - Strips those characters from words
        - Counts occurrences of each cleaned word
        - Sorts the dictionary by frequency in descending order
        - Filters out any keys that are not pure alphabetic words

    Args:
        input_text (str): The text to analyze

    Returns:
        dict: A dictionary {word: count} sorted by descending count
    """
    unwanted_chars = ''.join(set([char for char in input_text if not char.isalpha()]))
    
    # Count how many times each cleaned word appears in the text
    words_dict = {word.lower().strip(unwanted_chars): input_text.count(word.lower().strip(unwanted_chars)) for word in input_text.split()}
    
    # Sort by frequency (value) in descending order
    sorted_dict = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))
    
    # Keep only keys that are alphabetic (remove numbers, empty strings, etc.)
    final_dict = {word: count for word, count in sorted_dict.items() if word.isalpha()}
    return final_dict

def printer(N, words_dict):
    """
    Prints the top-N most frequent words in the given dictionary.

    Args:
        N (int): Number of top words to print
        words_dict (dict): Dictionary of word frequencies
    """
    sorted_list = list(words_dict.items())[:N]
    i = 1
    for word, count in sorted_list:
        print(f'{i} - word "{word}" {count} times')
        i += 1

def main():
    """
    Main execution flow:
        - Get N and the input text
        - Build the word frequency dictionary
        - Print the top-N words
    """
    N, input_text = get_vars()
    words_dict = mk_words_dict(input_text)
    printer(N, words_dict)

if __name__ == '__main__':
    main()
