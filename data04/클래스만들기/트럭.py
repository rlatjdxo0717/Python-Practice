class Truck:
    weight = None
    company = None

    def move(self):
        print(self.weight,  '톤의 짐을 실어나르다.')
    def own(self):
        print(self.company, '회사 소속의 트럭입니다.')

    def __str__(self):
        return str(self.weight) + ', ' + self.company

if __name__ == '__main__':
    car2 = Truck()
    car2.weight = 1
    car2.company = 'KST'
    print(car2)
    car2.move()
    car2.own()
