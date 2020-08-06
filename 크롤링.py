from bs4 import *
import urllib.request
url2="https://ohou.se/contents/card_collections?style=5"
req2 = urllib.request.urlopen(url2)
res2 = req2.read().decode('utf-8')
soup = BeautifulSoup(res2, 'html.parser')
e =soup.find_all('a', {'class': 'card-item__content__link'})
for t in e:
    url = "https://ohou.se"+t['href']
    req = urllib.request.urlopen(url)
    res = req.read().decode('utf-8')
    soup = BeautifulSoup(res, 'html.parser')
    a = soup.find_all('img', {'class': 'card-detail-card-image__image'})
    b = soup.find_all('p', {'class': 'card-detail-card__description'})
    c = soup.find_all('span', {'class': 'card-detail-header__prop'})
    c1=c[0].text
    if c1.find("스타일") > 0:
        print("10평 미만"+c[0].text+c[1].text)
    else:
        print(c[0].text+c[1].text+c[2].text)
    for i in range(len(a)):
        print(a[i]['src'])  # 사진
        print(b[i].text)    # 내용

