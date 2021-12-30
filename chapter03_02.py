# Chapter 03-02
# 파이썬 문자형

# 빈 문자열
str1 = ''
str2 = str()

print(type(str1), len(str1))
print(type(str2), len(str2))

# 이스케이프 문자 사용
'''
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
'''

print("I'm Boy")
print('I\'m boy')

print('a \t b')
print('a \nb')
print('a \" b')

escape_str1 = "do you have a \"retro games\"?"
print(escape_str1)

escape_str2 = 'what\'s on tv?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "click \t\t strat!"
t_s2 = "new line \n\n check!"

print(t_s1)
print(t_s2)
print()

# raw string 출력('앞 r)
# 이스케이프 문자 무시(\t)
raw_s = r'D:\pytion\test'

print(raw_s)
print()

# 멀티 라인 입력
# 역슬래쉬 사용
multi_str = \
'''
string
multi line
test
'''

print(multi_str)


# 문자열 연산
str_o1 = 'python'
str_o2 = 'apple'
str_o3 = 'how are you doing'
str_o4 = 'seoul daejeon busan jinju'

print(str_o1 *3)
print(str_o1 + str_o2)
print('y' in str_o1) #시퀀스
print('p' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, iaslnum, startswith, count, endswith, isalpha...)
print('Capitalize :', str_o1.capitalize()) # 문자열 첫번째 자리를 대문자로 변환
print('endswith? : ', str_o2.endswith('e')) # 문자열 끝자리가 해당 문자로 끝나는지
print('replace :', str_o1.replace('thon', 'good')) # a문자열을 b문자로 변환
print('sorted :', sorted(str_o2)) # 리스트 형태로 정렬
print('split :', str_o4 .split(' ')) # 문자 분리

# 반복(시퀀스)
im_str = 'good boy!'

print(dir(im_str)) # __iter__

# 출력
for i in im_str:
    print(i)
    print()

# 슬라이싱
str_sk = 'nice python'

# 슬라이싱 연습
print(str_sk[0:3]) # 0 1 2
print(str_sk[5:]) # =[5:11]
print(str_sk[:len(str_sk)]) # =str_sk[:11]
print(str_sk[:len(str_sk)-1]) # =str_sk[:10]
print(str_sk[1:9:2]) # 1~9번째 문자중 2칸씩
print(str_sk[-5:])
print(str_sk[1:-2])
print(str_sk[::2])
print(str_sk[::-1])
print()
# 아스키 코드
a = 'z'

print(ord(a))
print(chr(122))