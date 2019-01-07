import bs4
import csv
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/rss?hl=th&gl=TH&ceid=TH:th"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)

myData = [[1, 2, 3], ['news.title.text', 'news.link.text', 'news.pubDate.text']]
csv.register_dialect('myDialect', delimiter='/', quoting=csv.QUOTE_NONE)
myFile = open('googlenews.csv', 'w')  
with myFile:  
   writer = csv.writer(myFile, dialect='myDialect')
   writer.writerows(myData)
