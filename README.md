# word-concordance
## Source code for assignment in SENG 265 - Software Development 
##### *published with permission*
Specifically the course considers one kind of concordance known as *keyword-out-of-context or KWOC*. The Oxford English Dictionary defines a concordance is an "alphabetical arrangement of principal words contained in a book, with citations of the passages in which they occur". Someone using a concordance is therefore able to look up a word of interest to them for that book, and fin all the locations (page numbers and line numbers) where the word is used.

This concordance implementation will be for texts much, much smaller than a complete book! Instead the concordance will relate words to the lines in which they occur in some text file being processed

### Asignment 1 - C basic
#### Objectives:
* Use the C programming languague to write the first implementation of a concordance-generation program **without using dynamic memory**.

#### Example:
 Consider the following small text file. Line numbers are given for reference. (Among the test files for this first assignment, this corresponds to the contents of in04.txt.)
 ```
1 the fish a dog cat dog rabbit
2 the fish and cat
3 a rabbit or elephant
 ```

 The concordance for this file is to be generated using the following command (where I assumeall of the needed text files are contained in the same directory as the executable).
 `$ ./kwoc1 -e english.txt in04.txt`
 
 The program produces this output to the console:
 ```
CAT       the fish a dog cat dog rabbit (1) 
CAT       the fish and cat  (2) 
DOG       the fish a dog cat dog rabbit (1*)
ELEPHANT  a rabbit or elephant (3) 
FISH      the fish a dog cat dog rabbit (1) 
FISH      the fish and cat  (2) 
RABBIT    the fish a dog cat dog rabbit (1) 
RABBIT    a rabbit or elephant (3)
 ```

 Each line is made up of a keyword, followed by an input line within which that word appeared, and ends with a number reference. The keywords are printed in alphabetical order. The word **cat** (printed as CAT when shown as a keyword) appears on lines 1 and 2 of the input; the word **dog** appears in only one input line –*line 1*– but does so more than once, hence the asterisk. And so on and so forth.
 Also, some words contained within the input file do not appear as keywords in the concordance. For example, **and**, **or**, and **the** are not really of interest to anyone using a concordance – that is, they are excluded. A file with exclusion words was given to kwoc1on the command line via the **-e** argument.

#### Some simplifying assumptions
In order to reduce the complexity of the program, the following simplifications and size limits have been provided.
1. All input consists of lower-case letters, and all words on a line are separated by a single space. There is no other punctuation such as commas, colons, quotations marks, periods, etc. That is, there are not cases such as that keyword computerappearing as computeror "Computeror computer-aidedor computer?or computer',etc. 
1. All provided exclusion-word files will have one word per line, and lines will be in alphabetical order.
1. Each input file (i.e., those for which a KWOC index is to be created): 
    1. will have at most 100 lines; 
    1. has input lines at most 80 characters long (including spaces and newline character);
    1. has words no longer than 20 characters; 
    1. has no more than 500 unique keywords, although a specific keyword may appear many times in the input file. 
    1. Also: files with exception words will have no more than 100 lines (i.e., no more than 100 words).
1. Your solution must not make use of the dynamic-memory functions malloc, calloc, valloc, realloc, etc. That is, all memory needed can be statically allocated (i.e., program-scope variables) given the size limits described abovein item 3.
1. All code must appear in a single source-code file named kwoc1.c.
 
#### Testing
Shown below is an execution of kwoc1 using pipe operator. Assuming that all of the test files are in the same directory as kwoc1. 
`./kwoc1in04.txt -e english.txt | diff out04.txt -`

10 test cases are provided and assume all test inputs will be well-formed (i.e., our teaching team will not test your submission for its handling of error-formed inputor for malformed command-line arguments).

### Asignment 2 - Python basic
#### Objectives:
* Use the Python 3 programming language to write a less resource-restricted implementation of kwoc (but **without using regular expressions or user-defined classes**).

