# Chapter 03-4
# 튜플
# 리스트와 비교가 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) # 불변


# 선언
a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>')
print('d - ', d[1]) #1000
print('d - ', d[0] + d[1] + d[1]) #2100
print('d - ', d[-1]) #Captine
print('d - ', e[-1]) #('Ace', 'Base', 'Captine')
print('d - ', e[-1][1]) #Base
print('d - ', list(e[-1][1])) #['B', 'a', 's', 'e']

# 수정X 확인
# d[0] = 1500

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3]) #(100, 1000, 'Ace')
print('d - ', d[2:]) #('Ace', 'Base', 'Captine')
print('d - ', e[2][1:3]) #('Base', 'Captine')

# 튜플 연산
print('>>>>>')
print('c + d', c + d) #(11, 12, 13, 14, 100, 1000, 'Ace', 'Base', 'Captine')
print('c * 3', d * 3) #(100, 1000, 'Ace', 'Base', 'Captine', 100, 1000, 'Ace', 'Base', 'Captine', 100, 1000, 'Ace', 'Base', 'Captine')

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a) #(5, 2, 3, 1, 4)
print('a - ', a.index(3)) #2
print('a - ', a.count(2)) #1

# 팩킹 & 언팩킹

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

print(t)

# 언팩킹
(x1, x2, x3, x4)  = t #('foo', 'bar', 'baz', 'qux')

print(type(x1), type(x2), type(x3), type(x4)) #<class 'str'> <class 'str'> <class 'str'> <class 'str'>
print(x1, x2, x3, x4) #foo bar baz qux
