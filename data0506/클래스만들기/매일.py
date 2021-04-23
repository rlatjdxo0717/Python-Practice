class Day:
    doing = None
    time = 0
    location = None
    count = 0

    def __init__(self, doing, time, location):
        self.doing = doing
        self.time = time
        self.location = location

    def study(self):
        return self.doing + '를 ' + str(self.time) + '시간 하다.'

    def where(self):
        return self.location + '에서 ' + self.doing + "를 하다."

    def __str__(self):
        return self.doing + ' ' + str(self.time) + ' ' + self.location

if __name__ == '__main__':
    day1 = Day('정처기공부', 10, '서울')
    day2 = Day('파이썬공부', 11, '경기')
    day3 = Day('DB공부', 12, '부산')

    print(day1)
    print(day2)
    print(day3)

    print(day1.study())
    where_value = day1.where()
    print(where_value)