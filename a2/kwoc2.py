#!usr/bin/env python3
import sys

def main():
    occurrences_dict = {}
    exclusion_words = []
    if (len(sys.argv) != 4) and (len(sys.argv) != 2):
        print("Error. Invalid number of arguements.")
        sys.exit(1)
    elif len(sys.argv) == 2:
        input_txt = sys.argv[1]
    else:
        for i in range(len(sys.argv)-1):
            if sys.argv[i] == "-e":
                exclusion_file = sys.argv[i + 1]
                exclusion_words = get_exclusion_words(exclusion_file)
                if i == 1:
                    input_txt = sys.argv[3]
                else:
                    input_txt = sys.argv[1]

    unique_words, lines = get_unique_words(input_txt, exclusion_words)
    get_occurrence(lines, unique_words, occurrences_dict)
    max_len = get_longest_word(unique_words)
    print_output(max_len, unique_words, occurrences_dict)

def get_exclusion_words(file_name):
    exclusion_words = []
    exclusion_input = open(file_name, "r")
    for line in exclusion_input:
        exclusion_words.append(line.rstrip("\n"))
    return exclusion_words

def is_valid_keyword (keyword, exclusion_words):
    if (keyword[-1] == "-"):
        return False
    for word in exclusion_words:
        if word == keyword.lower():
            return False
    return True

def get_unique_words(file_name, exclusion_words):
    unique_words = []
    lines = []
    input_txt = open(file_name, "r")
    for line in input_txt:
        line = line.rstrip("\n")
        lines.append(line)
        if len(line) > 0:
            words = line.split(" ")
            for word in words:
                if (is_valid_keyword(word, exclusion_words)):
                    unique_words.append(word.upper())
        if (len(unique_words) != 0):
            unique_words = list(set(unique_words))
            unique_words.sort()
    return unique_words, lines

def count_num_occurence(line, keyword):
    count = 0
    words = line.split(" ")
    for word in words:
        if word.upper() == keyword:
            count += 1
    return count

def get_occurrence (lines, unique_words, occurrences_dict):
    for keyword in unique_words:
        for i in range(len(lines)):
            count = count_num_occurence(lines[i], keyword)
            if (count > 0):
                if keyword in occurrences_dict:
                    occurrences_dict[keyword].append((lines[i], i, count))
                else:
                    occurrences_dict[keyword] = [(lines[i], i, count)]

def get_longest_word (unique_words):
    max_len = 0
    for keyword in unique_words:
        if len(keyword) > max_len:
            max_len = len(keyword)
    return max_len

def print_output(max_len, unique_words, occurrences_dict):
    for keyword in unique_words:
        keyword_format = keyword + " "*(max_len - len(keyword))
        for line in occurrences_dict[keyword]:
            print(keyword_format, " {}".format(line[0]), end = " ")
            if line[2] > 1:
                print("(%d*)" % (line[1] + 1))
            else:
                print("(%d)" % (line[1] + 1))

if __name__ == "__main__":
    main()
