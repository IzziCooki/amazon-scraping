import requests
import re
from bs4 import BeautifulSoup


def scrape_amazon(url):
    r = requests.get(url)

    r = requests.get(url, headers={
                     "User-Agent": "Chrome OS/Chrome browser: Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"})

    soup = BeautifulSoup(r.content, "html.parser")

    title = soup.select("#productTitle")[0].get_text()
    pricev2 = soup.find("span", {"class": "a-offscreen"}).get_text()

    description = soup.select("#feature-bullets")[0].get_text()

    return {"Title": title, "Price": pricev2, "Description": description}


