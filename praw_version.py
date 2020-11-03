import praw
import requests
import os
from secret import secret

# TODO: lav menu / download billeder eller set random wallpapir 
# TODO: Check if url is image

def main():
    reddit = praw.Reddit(
    client_id="8lMM3nLN0uuT6Q",
    client_secret=secret,
    user_agent="python: v1.0.0 (by u/Toidix)"
    )

    sub = input("Write subreddit: ")

    for submission in reddit.subreddit(sub).top(limit=10):
        fileName = submission.title
        url = submission.url

        if not os.path.isfile("/home/henrik/Desktop/wallpapers/" + fileName):
            res = requests.get(url, allow_redirects=True)
            open("/home/henrik/Desktop/wallpapers/" + fileName, 'wb').write(res.content)

    print("Finished!")


if __name__ == '__main__':
    main()