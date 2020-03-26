from src.crawler import get_banner, get_soup_from_url

if __name__ == "__main__":
    banner = get_banner()
    soup = get_soup_from_url("https://www.washingtonpost.com/us-policy/2020/03/24/"
                             "trump-coronavirus-congress-economic-stimulus/")
    print(banner)
    headline = soup.find('h1', {"class": "font--headline gray-darkest mb-sm null"})
    print(headline.get_text())
    print(banner)
