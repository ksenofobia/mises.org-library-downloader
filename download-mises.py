#!/bin/env python
import urllib3
import re
import requests
from sys import stdout
import os
JUMP_LEFT_SEQ = '\u001b[100D'

url = "https://mises.org/library/books?book_type=All&title=All&author=All&topic=All&austrian_school=All&level=All&page="
# as of 14.05.2021 there are 70 pages on mises library
pages = 70


def get_page(page=str):
    # urllib3 magic
    http = urllib3.PoolManager()
    url_request = http.request('GET', page)
    # convert recieved bytes to string
    url_response = url_request.data.decode('utf-8')

    # pattern matching pdf links
    link_pattern = re.compile(
        r'(http|https)(:\/\/cdn.mises.org)([\s\w\-\.,@?^=%&:/~\+#]*[\s\w\-\@?^=%&/~\+#])?(.pdf)')
    matched = link_pattern.findall(url_response)
    return matched


def get_pdf(links=list):
    # convert tuples to list items
    for i in links:
        # join current tuple to get the link
        book_url = ''.join(i)
        # join tuples from [2] to [3] included and remove [0] charater(always'/')
        book_title = ''.join(i[2:4])[1:]
        # print(f"Downloading {book_title} from {book_url}\n")
        book_request = requests.get(book_url)
        with open(book_title, "wb") as file:
            file.write(book_request.content)
        # print(f"Successfully downloaded {book_title}!\n")


def main():
    try:
        for i in range(pages):
            current_url = url + str(i)
            # print(f"Looking on {i} of {pages} pages.\n")
            print(JUMP_LEFT_SEQ, end='')
            print(f'Downloading books from pages: {i + 1}/{pages}', end='')
            stdout.flush()
            list_of_links = get_page(current_url)
            get_pdf(links=list_of_links)
        print("\nDone!\nTaxation is theft.")
    except KeyboardInterrupt:
        leftovers = ["urllib3", "re", "requests"]
        for i in leftovers:
            if os.path.exists(i):
                os.remove(i)
            else:
                pass
        exit(0)


if __name__ == "__main__":
    main()
