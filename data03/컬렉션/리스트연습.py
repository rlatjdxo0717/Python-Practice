food = ['감자','양파','고구마']
food[2] = '국수'

print(food)
print("리스트의개수",len(food))
print('요소, element의 글자수',len(food[0]))

#########################
hobby = []
tour = list()
hobby.append('코딩')
hobby.append('등산')
hobby.append('독서')
hobby.append('글쓰기')
print(hobby)
print(len(hobby))
tour.append('제주도')
tour.append('울산')
tour.append('부산')
tour.append('강릉')
tour.append('강남')
print(tour)
print(len(tour))

del tour[0]
print(tour)
tour.insert(0, '수원') #append는 끝에 끼고, insert는 끼는 위치를 정할수있음
print(tour)

for x in tour:
    print(x,end=' ')
print()
for x in range(len(tour)): #0~4
    print(tour[x],end=' ')

#########################
buy = []
wish = list()
for x in range(5): #0~4
    buy.append(input())
print(buy)

data = input()
data2 = data.split(',')
print(type(data2))
for x in data2:
    print('나는',x,'가 되고 싶어요')