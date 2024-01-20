# run 하려면 상단에 파일확인 한 뒤 해당 파일이면 : alt + shift + x
# 해당 파일 확인 안하고 런 : ctrl + shift + f10
# 이클립스 단축키로 실행 : ctrl + F11X
# 개별 실행('pytone console'로 연결 : ctrl + alt + E
# 한 번에 주석을 하고 싶다면 'ctrl + /' 특정 구역(블럭) 주석화는 """(쌍따옴표 3개) or '''(따옴표 3개)
# 한줄 복사 : ctrl + alt + 아래 방향키
# 한줄 삭제 : ctrl + d
# 구조적 프로그래밍 언어의 대부분은 명령어가 존재(들여쓰기 사용) but, 파이썬은 이러한 명령어가 없다. (들여쓰기를 통한 구분)
# 반디집 압축을 통하여 파이썬 코드가 담겨있는 py파일을 바로 가져올 수 있음.
# 파이썬 식별자는 변수, 함수, 모듈, 클래스 또는 객체를 식별하는데 사용되는 이름


print(10+20)
print('처음 작성하는 파이썬 프로그램')
print("처음 작성하는 파이썬 프로그램") #''나 ""은 같음. (ex- 'hello' == "hello")
print('자바');     print('파이썬')   # 중간에 세미콜론을 찍지 않으면 코드가 실행이 안됨

# 기본적인 연산
sum=0
for i in range(1,11):
    sum+=i
print(sum)


#  python의 예약어 목록

import keyword

print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
#  'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
#  'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 변수(variavle) : 메모리상에 데이터를 저장하기 위한 기억공간의 이름
# 변수 만드는 형식 :   변수명 = 값(데이터)

# 정수형 변수
i = 10
print('i=', i)
print(type(i))                      # <class 'int'>

# 실수형 변수
r = 3.14
print('r=', r)
print(type(r))                      # <class 'float'>

# 복소수형 변수 (자주쓰지는 않음)
c = 3 + 5j
print('c=', c)
print(type(c))                      # <class 'complex'>

# 논리형 변수
b1 = True                           # 첫 캐릭터를 대문자로 작성
b2 = False
print('b1=', b1)
print('b2=', b2)
print(type(b1))                     # <class 'bool'>
print(type(b2))

# 문자형 변수
s1 = "파이썬"
s2 = 'python'
print('s1=', s1)
print('s2=', s2)
print(type(s1))                     # <class 'str'>
print(type(s2))

# 리스트(list)
list = ['빨강','주황','노랑','초록','파랑','남색','보라']
print(list[0])                      #  인덱싱 : 빨강
list[0] = 'red'                     # 빨강을 red 로 수정
print('list=', list)                # ['red', '주황', '노랑', '초록', '파랑', '남색', '보라']
print(type(list))                   # <class 'list'>

# 튜플(tuple) 리스트와 다르게 수정이 불가능.
t = ('red','orange','yellow','green','blue','navy','purple')
print(t[0])                         # 인덱싱 : red
# t[0] = '빨강'                     # tuple 은 원소의 값을 수정할 수 없다.
print('t=', t)                      #  t= ('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple')
print(type(t))                      # <class 'tuple'>

# 집합(set)
s = set([1, 2, 3])
print('s=', s)                      # s= {1, 2, 3}
print(type(s))                      # <class 'set'>

# 딕셔너리(dictionary) : { 'key' : 'value' }
d = {'네이버' : 'http://www.nave.com',
     '구글' : 'http://www.google.com',
     '애플' : 'http://www.apple.com'}
print('d=', d)
print(type(d))                      # <class 'dict'>