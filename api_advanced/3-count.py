#!/usr/bin/python3
""" count_words.py """
import requests


def count_words(subreddit, word_list, after="", counts=[]):
    """Prints a sorted count of given keywords from a subreddit."""

    if after == "":
        counts = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            params={'after': after},
                            allow_redirects=False,
                            headers={'User-Agent': 'Mozilla/5.0'})

    if response.status_code == 200:
        data = response.json()

        for topic in data['data']['children']:
            title_words = topic['data']['title'].split()
            for word in title_words:
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        counts[i] += 1

        after = data['data']['after']
        if after is None:
            merged_counts = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        merged_counts.append(j)
                        counts[i] += counts[j]

            sorted_counts = (
                sorted(zip(word_list, counts),
                       key=lambda x: (-x[1], x[0].lower())))

            for i in range(len(word_list)):
                if (counts[i] > 0) and i not in merged_counts:
                    print("{}: {}".format(word_list[i].lower(), counts[i]))
        else:
            count_words(subreddit, word_list, after, counts)
