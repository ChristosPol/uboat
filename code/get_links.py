from bs4 import BeautifulSoup
import requests
import pandas



page = requests.get('https://uboat.net/boats/listing.html')
content = page.content
soup = BeautifulSoup(content, 'html.parser')# print(soup.prettify())

p1 = str(soup.select('#content > p:nth-child(6)')).split(',')[ : -1]
p2 = str(soup.select('#content > p:nth-child(7)')).split(',')[ : -1]
p3 = str(soup.select('#content > p:nth-child(8)')).split(',')[ : -1]
p4 = str(soup.select('#content > p:nth-child(9)')).split(',')[ : -1]
p5 = str(soup.select('#content > p:nth-child(10)')).split(',')[ : -1]
p=p1+p2+p3+p4+p5

boat_names=[]
for i in p:
    mk1 = i.find('/u') + 1
    mk2 = i.find('.htm', mk1)
    boat_names.append(i[mk1 : mk2])

#boat_names = boat_names[ : -1]

boat_links=[]
for names in boat_names:
    boat_links.append('https://uboat.net/boats/'+names+'.htm')

df = pandas.DataFrame(data={"Name":boat_names,"Links": boat_links})
df.to_csv("./Links.csv", sep=',',index=False)
print(df)

# pip freeze > requirements.txt
# pip install -r requirements.txt
