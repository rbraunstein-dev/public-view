#!/usr/bin/env python3

import fileinput
import re

#Total number of phrases output, can be modified to change the number outputted
MOST_COMMON = 100
#number of words
#can modify this number to change the length of the phrases
WORD_SEQ_Index_Value = 3

#dictionary count
dict_count = {}
#regex pattern search
regex = r"(?!('|’).*('|’))\b[\w('|’)]+\b"
#regex = r"\b[\w('|’)]+\b"


def print_result(dict_count: dict[str, int]) -> None:
    sorted_dict = {
        #k = phrase, v = count 
        k: v
        for k, v in sorted(dict_count.items(), key=lambda item: item[1], reverse=True)
    }
    #prints the first 100 (MOST_COMMON) items in the sorted_dict list
    for k, v in list(sorted_dict.items())[:MOST_COMMON]:
        print(f"{k} - {v}")
    pass


def process(line: str, last_words: list[str]) -> list[str]:
    matches = re.finditer(regex, line)

    for index, match in enumerate(matches):
        word = match.group()
        #Checks if length of last_words list is equal to 2, sends list through to loop if True
        if len(last_words) == WORD_SEQ_Index_Value - 1:
            #joins each word fed into the loop together separated by a space as the three_words variable
            three_words = " ".join([*last_words, word])
            #if the combination of words isn't in the dictionary already, add it and set its value to 1
            if three_words not in dict_count:
                dict_count[three_words] = 1
            else:
                #if the combination of words is in the dictionary already, increase the count by 1
                dict_count[three_words] = dict_count[three_words] + 1
            #removes the first item from the last_words list
            last_words.pop(0)
        #continues appending each match to last_words list until it contains enough words to make it through the above 'if' statement
        last_words.append(word)
    return last_words


if __name__ == "__main__":
    #initializes current file as empty
    current_file = None
    #initializes list of words
    last_words = []
    #for loop to process file line by line
    for line in fileinput.input():
        now_processing = fileinput.filename()
        if now_processing != current_file:
            current_file = now_processing
            print_result(dict_count)
            print(f"Now processing file {now_processing}")
            dict_count = {}
            last_words = []
        #Passes in current line of current file (lower-cased) as a parameter as well as current last_word list
        last_words = process(line.lower(), last_words)
    print_result(dict_count)
