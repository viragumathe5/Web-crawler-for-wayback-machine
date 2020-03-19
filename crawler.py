from bs4 import BeautifulSoup
import urllib.request



with urllib.request.urlopen("https://www.pixar.com/feature-films/cars-3") as reply:
    html = reply.read()  


soup = BeautifulSoup(html)

print(soup)


links = []

links = soup.findAll("img")


print("<********************************************************************************************************>")
print("<********************************************************************************************************>")

print(links)


for link in links:
    print(link.get("src"))       

