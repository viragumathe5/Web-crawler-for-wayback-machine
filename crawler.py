from bs4 import BeautifulSoup
import bs4
import urllib.request


def get_soup_from_url(url: str = "https://www.pixar.com/feature-films/cars-3") -> bs4.BeautifulSoup:

    with urllib.request.urlopen(url) as reply:
        html = reply.read()  


    soup = BeautifulSoup(html)

    print(soup)


    links = []

    links = soup.findAll("img")

    print(links)


    for link in links:
        print(link.get("src"))       



get_soup_from_url()
        


    #print(links)

