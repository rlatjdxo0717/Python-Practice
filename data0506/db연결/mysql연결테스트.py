import pymysql

con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
print(con.get_host_info())

cur = con.cursor()
print(cur)

sql = 'insert into member values("python1","python2","python3","python4")'
cur.execute(sql)
con.commit()