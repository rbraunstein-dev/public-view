#!/usr/bin/env python3

import fileinput
import re
# import os
import operator
#from os.path import expanduser

# home = expanduser("~")
# filepath = f"{home}/Documents/gitprojects/codez/IT Tools/mac-unix/python_scripts/moby-dick.txt"

word_per_list = 3
#Searches word characters and both versions of apostrophes 1 to unlimited times as long as they're within the boundaries of a word
regex = re.compile(r"\b[\w('|’)]+\b")

# Read input line by line with proper regex
# (add file input later)
def input_reader():
    phrases_dictionary = {}
    three_words = []
    # file = open(filepath, 'r')

    textlines = fileinput.input()
    for line in textlines:
        words_in_line = regex.findall(line)
    # Create 3 word phrases from every 3 words
        for word in words_in_line:
            single_word = word.lower()
            if len(three_words) == word_per_list:
                word_join = " ".join(three_words)
                # Add phrases to a dictionary: phrases as keys, counts as values 
                # (Check the dictionary to see if they exist already if so update the value with a +1 count)
                if word_join not in phrases_dictionary:
                    phrases_dictionary[word_join] = 1
                    #print("Creating " + str(phrases_dictionary[word_join]))
                else:
                    phrases_dictionary[word_join] = phrases_dictionary[word_join] + 1
                    #print("Updating " + str(phrases_dictionary[word_join]))
                three_words.pop(0)
            three_words.append(single_word)
    return phrases_dictionary


# After the whole dictionary has been built, sort through and order them highest value to lowest.+
def dictionary_sorter(dictionary_input):

    sorted_dictionary = {
        phrase: number_of_occurrences
        for phrase, number_of_occurrences in sorted(dictionary_input.items(), key=operator.itemgetter(1), reverse=True)
    }
    # Print the first 100 entries [:99]
    for phrase, number_of_occurrences in list(sorted_dictionary.items())[:99]:
        print(str(phrase) + " - " + str(number_of_occurrences))

    return(sorted_dictionary)




if __name__ == '__main__':
    initial_dictionary = input_reader()
    dictionary_sorter(initial_dictionary)