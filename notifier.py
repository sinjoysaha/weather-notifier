from bs4 import BeautifulSoup
import notify2
import requests

url = "https://weather.com/en-IN/weather/today/l/93129bd249f38a036dca3f85c159235f0e109334e73454e7d1251d904979ad69"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

temp = soup.findAll('div', class_ = "today_nowcard-temp")
temp = str(temp[0]).split('<span class="">')
temp =temp[1].split('<sup>')
temp = temp[0]

phrase = soup.findAll('div', class_ = "today_nowcard-phrase")
phrase = str(phrase[0]).split('phrase">')
phrase = phrase[1].split('<')[0]

notify2.init('NotiPy')
title = phrase
body = temp+' °C'
n = notify2.Notification(title, body)
n.set_timeout(1000)
n.set_location(1400,20)

n.show()

