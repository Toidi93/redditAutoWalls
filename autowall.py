import praw
import requests
import os
from secret import secret
from PIL import Image
from time import sleep

# TODO: lav menu / download billeder eller set random wallpapir

SAVE_FOLDER = "/home/henrik/Desktop/wallpapers/"


def main():
    reddit = praw.Reddit(
        client_id="8lMM3nLN0uuT6Q",
        client_secret=secret,
        user_agent="python: v1.0.0 (by u/Toidix)"
    )

    #sub = input("Write subreddit: ")
    sub = "Wallpaper"


    downloadSave(reddit, sub)

    print("Finished!")


def downloadSave(reddit, sub):
    """ Download and save img """
    for submission in reddit.subreddit(sub).hot(limit=200):
        if not isImage(submission.url.split(".")[-1]):
            continue
        fileName = submission.title + "." + submission.url.split(".")[-1]
        url = submission.url

        if os.path.isfile(SAVE_FOLDER + fileName):
            continue

        res = requests.get(url)
        open(SAVE_FOLDER + fileName, 'wb').write(res.content)
        filePlace = SAVE_FOLDER + fileName

        image = Image.open(filePlace)
        width, height = image.size
        if height > width: continue

        os.system(f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri '{filePlace}'")

        return


def isImage(filetype):
    imgTypes = ["jpg", "pgn"]
    return filetype in imgTypes


if __name__ == '__main__':
    while True:
        main()
        sleep(5)
