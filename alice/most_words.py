import sys


def get_vars():
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
    unwanted_chars = ''.join(set([char for char in input_text if not char.isalpha()]))
    words_dict = {word.strip(unwanted_chars): input_text.count(word.strip(unwanted_chars)) for word in input_text.split()}
    sorted_dict = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))
    final_dict = {word: count for word, count in sorted_dict.items() if word.isalpha()}
    return final_dict


def printer(N, words_dict):
    sorted_list = list(words_dict.items())[:N]
    i = 1
    for word, count in sorted_list:
        print(f'{i} - word "{word}" {count} times')
        i += 1


def main():
    N, input_text = get_vars()
    words_dict = mk_words_dict(input_text)
    printer(N, words_dict)


if __name__ == '__main__':
    main()