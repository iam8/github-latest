# Ioana A Mititean
# 12/15/21
# UWPCE Course 3 - Internet Programming in Python
# Lesson 06 - Using APIs and Getting Started with Django

"""
Script that retrieves a list of GitHub 'events' for a specified GitHub user, and then prints out
the time stamp associated with the first event in that list.

User 'events' include things like pushing to a repo or opening up an issue on a repo.

The GitHub username is entered via the command line, as below:
    > python main.py username
"""

import json
import sys

import requests


if __name__ == "__main__":

    username = sys.argv[1]

    events_info = requests.get(f"https://api.github.com/users/{username}/events")
    time_first = events_info.json()[0]["created_at"]

    print(f"An event associated with the user '{username}' occurred at {time_first}.")
