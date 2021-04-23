import db연결.mysql연결모듈 as db

id = input('수정할 아이디를 입력하세요.')
tel = input('수정할 연락처를 입력하세요.')

db.update(id, tel)
