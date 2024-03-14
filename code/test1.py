from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

link="https://uboat.net/boats/u5.htm"
page = requests.get(link)
content = page.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.find_all("td", string="marker"))


# text = soup.select_one('script').get_text()
# print(text)
# text = text.split("ue_mid = '")[1]
# text = text.split("',")[0]
# print(text)