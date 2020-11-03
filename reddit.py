import requests

def main():
    # wallpaper soure
    url = "https://www.reddit.com/r/wallpaper.json"

    #get request of url and show resault
    res = requests.get(url)
    if not check_request(res.status_code): return
    print(res.json())


""" Function to check for good request """
def check_request(statusCode):
    if statusCode == 200:
        print("Yay!")
        return True
    elif statusCode == 429:
        print("Too many requests")
    else:
        print(f"fail status code: {statusCode}")
    return False


if __name__ == '__main__':
    main()