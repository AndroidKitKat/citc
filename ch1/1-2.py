#!/usr/bin/env python3
'''
Check Permutation: Given two strings, write a method to decide if one
                   is a permutation of the other.
'''

import string
import argparse
import sys

def checkPermutation(stringOne, stringTwo):
    #first test, skips the bullshit below
    if len(stringOne) is not len(stringTwo):
        return False

    sortedStringOne = sorted(stringOne)
    print(sortedStringOne)
    sortedStringTwo = sorted(stringTwo)
    print(sortedStringTwo)
    # ok so this is bad and slow and bad
    for letter in range(len(sortedStringOne)):
        if sortedStringOne[letter] is not sortedStringTwo[letter]:
            return False
    return True
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
        'Checks to see if a string is a permutation of another')
    parser.add_argument('strings', metavar='s', type=str, nargs='+',
        help='Strings to check (max 2)')
    args = parser.parse_args()
    if len(args.strings) is not 2:
        print("Two String Maximum", file=sys.stderr)
        sys.exit(1)
    
    if checkPermutation(args.strings[0], args.strings[1]):
        print("These two strings are permutations of each other")
    else:
        print("These two strings are not permutations of each other")