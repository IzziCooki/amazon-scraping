import requests
import re
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Turtle-Beach-Gaming-Headset-PlayStation/dp/B00ZC3S818/?_encoding=UTF8&pf_rd_p=7ea15e7b-fb3f-4eb6-95b9-585f7ccb8346&pd_rd_wg=szula&pf_rd_r=KT7M9F4RT4RV5RB7XZKG&pd_rd_w=GP3DX&pd_rd_r=03d83078-c27c-4ef1-82d3-e891eb8976f6&ref_=pd_gwm_bmx_gp_8b80hvqo"


def scrape_amazon(url):
    r = requests.get(url)

    r = requests.get(url, headers={
                     "User-Agent": "Chrome OS/Chrome browser: Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"})

    soup = BeautifulSoup(r.content, "html.parser")

    title = soup.select("#productTitle")[0].get_text()
    pricev2 = soup.find("span", {"class": "a-offscreen"}).get_text()

    description = soup.select("#feature-bullets")[0].get_text()

    return {"Title": title, "Price": pricev2, "Description": description}


