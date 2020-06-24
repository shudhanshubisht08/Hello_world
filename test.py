import requests
import bs4
res = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
# print(type(res))
# # print(res.text)
#
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# # print(type(soup))
# hi = soup.select('title')
# # print(hi[0].getText())
