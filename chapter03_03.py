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