#!/usr/bin/env python3
'''
URLify: Write a method to replace all spaces in a string with %20.
        You may assume that the string has sufficient space at the
        end to hold the additional characters, and that you are given
        the "true" length of the string.

EXAMPLE:   
    Input: "Mr John Smith", 13
    Output: "Mr%20John%20Smith" 
'''

import string
import argparse

#Length is unneeded in Python
def replaceSpace(text):
    return text.replace(' ', '%20')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=
        'Replaces spaces in strings with "%20."')
    parser.add_argument('strings', metavar='s', type=str, nargs='+', 
        help='A string to process')
    args = parser.parse_args()
    for string in args.strings:
        print(replaceSpace(string))
    