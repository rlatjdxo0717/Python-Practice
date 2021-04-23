for x in range(1, 10):
    print(x)

for x1 in range(1, 15):
    print(x1)

for x2 in range(0, 20):
    print(x2)

for x3 in range(1, 20, 2):
    print(x3)

for x4 in range(10, 20, 5):
    print(x4)

num1 = 0
for x5 in range(10, 50, 10):
    num1 = num1 + x5
print(num1)

num2 = 1
for x6 in range(3, 30, 8):
    num2 = num2 * x6
print(num2)

food = ['감자','고구마','양파']
for f in food:
    print(f,"짱!")

for f1 in food:
    print(f1,"짱!",end='')

food2 = "감자 고구마 양파 스프 국수 라면"
food_list = food2.split()
for x in food_list:
    if x not in ['양파','국수']:
        print(x + "맛있어!", end=' ')