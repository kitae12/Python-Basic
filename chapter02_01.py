#파이썬 변수

#기본 선언
n = 700

#출력
print(n)
print(type(n))

#동시선언
x = y = z = 700
print(x, y, z)

#선언
var = 75

#재선언
var = 'Change Value'

#출력
print(var)
print(type(var))
print()
#Object Reference
#변수 값 할당 상태

#id(identity)확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

#같은 오브젝트를 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

#다양한 변수 선언 방법
#CameL Case : numberOfCollegeGraduates -> Method
#Pascal Case : NumberOfCollegeGraduates ->Class
#Snake Case : number_of_college_graduates

#허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age = 7
age_ = 8
_AGE_ = 9

#예약어는 변수명으로 불가능
