def add(x,y):
    return x + y
def minus(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y

if __name__ == '__main__': # 자바에서의 main역할
    print('더한 결과 >>', add(1000, 2000))

# 메인 안에다가 써야함
# 메인 밖에다가 쓰면 실행은 되지만 다른 import하는곳에도 같이 실행됨.
