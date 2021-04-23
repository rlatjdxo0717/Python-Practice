# 기본 라이브러리(표준 라이브러리)
import math
import random

print(math.sqrt(9.0))
print(random.randint(1, 100)) # 1~99까지의 랜덤값 출력

# 연산자
# 산술, 대입, 비교, 논리

# 산술연산자
x = 100
y = 333
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y) #나머지
print(x // y) #정수부분만 추출!

# 대입연산자(=할당연산자)
# 파이썬에서는 변수의 생성과 타입이
# 값을 대입할 때 결정된다.
# auto-typing!

#비교연산자 => 비교의 결과가 논리형

print(x == y)
print(x != y)

a = 10
a *= 10 #a = a * 10
print(a)

# 논리연산자 : and, or, not
id = 'root'
pw = '1234'

print(id == 'root' and pw == '1234')
print(id == 'root' or pw == '5678')

# 멤버쉽 연산자 : in(~안에)
member = ['이성태','김성태','정성태']
print('이성태' in member)
print('이성태' not in member)