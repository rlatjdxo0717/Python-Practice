num1 = int(input('num1 >> '))
num2 = int(input('num2 >> '))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

a = input('이름을 입력하세요 >> ')
b = int(input('나이를 입력하세요 >> '))
print(a,'는',b,'세 입니다.')
if b > 100:
    print('나이가 많으시군요!')
else:
    print('아직 어리시군요!')

hobby = "달리기"
time = 10
print(hobby,'를',time,'시간 했습니다')
if hobby == '달리기'and time >= 10:
    print('오늘',hobby,'는 충분')
else:
    print('어떤운동이든 시작하세요!!')