#### Assumptions:
1. There are no longer maximum values for # of input lines, # of exception words, # of keywords, lengths of words, or lengths of input lines.
1. Input-file words may now be in upper and lower case. However, the words “apple” and “Apple” would both appear with the line for keyword “APPLE”.Exception-file words will still be lower-case (and store alphabetically in the file).
1. The only punctuation in the input-files, besides single spaces between words, will be the hyphen (**“-”**) that may appear between words. For example, “twenty-one” would be one whole word, but words with two or more hyphens such as “twenty--one” or words ending in a hyphen and followed by another word such as would occur with “twenty-or” would not be considered a valid word (i.e., such words with multiple or trailing hyphens will not appear within input files or exception-word files).
1. Global variable are permitted.

#### Running program and Testing
Running the program will also be similar to assignment #1. For example, to run code for test 17, either one of the following command lines is possible:
```
$ ./kwoc2.py -e latin-2.txtin17.txt
$ ./kwoc2.py in17.txt -e latin-2.txt
```

20 test cases are provided. Assume all test inputs will be well-formed (i.e., our teaching team will not test your submission for its handling of error-formed inputor for malformed command-line arguments).


### Assignment 3 - Dynamic Memory
#### Objective:
* Revisit the C programming language, this time using dynamic memory.
* Use valgrindto determine how effective the solution is in its management of dynamic memory.

#### File provided:
The program itself now consists of several files, some of which are C source code, and one of which is for build management.
* kwoc3.c: The majority of the solution will most likely appear in this file. Some demo code (protected with an #ifdef DEBUG conditional-compilation directive) shows how a simple list consisting of words can be constructed, traversed, and destroyed.
* emalloc.[ch]: Code for safe calls to malloc().
* linky.[ch]: Type definitions, prototypes, and codefor the singly-linked list implementation described in lectures.
* makefile: This automates many of the steps required to build the kwoc3 executable, regardless of what files (.cor .h) are modified.

#### Asumptions:
1. Keywords will be **at most 40 characters long**, and you may use a compile-time constantto represent this.
1. The length of any input line will be **at most 100 characters**, and you may usea compile-time constant to represent this.
1. There is no restriction or upper limit on the number of distinct keywords or exceptions words, nor is there any restriction on the numberof lines of input.
1. 

#### Running the program and Testing
```
./kwoc3in14.txt -e english-2.txt| diff out14.txt -
./kwoc3-e latin-2.txtin18.txt | diff out18.txt -
```

20 test cases are provided. Assume all test inputs will be well-formed (i.e., our teaching team will not test your submission for its handling of error-formed inputor for malformed command-line arguments).


### Assignment 4 - Python Classes and Regular Expressions
#### Objective:
A less resource-restricted implementation of *kwoc* using user-defined classes and regular expressions.

#### Assumptions:
1. There are no maximum values for # of input lines, # of exception words, # of keywords, lengths of words, or lengths of input lines.
1. Input-file words may now be in upper and lower case. However, the words “apple” and “Apple” would both appear with the line for keyword “APPLE”. Exception-file words will still be lower-case (and store alphabetically in the file).
1.  Words may contain dashes, and the words may contain upper-and lower-case letters yet still be considered the same word (e.g., “Who”and “who”).
1. Words may now end with **'s** and **'t** (as in “Thor’s hammer” or in “Thor can’t come to the door right now”).The 's and 't are to be considered part of the word.
1. Double-quotes may now appear before and after words, as may parentheses.These are not to be considered part of the word.
1. Other punctuation such as commas (**“,”**), periods (**“.”**), colons (**“:”**), semi-colons (**“;”**), exclamation marks (**“!”**) and question marks (**“?”**) may appear at the end of a word. These are not to be considered part of the word.

#### Tasks:
* Read text input from a file, line by line
* Write output to the terminal
* Extract substrings from lines produced when reading a file•create and use lists in a non-trivial way
* Write a user-defined class•use regular expressions

#### Testing
25 test cases are provided. Assume all test inputs will be well-formed (i.e., our teaching team will not test your submission for its handling of error-formed inputor for malformed command-line arguments).

