#과제 1 - 반복문 for문을 이용해서 구구단(2~9단)을  각 단별로 세로로 출력하는 프로그램을 작성하세요?

gugudan = int(input('출력을 원하는 단을 입력하세요.'))  # 제목 부분 출력 빌드업 함수 (input함수 : 실행란에서 질문을 할 수 있음)
print('[', gugudan, '단]')  # 제목 부분 출력

for i in range(1, 10):  # i변수 범위지정
    print(gugudan, '*', i, '=', gugudan * i)  # input 함수에 넣은 내용 과 i 변수를 곱한 수 가 나오도록 출력

'''
Quiz 1 답안 :
각 단을 열방향으로 출력
for d in range(2,10):
    print('[',d,'단]', end='\t\t\t') # "end='\t\t\t'"는 줄을 바꾸지 않고 가로로 출력
print()
for i in range(1, 10):
    for dan in range(2, 10):
        print(dan,'*',i,'=',dan*i, end='\t\t')
    print()
'''
'''
#과제 2 - 키보드로 주민번호 13자리를 입력 받았을때 남자인지, 여자인지를 판별하는 프로그램을 작성하세요?
ex)  9501011234567

1. 주민번호는 하이픈(-) 없이 13자리를 입력한다.
2. 입력한 주민번호가 13자리가 아닌경우에 메세지를 출력한다.
3. 입력한 주민번호를 이용해서 남자, 여자를 판별해서 출력한다.
'''

r_num = input('주민번호를 입력해주세요. :')  # 주민번호 입력 물음 빌드업.
print('[',r_num,']')    # 주민번호를 괄호안에 출력

if "1" == r_num[6] or "3" == r_num[6]:  # 1 or 3은 남자 r_num을 리스트화 해서 추출하고 식별
    print('남자')
else:
    "2" == r_num[6] or "4" == r_num[6]
    print('여자')
'''
Quiz 2 답안 :
jumin = input('주민번호 13자리를 입력하세요?')

if len(jumin) != 13: # 숫자열을 strig으로 만들어 13자리가 아니면 13자리를 입력하세요를 출력하게 만듬. (첫번째 조건)
    print('13자리를 입력하세요')
elif jumin[6] == '1' or jumin[6] == '3':
    print('남자')
elif jumin[6] == '2' or jumin[6] == '4':
    print('여자')
else:   # 위의 조건이 모두 아닐경우
    print('똑바로 입력하세요')  # 1~4의 숫자가 아니면 출력됨. (두 번째 조건)
'''

#giduck23@naver.com 제출