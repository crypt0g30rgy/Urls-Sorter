import requests

urls = []

with open('urls.txt', 'r') as f:  # reading urls from file
    urls = [line.strip() for line in f.readlines()]

urls_visited = []

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        urls_visited.append(url)

with open('visited_urls.txt', 'w') as f:  # saving visited urls to file
    for url in urls_visited:
        f.write(url + "\n")