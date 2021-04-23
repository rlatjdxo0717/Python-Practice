from 함수정의.문제함수 import *

# 문제1 : exam01()
exam01_id = input('아이디를 입력하세요 >> ')
exam01_name = input('이름을 입력하세요 >> ')
exam01(exam01_id,exam01_name)

# 문제2 : exam02()
data1 = int(input('숫자1 >>'))
data2 = int(input('숫자2 >>'))

exam02_result1 = exam02add(data1,data2)
exam02_result2 = exam02minus(data1,data2)
exam02_result3 = exam02mul(data1,data2)
exam02_result4 = exam02div(data1,data2)
exam02_result5 = exam02na(data1,data2)

print('두 수의 합은', exam02_result1)
print('두 수의 차는', exam02_result2)
print('두 수의 곱은', exam02_result3)
print('두 수의 나눗셈은', exam02_result4)
print('나누고나서의 나머지는', exam02_result5)

# 문제3 : exam03()
exam03_name = input('이름을 입력하세요 >> ')
exam03_age = int(input('나이를 입력하세요 >> '))
exam03_result = exam03(exam03_name,exam03_age)

# 문제4 : exam04()
exam04_result = int(input('엄마 용돈 주세요: '))

if exam04_result > 10000:
    print('엄마 너무 용돈이 많아요.')
else:
    print('엄마 너무 용돈이 적어요.')
# 문제5 : exam05()
exam05_num = int(input('숫자를 입력하세요 >> '))
exam05(exam05_num)
# 문제6 : exam06()
exam06_result = int(input('실적을 입력하세요 >> '))
exam06(exam06_result)
# 문제7 : exam07()
exam07_id = input('미사일 이름은 : ')
exam07_start = int(input('미사일 시작값은 : '))
exam07_move = float(input('미사일 움직이는 값은 : '))
exam07(exam07_id,exam07_start,exam07_move)
# 문제8 : exam08()
exam08_num1 = int(input('받은 돈을 입력하세요 : '))
exam08_num2 = int(input('상품의 총액을 입력하세요 : '))
exam08(exam08_num1,exam08_num2)
# 문제9 : exam09()
exam09()