'''SQL语句参数化'''

import pymysql
conn = pymysql.connect(host="localhost",
       user="root",password="123456",
       database="db4",charset="utf8")
cursor1 = conn.cursor()
try:
    name = input("请输入省:")
    s_id = input("请输入对应编号:")
    sql_insert = "insert into sheng(s_name,s_id)\
                  values(%s,%s);"
    cursor1.execute(sql_insert,[name,s_id])
    print('ok')
    conn.commit()
except Exception as e:
    conn.rollback()
    print("出现错误,已回滚",e)



cursor1.close()
conn.close()