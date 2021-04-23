import db연결.mysql_bbs.bbs_dao as db

id = input('수정할 아이디를 입력하세요.')

title = input('수정할 제목을 입력하세요.')

db.update(id, title)
