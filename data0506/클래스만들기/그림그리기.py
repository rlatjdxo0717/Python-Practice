import threading
import turtle
import random

## 클래스 선언 부분 ##
class Shape:  # 부모 클래스
    myTurtle = None
    cx, cy = 0, 0  # 사각형 및 원의 중심점.

    def __init__(self):
        self.myTurtle = turtle.Turtle('turtle')  # 거북이 생성.

    def setPen(self):  # 펜 색상과 두께를 랜덤하게 뽑기
        r = random.random()
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor((r, g, b))
        pSize = random.randrange(1, 10)
        self.myTurtle.pensize(pSize)


class Rectangle(Shape):  # 자식 클래스
    width, height = [0] * 2

    def __init__(self, x, y):
        Shape.__init__(self)
        self.cx = x
        self.cy = y
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)

    def drawShape(self):
        # 네모 그리기
        sx1, sy1, sx2, sy2 = [0] * 4  # 왼쪽 위 X, Y와 오른쪽 아래 X,Y

        sx1 = self.cx - self.width / 2
        sy1 = self.cy - self.height / 2
        sx2 = self.cx + self.width / 2
        sy2 = self.cy + self.height / 2

        self.setPen()  # 부모 클래스 메서드
        self.myTurtle.penup()
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.pendown()
        self.myTurtle.goto(sx1, sy2)
        self.myTurtle.goto(sx2, sy2)
        self.myTurtle.goto(sx2, sy1)
        self.myTurtle.goto(sx1, sy1)

class Star(Shape):
    def __init__(self, x, y):
        self.cx = x
        self.cy = y
        Shape.__init__(self)
        # self.myTurtle = turtle.Pen('turtle')

    def drawShape(self):
        self.myTurtle.penup()
        self.myTurtle.goto(self.cx, self.cy)

        self.setPen()
        self.myTurtle.pendown()
        while True:
            z = random.randrange(1, 180)
            w = random.randrange(1, 180)
            self.myTurtle.left(z)  # 왼쪽으로 90도 방향을 전환
            self.myTurtle.forward(w)  # 앞으로 쭉 진행

## 함수 선언 부분 ##
def rectThread(a):
    for x in range(100):
        print(a, '번 스레드가 시작됩니다.')
        x = random.randrange(-500, 700)
        y = random.randrange(-500, 700)
        rect = Rectangle(x, y)
        rect.drawShape()

def starThread(a):
    for x in range(100):
        print(a, '번 스레드가 시작됩니다.')

        x = random.randrange(-100, 200)
        y = random.randrange(-100, 200)
        star = Star(x, y)
        star.drawShape()

## 메인 코드 부분 ##
turtle.title('거북이로 객체지향 사각형  그리기')

thread1 = threading.Thread(target=rectThread, args=(1,))
thread2 = threading.Thread(target=starThread, args=(2,))

thread1.start()
thread2.start()

turtle.done()