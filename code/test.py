# find() method will search the
# given marker and stores its index
# sampleStr='<a href="/boats/u2.htm">U-2</a>'
# mk1 = sampleStr.find('/u') + 1
# mk2 = sampleStr.find('.htm', mk1)
# subString = sampleStr[ mk1 : mk2 ]
# print(mk1, mk2)
# print(subString)
# name='u104'
# strings='https://uboat.net/boats/'+name+'.htm'
from bs4 import BeautifulSoup
import requests
page = requests.get('https://uboat.net/boats/u1.htm')
content = page.content
soup = BeautifulSoup(content, 'html.parser')
Fate=[]

Fate.append(soup.find('td', string="Fate").find_next_sibling("td").text)
print(Fate)