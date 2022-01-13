# Chapter03-6
# 집합 특징
# 집합 자료형(순서x, 중복x)


# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)

# 튜플 변환 
t = tuple(b)
print(type(t), t) # (1, 2, 3, 4)

# 리스트 변환
l = list(c)
l2 = list(e)

print(l) # [1, 4, 5, 6]
print(l2) # ['qux', 'bar', 'foo', 'baz']

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print('s1 & s2 : ', s1 & s2) # s1 & s2 :  {4, 5, 6}
print('s1 & s2 : ', s1.intersection(s2)) 

# 합집합
print('s1 | s2 :', s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('s1 | s2 :', s1.union(s2))

# 차집합
print('s1 - s2 :', s1-s2) # {1, 2, 3}
print('s1 - s2 :', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 :', s1.isdisjoint(s2)) # False

# 부분 집합 확인
print(s1.issubset(s2)) # False
print(s1.issuperset(s2)) # False

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print(s1)

s1.remove(2) # 존재하지 않는 값이면 에러
print(s1)

s1.discard(3) # 존재하지 않는 값이여도 에러x
print(s1)

s1.clear()
print(s1)