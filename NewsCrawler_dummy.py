from bs4 import BeautifulSoup
import bs4
import urllib.request

def get_soup_from_url(url: str ) -> BeautifulSoup:

    with urllib.request.urlopen(url) as reply:
        return BeautifulSoup(reply.read(), 'html.parser') 


if __name__ == "__main__":

    soup = get_soup_from_url("https://www.washingtonpost.com/us-policy/2020/03/24/trump-coronavirus-congress-economic-stimulus/")

    content1 = []

    print(f"\n<{'*' * 104}>\n")

    content1 = soup.find('h1', {"class": "font--headline gray-darkest mb-sm null"})

    print(content1.get_text())

    print(f"\n<{'*' * 104}>\n")
