from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_soup_from_url(url: str) -> BeautifulSoup:
    with urlopen(url) as reply:
        return BeautifulSoup(reply.read())


if __name__ == "__main__":
    soup = get_soup_from_url("https://www.pixar.com/feature-films/cars-3")
    print(soup)
    print(f"\n<{'*' * 104}>\n")
    links = soup.find_all("img")
    print(f"\n<{'*' * 104}>\n")
    print(links)
    print(f"\n<{'*' * 104}>\n")
    sources = [src for img in soup.find_all("img") if (src := img.get("src"))]
    f"{len(sources) / len(links)*100:.2f}% of imgs have a src attribute."
    for i, src in enumerate(sources, 1):
        print(f"{i:>4}: {src}")
