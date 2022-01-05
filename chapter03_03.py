# chapter03-3
# 파이썬 리스트
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] #Len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d) #<class 'list'> [1000, 10000, 'Ace', 'Base', 'Captine']
print('d - ', d[1]) #10000
print('d - ', d[0] + d[1] + d[1]) #21000
print('d - ', d[-1]) #Captine
print('d - ', d[-1][0]) #C
print('d - ', e[-1][1]) #Base
print('d - ', list(e[-1][1])) #['B', 'a', 's', 'e']

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3]) #[1000, 10000, 'Ace']
print('d - ', d[2:]) #['Ace', 'Base', 'Captine']
print('e - ', e[-1][1:3]) #['Base', 'Captine']

# 리스트 연산
print('>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 값 비교
print(c == c[ :3] + c[3: ]) #True
print()

# ID, 동일한 id 값을 갖는다
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c) #[4, 75, 80, 85]
c[1:2] = ['a', 'b', 'c'] # [4, 'a', 'b', 'c', 80, 85], [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c'] # [4, ['a', 'b', 'c'], 80, 85]
print('c - ', c)
c[1:3] = [] #[4, 'c', 80, 85]
print('c - ', c)
del c[2] #[4, 'c', 85]
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)

a.append(10)
print('a - ', a) #[5, 2, 3, 1, 4, 10]

a.sort()
print('a - ', a) #[1, 2, 3, 4, 5, 10]

a.reverse()
print('a - ', a) #[10, 5, 4, 3, 2, 1]
print('a - ', a.index(3), a[3]) #3 3

a.insert(2, 7)
print('a - ', a) #[10, 5, 7, 4, 3, 2, 1]

a.remove(10)
print('a - ', a) #[5, 7, 4, 3, 2, 1]

print('a - ', a.pop()) #1, pop = lifo / Queue = fifo
print('a - ', a) #[5, 7, 4, 3, 2]

print('a - ', a.count(4)) #1 = 4의 개수


ex = [8, 9]
a.extend(ex)
print('a - ', a) #[5, 7, 4, 3, 2, 8, 9]