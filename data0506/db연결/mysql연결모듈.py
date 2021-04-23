import pymysql # alt + Enter

#DAO 역할 모듈: CRUD(DML)

#정형데이터 = > mysql, oracle, sqlite3 (RDBMS,관계형 데이터베이스)
def create(id, pw, name, tel):

    con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into member values("' + id + '","' + pw + '","' + name + '","' + tel + '")'
    cur.execute(sql)
    con.commit()
    con.close()

def create2(data):

    con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into member values(%s, %s, %s, %s)'
    result = cur.execute(sql,data)
    print('처리결과 : ',result, '개')
    con.commit()
    con.close()

def create3(datas):

    con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into member values(%s, %s, %s, %s)'
    result = cur.executemany(sql,datas)
    print('처리결과 :',result, '개')
    con.commit()
    con.close()

def read():
    con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = "select * from member where id = 'apple'"
    cur.execute(sql)

    row = cur.fetchone()
    # cur.fetchall() : 조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(row)
    print(type(row))
    print(row[0])

    con.close()

def read2(id):
    con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = "select * from member where id = %s"
    cur.execute(sql, id)

    row = cur.fetchone()
    # cur.fetchall() : 조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(row)
    print(type(row))
    print(row[0])

    con.close()

def read3():
    con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor(pymysql.cursors.DictCursor)
    print(cur)

    sql = "select * from member"
    cur.execute(sql)

    # row = cur.fetchone()
    rows = cur.fetchall()  # 조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(rows)
    print(type(rows))
    # print(rows[0])
    for row in rows:
        print(row)

    con.close()

def update(id, tel):
    #1. mysql과 연결
    con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
    print(con.get_host_info())

    #2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득
    cur = con.cursor()
    print(cur)

    #3. sql문을 만들어서 전송함.
    data = (tel, id)
    sql = "update member set tel = %s where id =%s"
    cur.execute(sql, data) #tuple로 넣어주어야 한다.

    #4. auto-commit이 안된다 수동으로 반영시켜야한다.
    con.commit()
    con.close()

def delete(id):

    con = pymysql.connect(host='localhost', port=3388, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'delete from member where id = "' + id + '"'
    cur.execute(sql)
    con.commit()
    con.close()
