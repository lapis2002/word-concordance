#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//I have modified some functions from code provided in lectures.

#define MAX_NUM_KEYWORDS 500
#define MAX_WORD_LEN 25
#define MAX_LINE_LEN 80
#define MAX_NUM_LINES 100
#define MAX_EXCLUSION_WORDS 100
#define TRUE 1
#define FALSE 0

char lines[MAX_LINE_LEN][MAX_NUM_LINES];
// int num_lines;
char words[MAX_NUM_KEYWORDS][MAX_WORD_LEN];

//int num_occur[MAX_NUM_KEYWORDS];

//int  num_exclusion_words = 0;
char exclusion_words[MAX_EXCLUSION_WORDS][MAX_WORD_LEN];

/*
Purpose: swap 2 words.
Arg: (char *) word 1, (char *) word 2.
Retrun void
*/

void str_swap(char * str1, char * str2) {
  char temp[MAX_WORD_LEN];
    strncpy(temp, str1, MAX_WORD_LEN);
    strncpy(str1, str2, MAX_WORD_LEN);
    strncpy(str2, temp, MAX_WORD_LEN);
}

/*
Purpose: compare 2 words.
Arg    : (char *) word 1, (char *) word 2.
Return : void
*/

int compare_less (char * w1, char * w2) {
  int i;
  int min_len;
  if (strlen(w1) <= strlen(w2)) {
    min_len = strlen(w1);
  } else {
    min_len = strlen(w2);
  }
  for (i = 0; i < min_len; i ++ ) {
    if (w1[i] > w2[i]) {
      return TRUE;
    } else if (w1[i] < w2[i]) {
      return FALSE;
    }
  }
  if (strlen(w1) < strlen(w2)) {
    return FALSE;
  } else {
    return TRUE;
  }
}

/*
Purpose: sort the array in alphabetical order.
Arg    : none
Return : void
 */
void sort(int * num_words_pt) {
  int count = * num_words_pt;
  int i;
  int j;
  for (i = 0; i < count; i ++) {
    for (j = 0; j < count; j ++) {
      if (!compare_less(words[i], words[j])) {
        //swap
          str_swap(words[i], words[j]);
      }
    }
  }
}

/*
Purpose: check if word is in the exclusion word.
Arg    : (char*) word, (char*) exclusion word array
Return : TRUE or FALSE
*/

int is_exclusion_word (char * word, int * num_exclusion_words_pt) {
  int i;
  for (i = 0; i < *num_exclusion_words_pt; i ++) {
    if (strcmp(word, exclusion_words[i]) == 0) {
      return TRUE;
    }
  }
  return FALSE;
}

/*
Purpose: store unique words which is not in the exclusion word array. The array of unique words is in  in alphabetical order
Arg    : (char *) line of text, (char *) array of unique words, (char *) array of exlusion words.
Return : void
*/

void store_the_words(char *line, int * num_occur_pt, int * num_words_pt, int *num_exclusion_words_pt) {;
    char buffer[MAX_LINE_LEN];
    char *t;
    int i;
    strncpy(buffer, line, MAX_LINE_LEN);
    t = strtok(buffer, " ");
    while (t != NULL) {
      for (i = 0; i <= *num_words_pt; i++) {
        // check if t is in the array or not
        if (strcmp(t, words[i]) == 0) {
            break;
        }
        else if (i == *num_words_pt) {
          // check if t is in the axclusion word array or not
            if (is_exclusion_word(t, num_exclusion_words_pt) == FALSE) {
              strncpy(words[*num_words_pt], t, MAX_WORD_LEN);
              *(num_occur_pt + *num_words_pt) = 0;
              *num_words_pt = *num_words_pt + 1;
              break;
            }
        }
      }
      t = strtok(NULL, " ");
    }
}


/*
Purpose : count the number of appearance of the word in line.
Arg     : (char *) word, (char *) line.
Return  : (int) num of occurences.
*/

