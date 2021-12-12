import requests


def check_url_validity(urls):
    for url in urls:
        try:
            requests.get(url)
            print(f"{url} is up!")
        except:
            print(f"{url} is down!")


print("Welcome to IsItDown.py!")
start_over = 'y'
while start_over == 'y':
    URLs = input("Please write a URL or URLs you want to check. (separated by comma)\n")
    URLs = [
        url.strip().lower() if 'http://' in url else 'http://' + url.strip().lower()
        for url in URLs.split(',')
    ]
    check_url_validity(URLs)
    start_over = input("Do you want to start over? y/n ")
