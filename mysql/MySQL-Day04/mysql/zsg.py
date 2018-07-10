import pymysql

# 1.创建数据库连接对象
conn = pymysql.connect(host="localhost",
       user="root",password="123456",
       database="db4",charset="utf8")
# 2.创建游标对象
cursor1 = conn.cursor()
# 3.利用execute方法执行sql命令
try:
    sql_insert = "insert into sheng(s_name) \
                  values ('台湾省');"
    cursor1.execute(sql_insert) # 增加数据
    sql_delete = "delete from sheng where id=2;"
    cursor1.execute(sql_delete) # 删除数据
    sql_update = "update sheng set s_name='修改' \
                  where id=1;"
    cursor1.execute(sql_update) # 修改记录
    print("ok")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("出现错误，已回滚",e)

cursor1.close() # 关闭游标对象
conn.close() # 关闭数据库连接

