int num_occurrences(char * word, char * line) {
  char buffer[MAX_LINE_LEN];
  char *t;
  int  num_occur = 0;

  strncpy(buffer, line, MAX_LINE_LEN);
  t = strtok(buffer, " ");
  while (t != NULL) {
      if (strcmp(word, t) == 0) {
          num_occur++;
      }
      t = strtok(NULL, " ");
  }

  return (num_occur);
}
/*
Purpose: find the longest word.
Arg: (char *) array of words.
Return: (int) the longest length.
*/
int longest_word (int *num_words_pt) {
  int i = 0;
  int longest = 0;
  for (i = 0; i < *num_words_pt; i ++) {
    if (strlen(words[i]) >= longest) {
      longest = strlen(words[i]);
    }
  }
  return longest;
}


/*
Purpose: modify the word.
Arg: (char **) word, (int) the length of longest word in array.
Return: void
*/
void modify_word(int longest, char * word_pt) {
  char ch;
  ch = ' ';
  int i;
    for (i = 0; i < longest; i ++) {
      // check if char is NULL
      if (*(word_pt +i)) {
        // check if char is lower case
        if (*(word_pt +i) > 96) {
        *(word_pt +i) = *(word_pt +i) - 32;
      }
      } else {
        *(word_pt +i) = ch;
      }

    }
}
/*
Purpose: print the line that contains the word.
Arg    : (int) the order of the word in the unique words array,
         (char *) the unique words array,
         (int *) the num of occurences of word array,
         (char *) lines of text.
Return : void.
*/
void print_line(int word_th, int *num_lines_pt, int *num_words_pt) {
  int i;
  int longest_word_len;
  int num_occur;
  char modified_word[MAX_WORD_LEN];

  longest_word_len = longest_word(num_words_pt);
  for (i = 0; i < *num_lines_pt; i ++) {
    num_occur = num_occurrences(words[word_th], lines[i]);
    strncpy(modified_word, words[word_th], MAX_WORD_LEN);
    modify_word(longest_word_len, modified_word);
    if (num_occur == 1) {
      printf("%s  %s (%d)\n", modified_word, lines[i], i+1);
    } else if (num_occur > 1) {
      printf("%s  %s (%d*)\n", modified_word, lines[i], i+1);
    }
  }

}

int main(int argc, char *argv[]) {
    FILE *infile;
    FILE *language;
    char excp_line[MAX_LINE_LEN];
    char input_line[MAX_LINE_LEN];
    int num_occur[MAX_NUM_KEYWORDS];


    int  num_words = 0;
    int num_lines = 0;
    int  num_exclusion_words = 0;

    int i;


    // char exclusion_words[MAX_EXCLUSION_WORDS][MAX_WORD_LEN];

    if (argc == 4) {
      for (i = 0; i < argc - 1; i ++) {
        if (strcmp(argv[i], "-e") == 0) {
          language = fopen(argv[i + 1], "r+");
          if (language == NULL) {
              fprintf(stderr, "Problems opening %s for reading\n",
                  argv[i + 1]);
              exit(1);
          } else {
              if (i != 1) {
                infile = fopen(argv[1], "r");
              } else {
                infile = fopen(argv[3], "r");
              }
          }
        }
      }
      while (fgets(excp_line, MAX_LINE_LEN, language) != NULL) {
        /* Elliminate the newline character.
         */
        if (excp_line[strlen(excp_line)-1] == '\n') {
            excp_line[strlen(excp_line)-1] = '\0';
        }
        strncpy(exclusion_words[num_exclusion_words], excp_line, MAX_WORD_LEN);
        num_exclusion_words++;
      }
      fclose(language);
    }
    else if (argc == 2) {
      infile = fopen(argv[1], "r");
    }

    else {
      fprintf(stderr, "Invalid arguments\n");
      exit(1);
    }
      while (fgets(input_line, MAX_LINE_LEN, infile) != NULL) {
        /* Elliminate the newline character.
         */
        if (input_line[strlen(input_line)-1] == '\n') {
            input_line[strlen(input_line)-1] = '\0';
        }
        strncpy(lines[num_lines], input_line, MAX_LINE_LEN);
        num_lines ++;

    }
    for (i = 0; i < num_lines; i++) {
        store_the_words(&lines[i][0], num_occur, &num_words, &num_exclusion_words);
    }
    sort(&num_words);

    for (i = 0; i < num_words; i++) {
      print_line(i, &num_lines, &num_words);
    }

    fclose(infile);
  }
