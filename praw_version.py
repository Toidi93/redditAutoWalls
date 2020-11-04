import praw
import requests
import os
from secret import secret

# TODO: lav menu / download billeder eller set random wallpapir

SAVE_FOLDER = "/home/henrik/Desktop/wallpapers/"


def main():
    reddit = praw.Reddit(
        client_id="8lMM3nLN0uuT6Q",
        client_secret=secret,
        user_agent="python: v1.0.0 (by u/Toidix)"
    )

    sub = input("Write subreddit: ")
    #sub = "wallpapers"
    num = int(input("Number of images to download: "))
    #num = 2

    downloadSave(reddit, sub, num)

    print("Finished!")


def downloadSave(reddit, sub, num):
    """ Download and save img """
    for submission in reddit.subreddit(sub).hot(limit=num):
        if not isImage(submission.url.split(".")[-1]):
            continue
        fileName = submission.title + "." + submission.url.split(".")[-1]
        print(fileName)
        url = submission.url

        if not os.path.isfile(SAVE_FOLDER + fileName):
            res = requests.get(url)
            open("/home/henrik/Desktop/wallpapers/" +
                 fileName, 'wb').write(res.content)


def isImage(filetype):
    imgTypes = ["jpg", "pgn"]
    return filetype in imgTypes


if __name__ == '__main__':
    main()
