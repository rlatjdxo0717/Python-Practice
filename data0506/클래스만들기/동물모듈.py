# class의 역할 : 틀의역할!
# => object : 틀을 가지고 만든 실제 대상(객체, 우리가 쓸수있는 부품의 형태)
class Dog:  # 첫글자는 대문자로
    # 멤버변수
    color = None
    field = ''

    # 생성자함수(객체생성시 자동호출되는 함수, 초기화를 담당)
    # constructor!!!
    def __init__(self, color, field):
        self.color = color
        self.field = field
        print('생성자가 호출됨.')

    # 멤버함수
    def jump(self):
        print('강아지가 점프한다.')

    def sleep(self):
        print('강아지가 잔다.')

    # 오버라이드(재정의)
    def __str__(self):
        return 'dog의 속성값들 > ' + str(self.color) + ' ,' + self.field


if __name__ == '__main__':
    dog1 = Dog('white', '진돗개')
    # dog1 => 참조형(주소) : 객체생성할 때
    #         dog1에 대한 특성을 저장하기위해 멤버변수(color, field)들이 복사
    print(dog1)
    dog1.sleep()

    dog2 = Dog('blue', '요크셔테리어')
    print(dog2)
    dog2.jump()
