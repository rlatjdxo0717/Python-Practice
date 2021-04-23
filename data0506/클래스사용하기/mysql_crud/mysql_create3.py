import db연결.mysql연결모듈 as db

data1 = ("data1", "data1", "data1", "data1")
data2 = ("data2", "data2", "data2", "data2")
datas = (data1,data2)
print('입력된 데이터들',datas)
db.create3(datas)
