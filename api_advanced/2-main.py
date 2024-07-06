#!/usr/bin/python3
"""
main.py
"""
import sys

if __name__ == '__main__':
    get_hot_titles = __import__('recurse').get_hot_titles
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = get_hot_titles(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
