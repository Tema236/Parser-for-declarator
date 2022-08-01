#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql

con = pymysql.connect(host='localhost', user='test_user1', password='123456', database='tdbp1')

cursor = con.cursor()

cou_of_str_car = cursor.execute("select * from count_of_cars1")


cursor.execute("select * from count_of_cars1")
row_3 = cursor.fetchall()
maxcars18 = row_3[0][1]
maxcars19 = row_3[0][1]
maxcars20 = row_3[0][1]
srcars18 = 0
srcars19 = 0
srcars20 = 0
coc18 = 0
coc19 = 0
coc20 = 0

for row in row_3:
    #print('{0} {1} {2} {3}'.format(row[0], row[1], row[2], row[3]))
    if row[1] > maxcars18:
        maxcars18 = row[1]
        idcar18 = row[0]

    if row[2] > maxcars19:
        maxcars19 = row[2]
        idcar19 = row[0]

    if row[3] > maxcars20:
        maxcars20 = row[3]
        idcar20 = row[0]

    if row[1] != -1:
        srcars18 += row[1]
        coc18 += 1

    if row[2] != -1:
        srcars19 += row[2]
        coc19 += 1

    if row[3] != -1:
        srcars20 += row[3]
        coc20 += 1

print('\n------------------------------------\n')
cursor.execute(f"select user_name from names where user_id={idcar18}")
row_id = cursor.fetchall()
print('Max cars in 2018: ', maxcars18, '| user id: ', idcar18, '| Name: ', row_id[0][0])
cursor.execute(f"select user_name from names where user_id={idcar19}")
row_id = cursor.fetchall()
print('Max cars in 2019: ', maxcars19, '| user id: ', idcar19, '| Name: ', row_id[0][0])
cursor.execute(f"select user_name from names where user_id={idcar20}")
row_id = cursor.fetchall()
print('Max cars in 2020: ', maxcars20, '| user id: ', idcar20, '| Name: ', row_id[0][0])
print('\n------------------------------------\n')
print('Srednee cars for 1 person 2018: ', srcars18/coc18)
print('Srednee cars for 1 person 2019: ', srcars19/coc19)
print('Srednee cars for 1 person 2020: ', srcars20/coc20)
print('\n------------------------------------\n')
print('Kol-vo neykazannih cars in 2018: ', cou_of_str_car - coc18)
print('Kol-vo neykazannih cars in 2019: ', cou_of_str_car - coc19)
print('Kol-vo neykazannih cars in 2020: ', cou_of_str_car - coc20)


cursor.execute("select * from year_income")
row_4 = cursor.fetchall()
maxinc18 = row_4[0][1]
maxinc19 = row_4[0][1]
maxinc20 = row_4[0][1]


for row in row_4:
    #print('{0} {1} {2} {3}'.format(row[0], row[1], row[2], row[3]))
    if row[1] > maxinc18:
        maxinc18 = row[1]
        idinc18 = row[0]

    if row[2] > maxinc19:
        maxinc19 = row[2]
        idinc19 = row[0]

    if row[3] > maxinc20:
        maxinc20 = row[3]
        idinc20 = row[0]

print('\n------------------------------------\n')
cursor.execute(f"select user_name from names where user_id={idinc18}")
row_id = cursor.fetchall()
print('Max income in 2018: ', maxinc18, '| user id: ', idinc18, '| Name: ', row_id[0][0])
cursor.execute(f"select user_name from names where user_id={idinc19}")
row_id = cursor.fetchall()
print('Max income in 2019: ', maxinc19, '| user id: ', idinc19, '| Name: ', row_id[0][0])
cursor.execute(f"select user_name from names where user_id={idinc20}")
row_id = cursor.fetchall()
print('Max income in 2020: ', maxinc20, '| user id: ', idinc20, '| Name: ', row_id[0][0])


cursor.execute("select * from year_realestate")
row_4 = cursor.fetchall()
maxr18 = row_4[0][1]
maxr19 = row_4[0][1]
maxr20 = row_4[0][1]


for row in row_4:
    #print('{0} {1} {2} {3}'.format(row[0], row[1], row[2], row[3]))
    if row[1] > maxr18:
        maxr18 = row[1]
        idr18 = row[0]

    if row[2] > maxr19:
        maxr19 = row[2]
        idr19 = row[0]

    if row[3] > maxr20:
        maxr20 = row[3]
        idr20 = row[0]

print('\n------------------------------------\n')
cursor.execute(f"select user_name from names where user_id={idr18}")
row_id = cursor.fetchall()
print('Max realestate in 2018: ', maxr18, '| user id: ', idr18, '| Name: ', row_id[0][0])
cursor.execute(f"select user_name from names where user_id={idr19}")
row_id = cursor.fetchall()
print('Max realestate in 2019: ', maxr19, '| user id: ', idr19, '| Name: ', row_id[0][0])
cursor.execute(f"select user_name from names where user_id={idinc20}")
row_id = cursor.fetchall()
print('Max realestate in 2020: ', maxr20, '| user id: ', idr20, '| Name: ', row_id[0][0])
con.close()