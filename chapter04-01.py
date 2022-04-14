# Chapter 04-1



if True:
    print('Good') # Good

if False:
    print('Bad') # 출력x

if False:
    print('Bad!')
else:
    print('Good!') # Good!



x = 15
y = 10

# 양 변이 같은 경우 참
print(x == y) # False

# 양 변이 다를 경우 참
print(x != y) # True

# 왼쪽이 클 때 참
print(x > y) # True

# 왼쪽이 크거나 캍을 때 참
print(x >= y) # True

# 오른쪽이 클 때 참
print(x < y) # False

# 오른쪽이 크거나 캍을 때 참
print(x <= y) # False

print()

city = ""
if city:
    print("You are in:", city)
else:
    print("Please enter your city")

city2 = "Seoul"
if city2:
    print("You are in:", city2)
else:
    print("Please enter your city")

print()

a = 75
b = 40
c = 10

print('and: ', a > b and b > c) # True
print('or: ', a > b or b > c) # True
print('not: ', not a > b) # False

print()

# 순서 : 산술-관계-논리

print('e1 : ', 3+12 > 7+3) # True
print('e2 : ', 5+10*3 > 7+3*20) # False
print('e3 : ', 5+10 > 3 and 7+3 == 10) # True
print('e4 : ', 5+10 > 0 and not 7+3 == 10) #False


print()

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 =='admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')


num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')


tier = 'A'
total = 30

if tier =='A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')

