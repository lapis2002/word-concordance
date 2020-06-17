import sys
import re

PATTERN = r'''^((\w|\-)+$'''

class KWOC:

    def __init__(self, filename, exceptions):
        self.text = (self.get_content(filename))
        self.exclusion_words = self.get_exclusion_words(exceptions)
        
    def get_content(self, filename):
        input_txt = open(filename, "r")
        content = []
        for line in input_txt:
            line = line.rstrip("\n")
            content.append(line)
        # print(content)
        input_txt.close()
        return content
        
# assume exceptions exists
    def get_exclusion_words (self, exceptions):
        exclusion_pat = ""
        if (exceptions):
            exclusion_input = open(exceptions, "r")
            content = []
            for line in exclusion_input:
                line = line.rstrip("\n")
                content.append(line)            
                # print(exclusion_words)
            # print()
            exclusion_input.close()
            exclusion_words = ""
            for i in range(len(content)):
                exclusion_words += r"\b" + content[i]
                if i != len(content)-1:
                    exclusion_words += r"\b|"

            # print("exclude", exclusion_words)
            exclusion_pat = r"\b(?!" + \
                exclusion_words + r"\b)\w*['-]?\w+\b"
            # print()
            # print(exclusion_pat)
            return exclusion_pat

# pattern not enough
    def get_words(self):
        pat = self.exclusion_words
        if not pat:
            pat = r"\b\w*'?\w+\b"
        # pat = r"\b(?!the\b|a\b|or\b)w*'?\w+\b"
        # print("pattern", pat)
        # print("text", self.text)
        # text = "\n".join(self.text)
        # print("text", self.text)
        # print("pattern", pat)
        words = re.findall(pat, "\n".join(self.text), re.IGNORECASE)
        # print(words)
        return words

# fix this to handle more than 1 word in 1 line
    def find_word(self, word):
        # print(word)

        pat = r"\b" + word + r"(?![-|'])\b"
        # print(self.text)
        res = []
        for i in range(len(self.text)):
            match = re.findall(pat, self.text[i], re.IGNORECASE)
            if match:
                # print(match)
                # print()
                res.append((self.text[i], i, len(match)))
        return res

    def words_preprocessing(self):
        # self.text = self.text.split("\n")
        words = self.get_words()
        words = list(set([word.lower() for word in words]))
        words.sort()
        # print(words)

        return words, len(max(words, key=lambda x: len(x)))

# text preprocessing
# no longer print the keyword
    def print_word(self, word, longest_word_len):
        match = self.find_word(word)
        keyword_format = word.upper() + " "*(longest_word_len - len(word)+2)

        res = []

# not handle more than two words appear in 1 line yet i.e (1*)        
        for i in range(len(match)):
            if match[i][2] > 1:
                res.append( keyword_format + match[i][0] + " (" + str(match[i][1]+1) + "*)")
            else:
                res.append(keyword_format +
                           match[i][0] + " (" + str(match[i][1]+1) + ")")
        # print("match", match)
        # print()
        return res

    def print_list(self):
        word_list, max_len = len(self.words_preprocessing())
        res = []
        for word in word_list:
            res.append(self.print_word(word, max_len))

    def concordance(self):
        word_list, max_len = self.words_preprocessing()
        res = []
        for word in word_list:
            for s in self.print_word(word, max_len):
                res.append(s)

        return res
