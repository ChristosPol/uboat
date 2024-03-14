from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
data = pd.read_csv("Links.csv")
Ordered=[]
Ordered=[]
Laid=[]
Launched=[]
Commissioned=[]
Commanders=[]
Successes=[]
Fate=[]
for names in data['Links']:
    url=names
    print(names)
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    Ordered.append(soup.find('td', string="Ordered").find_next_sibling("td").text)
    Laid.append(soup.find('td', string="Laid down").find_next_sibling("td").text)
    Launched.append(soup.find('td', string="Launched").find_next_sibling("td").text)
    Commissioned.append(soup.find('td', string="Commissioned").find_next_sibling("td").text)
    Commanders.append(soup.find('td', string="Commanders").find_next_sibling("td").text)
    Successes.append(soup.find('td', string="Successes").find_next_sibling("td").text)
    Fate.append(soup.find('td', string="Fate").find_next_sibling("td").text)
    time.sleep(1)

d = {'UBoat':data['Name'],'Ordered': Ordered, 'Laid': Laid, 'Launched': Launched, 'Commissioned': Commissioned
     , 'Commanders': Commanders, 'Successes': Successes, 'Fate': Fate}
df = pd.DataFrame(data=d)
df.to_csv("./data.csv", sep=',',index=False)
