#Chapter 04-2
#FOR 실습


for v1 in range(10):
    print('v1 is : ', v1)

print()

for v2 in range(1, 11):
    print('v2 is : ', v2)

print()

for v3 in range(1, 11, 2):
    print('v3 is : ', v3)

print()

sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 Sum : ', sum1)

print('1 ~ 1000 Sum : ', sum(range(1, 1001)))

print()

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# Iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ['Kim', 'Park', 'Lee', "Cho", 'Choi', 'Yoo']

for n in names:
    print('Yor are : ', n)


lotto_numbers = [11, 19, 21, 28 ,36, 37]

for n in lotto_numbers:
    print("Current Number : ", n)


word = "Beautiful"

for s in word:
    print('word : ', s)


my_info = {
    "name" : 'Lee',
    "Age" : 33,
    "city" : "Seoul"
}

for k in my_info:
    print('key : ', k) 
'''
key :  name
key :  Age
key :  city
'''


my_info = {
    "name" : 'Lee',
    "Age" : 33,
    "city" : "Seoul"
}

for k in my_info:
    print('key : ', my_info[k])

for v in my_info.values():
    print('Value : ', v)

'''
key :  Lee
key :  33
key :  Seoul
'''

name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())


# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 4:
        print('Found : 4!')
        break
    else:
        print('not found : ', num)


# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type : ", v, type(v))

# for - else

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 55:
        print("Found : 55")
        break
else:
    print('Not Found : 55')

print()

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end ='')
    print()


name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))
