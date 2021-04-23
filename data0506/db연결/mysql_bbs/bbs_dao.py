import pymysql


def create(id, title, content, writer):
    con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
    cur = con.cursor()
    sql = 'insert into bbs values("' + id + '","' + title + '","' + content + '","' + writer + '")'
    cur.execute(sql)
    con.commit()
    con.close()


def read(id):
    con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
    cur = con.cursor()
    sql = "select * from bbs where id = %s"
    cur.execute(sql, id)
    row = cur.fetchone()
    print(row)
    con.close()


def read_all():
    con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
    cur = con.cursor(pymysql.cursors.DictCursor)
    sql = "select * from bbs"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    con.close()


def update(id, title):
    con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
    cur = con.cursor()
    data = (title, id)
    sql = "update bbs set title = %s where id =%s"
    cur.execute(sql, data)
    con.commit()
    con.close()
