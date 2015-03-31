#coding=utf-8
import sqlite3

conn = sqlite3.connect("../sqlite3/test.db")
cursor = conn.cursor()

#建立数据库
#sql = '''create table students (name text, username text, id int)'''
#cursor.execute(sql)
#cursor.close()

#插入数据
'''
print "Let's input some students!"
while True:
    name = raw_input("Student's name: ")
    username = raw_input("Student's username: ")
    id_num = raw_input("Student's id number: ")
    sql = "insert into students values(:st_name,:st_username,:id_num)"
    cursor.execute(sql,{'st_name':name,'st_username':username,'id_num':id_num})
    conn.commit()
    cont = raw_input("Another student? ")
    if cont[0].lower() == "n":
        break
cursor.close()
'''

#查询数据
sql = "select * from students"
results = cursor.execute(sql)
all_students = results.fetchall()
for student in all_students:
    print student
