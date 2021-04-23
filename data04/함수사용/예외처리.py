try:
    me_file = open("me.txt", "r", encoding='utf-8')
    print(me_file.readline())
    lines = me_file.readlines()
    print('읽어온 내용',lines)
    print(type(lines))
    me_file.close()
except IOError: # 에러가나면 이거 나옴
    print('파일을 읽는 중 에러발생!!!!')
finally: # break안걸리고 출력됨
    print('나는 예외처리를 꼭 해줌.')

print('내가 실행이 되는가...')