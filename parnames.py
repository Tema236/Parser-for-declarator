# scraper.py
import requests
from bs4 import BeautifulSoup
import json
import re
import pymysql

con = pymysql.connect(host='localhost', user='test_user1', password='123456', database='tdbp1')
cursor = con.cursor()

us_id = 132870

for i in range(0, 200):
    url = f'https://declarator.org/person/{us_id}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('h1', class_='title')

    for quote in quotes:
        a = str(quote.text).replace(' ','')
        reg = re.split('\s+', a)
        name = (reg[1])

    sql1 = f"INSERT INTO names (user_id, user_name) VALUES ({us_id}, '{name}')"
    print(sql1)
    cursor.execute(sql1)
    con.commit()
    print('completed')

    us_id += 1