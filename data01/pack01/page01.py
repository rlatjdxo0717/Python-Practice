# import pack02.mysqldb
from pack02 import mysqldb

# from 을 사용하면 pack.mysqldb.create()을 pack을 빼고 사용 ㅆㄱㄴ

print('welcome')
# 주석 : ctrl + /
# 실행 : ctrl + shift + f10

mysqldb.create()
mysqldb.read()
mysqldb.update()
mysqldb.delete()

# jframe 과동일 
from tkinter import *
window = Tk()
window.mainloop()