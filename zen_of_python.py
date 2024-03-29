import re
from collections import Counter

# Defines our regular expression for searching ZOP
pattern = "[A-Z]{3}[\s]{1}[A-Z][\w\d\s\\',\-\*]*[.\!]"
word_dict = {}


def zen_of_python(file):
    with open(file) as inputfile:
        content = inputfile.read()
        # Finds ZOP from file using regular expression
        match = re.findall(pattern, content)
        # Prints out ZOP lines without the ZOP marker
        for matches in match:
            clean_lines = matches[4:]
            print(clean_lines)
        # Splits lines of ZOP for our word count 
        for matches in match:
            clean_lines = matches[4:]
            words = clean_lines.split(' ')
            # Counts words in ZOP and eliminates words with
            # different cases to be not considered the same word
            for word in words:
                word = word.lower()
                if word in word_dict:
                    word_dict[word] = word_dict[word] + 1
                else:
                    word_dict[word] = 1
    # Sorts out words by how frequently they are used
    # and returns the 5 most common words
    occurrence_count = Counter(word_dict)
    top_words = occurrence_count.most_common(5)
    print('\nTOP 5 WORDS\n'
          f'{top_words[0][0]}\t:\t{top_words[0][1]}\n'
          f'{top_words[1][0]}\t:\t{top_words[1][1]}\n'
          f'{top_words[2][0]}\t:\t{top_words[2][1]}\n'
          f'{top_words[3][0]}\t:\t{top_words[3][1]}\n'
          f'{top_words[4][0]}\t:\t{top_words[4][1]}\n')


if __name__ == '__main__':
    zen_of_python('input.in')
