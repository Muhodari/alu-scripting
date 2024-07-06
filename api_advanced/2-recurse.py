#!/usr/bin/python3
""" recurse.py """
import requests

def get_hot_titles(subreddit, titles=[], after=None):
    """Returns a list of titles of all hot articles in a subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {"after": after}
    response = requests.get(
                            url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()["data"]
        titles += [post["data"]["title"] for post in data["children"]]
        if data["after"] is None:
            return titles
        else:
            return get_hot_titles(subreddit, titles, data["after"])
    elif response.status_code == 404:
        return None
