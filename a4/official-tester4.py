#!/usr/bin/env python3

#
# UVic SENG 265, Spring 2020, Assignment #4
#
# This test-driver program invokes methods on the class to be
# completed for the assignment.
#
# THIS IS THE VERSION OF THE TESTER THAT WILL BE USED WITH
# YOUR SUBISSION OF concordance.py.
#

import sys
import argparse
from concordance import KWOC


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', type=str, help='exception-word file')
    parser.add_argument('infile', type=str, help='input text file')

    args = parser.parse_args()
    if not args.infile:
        print("Need an infile...")
        sys.exit(1)

    # orig_stdout = sys.stdout
    # sys.stdout = None
    input_txt = open(args.infile, "r")
    lines = []
    for line in input_txt:
        line = line.rstrip("\n")
        lines.append(line)
    # print(lines)
    # print()
    # print(args.e)

    kwoc = KWOC(args.infile, args.e)
    result = kwoc.concordance()

    # sys.stdout = orig_stdout
    if result != []:
        print("\n".join(result))


if __name__ == "__main__":
    main()
