#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb

db=MySQLdb.connect(host="localhost",db="test",user="root",passwd="123456",charset="utf8")


cursor=db.cursor()


cursor.execute("select * from test")

data=cursor.fetchone()

print data

#插入一条记录
cursor.execute("INSERT INTO test ( name, sms_theme) VALUES (%s,%s)",(("天蓝","秋天")))
#插入多条记录
cursor.executemany("INSERT INTO test ( name, sms_theme) VALUES (%s,%s)",(('西方不败', '232'),("天蓝","秋天")))

#cursor.execute("update test set sms_theme=%s where id=1",("秋天不回来"))

#cursor.execute("delete from test where id=%d",(2))

#数据变更操作，必须commit
db.commit()

cursor.execute("select * from test")

alldata=cursor.fetchall()

for i in alldata:

    print i

#实现将读取到的数据变成字典形式
cur=db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

cur.execute("select * from test")

alllines=cur.fetchall()

for line in alllines:
    print line

#关闭连接
cursor.close()
cur.close()
db.close();
