def exam01(exam01_id, exam01_name):
    print('아이디가',exam01_id,'인',exam01_name,'님이 로그인되었습니다.')

def exam02add(x,y):
    return x + y
def exam02minus(x,y):
    return x - y
def exam02mul(x,y):
    return x * y
def exam02div(x,y):
    return x / y
def exam02na(x,y):
    return x % y

def exam03(exam03_name,exam03_age):
    print(exam03_name,'님의 10년후의 나이는',(10 + exam03_age),'세 입니다.')

def exam05(exam05_num):
    if (exam05_num % 2 == 0):
        print('짝수입니다.')
    else:
        print('홀수입니다.')

def exam06(exam06_result):
    if (exam06_result >= 1000):
        print('축하합니다. 실적을 달성하셧습니다.!')
        print('당신의 이번달 보너스는',int(exam06_result*0.2),'만원입니다.')
    else:
        pass

def exam07(exam07_id,exam07_start,exam07_move):
    print(exam07_id,'미사일이',(exam07_start+exam07_move),'로 이동되었습니다.')

def exam08(exam08_num1,exam08_num2):
    print('받은 돈: ',exam08_num1)
    print('상품의 총액: ',exam08_num2)
    print('부가세: ',int(exam08_num2/10))
    print('받은 돈: ',(exam08_num1-exam08_num2))

def exam09():
    for i in range(1000):
        print('*',end='')