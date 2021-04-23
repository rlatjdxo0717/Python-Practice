import db연결.mysql_bbs.bbs_dao as db

id = input("아이디를 입력하세요 : ")

db.read(id)