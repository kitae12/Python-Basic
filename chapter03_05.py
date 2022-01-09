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

# Key 갯수 확인
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))
print('e - ', len(e))
print('f - ', len(f))
print()

# 딕셔너리 함수
# dict_keys, dict_values, dict_items : 반복문(_iter)에서 사용 가능
print('a - ', a.keys()) # dict_keys(['name', 'phone', 'birth', 'address'])
print('a - ', list(a.keys())) # ['name', 'phone', 'birth', 'address']

print()

print('a - ', a.values()) # dict_values(['Park', '01033337777', '888888', 'seoul'])
print('a - ', list(a.values())) # ['Park', '01033337777', '888888', 'seoul']

print()

print('a - ', a.items()) # dict_items([('name', 'Park'), ('phone', '01033337777'), ('birth', '888888'), ('address', 'seoul')])
print('a - ', list(a.items())) # [('name', 'Park'), ('phone', '01033337777'), ('birth', '888888'), ('address', 'seoul')]

print()

print('a - ', a.pop('name')) # Park
print('a - ', a) # {'name': 'Park', 'phone': '01033337777', 'birth': '888888', 'address': 'seoul'}
                 # {'phone': '01033337777', 'birth': '888888', 'address': 'seoul'}

print('c - ', c.pop('arr')) # [1, 2, 3, 4, 5]
print('c - ', c) # {'arr': [1, 2, 3, 4, 5]} 
                 # {}
print()

print('f - ', f.popitem()) # ('Status', True)
print('f - ', f) # {'Name': 'Niceman', 'City': 'Seoul', 'Age': 33, 'Grade': 'A', 'Status': True}
                 # {'Name': 'Niceman', 'City': 'Seoul', 'Age': 33, 'Grade': 'A'
print('f - ', f.popitem())
print('f - ', f) # {'Name': 'Niceman', 'City': 'Seoul', 'Age': 33}

print()

print('a - ', 'birth' in a) # True
print('b - ', 'city' in b) # False



# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a) # {'name': 'Park', 'phone': '01033337777', 'birth': '870514', 'address': 'seoul'}

# 딕셔너리 수정
a['birth'] = '888888'
print('a - ', a) # {'name': 'Park', 'phone': '01033337777', 'birth': '888888', 'address': 'seoul'}

a.update(birth='999999')
print('a - ', a) # {'phone': '01033337777', 'birth': '999999', 'address': 'seoul'}

temp = {'address' : 'Busan'}
a.update(temp)
print('a - ', a) # {'phone': '01033337777', 'birth': '999999', 'address': 'Busan'}