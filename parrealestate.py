import requests
import json
from bs4 import BeautifulSoup
import pymysql

con = pymysql.connect(host='localhost', user='test_user1', password='123456', database='tdbp1')
cursor = con.cursor()
us_id = 132870

for i in range(0,200):
    url = f'https://declarator.org/api/get-year-realestate/{us_id}/?format=json'
    sql1 = f"INSERT INTO year_realestate (user_id, year_2018, year_2019, year_2020) VALUES ({us_id}, -1, -1, -1)";
    cursor.execute(sql1)
    con.commit()

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    parsed_string = json.loads(soup.text)

    print(parsed_string)

    for i in range(0,parsed_string["count"]):
        if (parsed_string["results"][i]['document__income_year']) == 2018 or (parsed_string["results"][i]['document__income_year']) == 2019 or (parsed_string["results"][i]['document__income_year']) == 2020:
            a1 = str('year_') + str(parsed_string["results"][i]['document__income_year'])
            a2 = parsed_string["results"][i]["year_realestate"]
            if a2 == None:
                a2 = -1
            sql = f"UPDATE year_realestate SET {a1}={a2} WHERE user_id = {us_id}"
            print(sql)
            cursor.execute(sql)
            con.commit()
        else:
            pass

    us_id += 1