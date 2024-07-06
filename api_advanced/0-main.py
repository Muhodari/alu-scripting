#!/usr/bin/python3
"""
main.py
"""
import sys

if __name__ == '__main__':
    get_top_ten = __import__('top_ten').get_top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        get_top_ten(sys.argv[1])
