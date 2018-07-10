import pymysql

conn = pymysql.connect(host="localhost",
       user="root",password="123456",
       database="db4",charset="utf8")
cursor1 = conn.cursor()
try:
    sql_select = "select * from sheng;"
    cursor1.execute(sql_select)
    data = cursor1.fetchone()
    print(data)
    print("*************************")

    data2 = cursor1.fetchmany(3)
    for i in data2:
        print(i)
    print("*************************")

    data3 = cursor1.fetchall()
    for i in data3:
        print(i)

    print("ok")
    conn.commit()
except Exception as e:
    print(e)

cursor1.close()
conn.close()















