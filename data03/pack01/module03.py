# 기본형 4가지
# 정수, 실수

age = 100
weight = 99.9

sum2 = age + weight
print(sum2)

temp = input('현재 온도는 >> ') #22.2
print(type(temp))

temp2 = float(temp) #int()
print(type(temp2))

if temp2 > 20:
    print('너무 더워요')
else:
    print('아직 안더워요')

# 타입을 변경하는 것 : 형변환(casting,캐스팅)
# 문자로 변경하는 것 : str()
# 정수로 변경하는 것 : int()
# 실수로 변경하는 것 : float()

# 문자
# String을 의미, char를 포함하는 의미!
company = '성태'
print(company, end=' ') #프린트 후, 마지막에 엔터! 적용
print('우리회사는',company)

# 논리
food = True #False
food2 = 1 #0

if food == True:
    print('배가 부르시겠군요.!')
else:
    print('배가고파요!')