from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_soup_from_url(url: str) -> BeautifulSoup:
    with urlopen(url) as reply:
        return(reply.read())


if __name__ == "__main__":
    soup = get_soup_from_url("https://www.pixar.com/feature-films/cars-3")
    print(soup)
    print(f"\n<{'*' * 104}>\n")
    links = soup.findAll("img")
    print(f"\n<{'*' * 104}>\n")
    print(links)
    print(f"\n<{'*' * 104}>\n")
    for link in links:
        print(link.get("src"))
