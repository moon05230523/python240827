# db1.py

import sqlite3

#con = sqlite3.connect(":memory:")
con = sqlite3.connect(r"c:\work\test.db")
cur = con.cursor()
cur.execute("create table if not exists PhoneBook (Name text, PhoneNum text);")

cur.execute("insert into PhoneBook values ('derick', '010-111');")

cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

name = "전우치"
phoneNum = "010-222"
cur.execute("insert into PhoneBook values (?,?);", (name, phoneNum))

cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

datalist = (("이순신","010-123"),("박문수","010-567"))
cur.executemany("insert into PhoneBook values (?,?);", datalist)

cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)


