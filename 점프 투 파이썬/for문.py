'''
for문은 세로로 출력이 핵심.
continue와 같이 사용.
if문과 같이사용.
range와 같이 사용.
'''

# 숫자나열
for i in range(10):
    print(i)

for i in range(1,10,2):     # range(시작 수, 인덱스 갯수, 증가 수)
    print(i)

for i in range(10,1,-1):
    print(i)

# 문자열 반복은 리스트로 (range 제거)
for i in ['사자','호랑이','토끼']:
    print(i)       # 리스트를 0번째 인덱스 부터 차례대로 출력

# 튜플과 함께 사용
a = [(1,2),(3,4),(5,6)]

for (first,last) in a:
    print(first+last)

# 합격 불합격 판정    * 파이썬 파일로 저장하고 명령 프롬프트에서 실행하면 print 결과를 출력해줌.
marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# continue문과 같이 사용
marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue  # 합격 점수만 골라냄 (marks에서 조건 미달인 경우 number의 처음으로 되돌아감.)
    print("%d번 학생 축하합니다. 합격입니다." % number)

# range를 사용
marks = [90,25,67,45,80]
for number in range(len(marks)):    # marks의 크기를 통해 범위를 입력
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다." % (number+1))


# 1부터 10부터까지 더하기
add = 0
for i in range(1,11):
    add = add + i       # 1이랑 i랑 헷갈리지 않게 조심.
print(add)

# 구구단 만들기
for i in range(2,10):   # i = 2부터 9까지 대입
    for j in range(1,10):      # j = 1부터 9까지 대입  * 첫번째 for문 아래에 들어가 있는 경우는 i가 2(인덱스 번호 0)일때 j 전부 곱하고, 3(인덱스 번호 1)일때 j 전부곱하고를 반복.
        print(i*j, end=" ")     # i*j를 출력 %=    * end
    print('')

# 리스트 내포 사용하기
'''
a = [1,2,3,4,]
result = []     # 가상의 리스트 생성
for num in a :     # for 다음 a의 각 원소와 연산될 변수를 만든다.
    result.append(num*3)    # append : 앞의 리스트에 괄호 안에 들어가는 변수(or 변수 연산)을 채운다.
print(result)
요렇게 되어있는 코드를 아래와 같이 간단하게 할 수 있다.
'''

a = [1,2,3,4]
result = [num * 3 for num in a]     # 리스트 안에 for문을 내포 시킴
print(result)

# 구구단 리스트 내포
result = [x * y for x in range(2,10)    # 연산을 정해두고 변수에 각각 범위를 입력.
    for y in range(1,10)]
print(result)
