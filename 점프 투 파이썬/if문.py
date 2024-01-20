'''
1. 변수설정 (?? = ??) * if문에 절대적인 역할을 함
2. if문에 조건 설정(반대는 else문, 항상 두 개 초과 안됨.) # if문 마지막에는 항상 '콜론(:)'이 존재
3. if문에 in을 사용하고 싶다면 s(리스트, 튜플, 문자열)로 변수 설정 (x in s)    * not in은 먼저 설정한 in에 의하여 참 거짓을 추출
4. if문과 else문 콜론 뒤 'pass'와 'print' 들여쓰기 없이 한 줄로 사용 가능
'''

# 간단 변수를 사용한
money = 1000    # 첫 번째 변수
card = True     # 두 번째 변수

if money >= 1000 or card:   # 돈이 있다면 (변수 설정이 중요)
    print("택시를 타고가라")   # 택시를 타러가라  * if문 아래 들여쓰기 필수

else:   # 거짓인 경우
    print("걸어가라")   # 걸어가라

# 리스트를 활용한 if문
pocket = ['paper','cellphone','money']  # 리스트로 변수를 생성

if 'money' in pocket:   # s가 x안에 있니? (x in s)
    print('택시를 타라')     # 만약 'pass'를 입력하게 된다면 True일 때 결과 값이 나오지 않는다.

else:
    print('걸어 가')

'''
변수 설정 후 띄어쓰기 없이 코드 작성 가능.
pocket = ['paper','cellphone','money']
if 'money' in pocket:pass
else:print("카드를 꺼내라")
'''

# elif를 활용한 if문
pocket = ['paper','cellphone']  # 리스트 변수 생성
card = True     # 일반 변수 생성

if money in pocket:
    print('택시를 타고가라')

elif card:  # 만약 else를 쓰게 되면 밑에 if문을 한 번 더 써야함.
    print('택시를 타고가라')

else:
    print('걸어 가')



# 프린트 대신 message 활용
score = 60
if score >= 60:
    message = "success"
else:
    message = "failure"

# 한 줄로 표현 가능
score = 60
message = "success" if score >= 60 else "failure"   # 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
print(message)  # print를 꼭 해줘야 함.

# 경우에 따른 if 문
a = 3
# qes = input("a는 무엇일까요?")
'''
if a == 1:
    print('a는 1이 아님')
elif == 3:
    print('정답')
elif (a>1)
    print('a는 좀 더 크다')
elif (a<1)
    print('a는 좀 더 크다')
'''

a = 3
if a == 1:
    print('"a"는 "1"이네요')
elif (a<1):
    print('"a"는 "1"보다 작네요')
    print('"a"는 ' + str(a) + '입니다.')
    print("프로그램이 끝났어요")
elif (a>1):
    print('"a"는 "1"보다 크네요')     # 크기 여부출력
    print('"a"는 ' + str(a) + '입니다.')    # a의 수 표현
