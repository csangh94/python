from selenium import webdriver
import time
import urllib.request
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import pymysql
import re
from datetime import datetime

driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')
driver.implicitly_wait(3)
test_list = []

for t in range(0, 8):
    driver.get('https://ohou.se/contents/card_collections?style=' + str(t))
    body = driver.find_element_by_css_selector('body')

    for i in range(15):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('a', {'class': 'card-item__content__link'})
        for x in a:
            test_list.append(x['href'])
    time.sleep(3)
test_t = set(test_list)
for x in test_t:
    url = "https://ohou.se" + x
    if url == "https://ohou.se/contents/card_collections/3538349?affect_type=CardIndex&affect_id=0" or url =="https://ohou.se/contents/card_collections/3808870?affect_type=CardIndex&affect_id=0":
        pass
    else:
        req = urllib.request.urlopen(url)
        res = req.read().decode('utf-8')
        soup = BeautifulSoup(res, 'html.parser')
        a = soup.find_all('img', {'class': 'card-detail-card-image__image'})
        b = soup.find_all('p', {'class': 'card-detail-card__description'})
        c = soup.find_all('span', {'class': 'card-detail-header__prop'})
        c1 = c[0].text
        sss = "10평 미만"
        eee = "아파트"
        ttt = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        img_url = ""
        content = ""
        for i in range(len(a)):
            img_url = img_url + a[i]['src'] + ","
            # if len(a) == 0:
            # content = content + b[i].text + "/"
            # else:
            content = content + re.sub(pattern='[^\w\s]', repl='', string=b[i].text).replace("\n", " ") + "/"
        if len(c) == 2:
            conn = pymysql.connect(host='localhost', port=3708, user='root', password='1234', db='living',
                                   charset='utf8')
            curs = conn.cursor()
            print(content)
            print(c)
            sql = "insert into interior_info(sqft,style,type,photo,content,day,mid) values('" + sss + "','" + c[
                0].text + "','" + c[
                      1].text + "','" + img_url[:-1] + "','" + content[:-1] + "','" + ttt + "','" + "a"+str(i) + "')"
            curs.execute(sql)
            conn.commit()
            conn.close()
        elif len(c) == 1:
            conn = pymysql.connect(host='localhost', port=3708, user='root', password='1234', db='living',
                                   charset='utf8')
            curs = conn.cursor()
            print(content)
            print(c)
            sql = "insert into interior_info(sqft,style,type,photo,content,day,mid) values('" + sss + "','" + c[
                0].text + "','" + eee + "','" + img_url[:-1] + "','" + content[:-1] + "','" + ttt + "','" +"a"+str(i)+ "')"
            curs.execute(sql)
            conn.commit()
            conn.close()
        else:
            conn = pymysql.connect(host='localhost', port=3708, user='root', password='1234', db='living',
                                   charset='utf8')
            curs = conn.cursor()

            sql = "insert into interior_info(sqft,style,type,photo,content,day,mid) values('" + c[
                0].text + "','" + c[
                1].text + "','" + c[
                      2].text + "','" + img_url[:-1] + "','" + content[:-1] + "','" + ttt + "','" + "a" + str(i) + "')"
            print(content)
            print(c)
            curs.execute(sql)
            conn.commit()
            conn.close()
