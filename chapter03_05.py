# Chapter03-5
# 딕셔너리
# 덕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name' : 'Park', 'phone' : '01033337777', 'birth' : '870514'}
b = {0 : 'Hello Python'}
c = {'arr' : [1, 2, 3, 4, 5]}
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 33,
    'Gread' : 'A',
    'Status' : True

}
e = dict([
    ('Name', 'Niceman'),

])

f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True

)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력
print()
print('a - ', a['name']) # Park, 존재하지 않는 Key 값이면 에러
print('a - ', a.get('name')) # 존재하지 않는 Key 값이면 결과가 'None' 
print('b - ', b[0]) # Hello Python
print('b - ', b.get(0)) # "
print('f - ', f.get('City')) # Seoul