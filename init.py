#! urr/bin/python
# coding:utf-8

import MySQLdb

conn=MySQLdb.connect(host="192.168.100.40",user="360_hqb",passwd="360hqb",db="okhqb",charset="utf8")

cursor=conn.cursor()

cursor.execute("insert into member_game_code(code) values(%s)",(("fsavwfe")))

conn.commit()

cursor.close()

conn.close()
