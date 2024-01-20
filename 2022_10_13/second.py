#  내장 함수

# 최대값 : max()    *ps.JAVA는 프로그램을 사용하지 않는다면 매개변수를 2개까지만 넣을 수 있다.
print(max(10, 20))                  # 20
print(max(10, 20, 30, 40, 50))      # 50
print(max([10, 20, 30, 40, 50]))    # 50
print(max('hello world'))           # w

# 최소값 : min()
print(min(10, 20, 30, 40, 50))      # 10
print(min([10, 20, 30]))            # 10

'''
range() 함수 : 매개변수 개수에 따라 달라짐. (렌지 최종값 -1)
range(초기값, 최종값, 증감값) : 초기값(정확) ~ 최종값-1 까지 증감
range(초기값, 최종값) : 초기값(정확) ~ 최종값-1 까지 1씩 증가
range(최종값) : 0 ~ 최종값-1 까지 1씩 증가
'''
print(range(10))              # range(0, 10)

print(list(range(10)))        # 0 ~ 9  : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  * range 함수에 list함수를 섞으면 대괄호가 나타남
print(list(range(1,10)))      # 1 ~ 9  : [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,2)))    # [1, 3, 5, 7, 9]

for i in range(1, 11):        # 1 ~ 10   * for i in 을 사용하면 값이 하나씩 출력 됨. ('print(i)'가 한 개씩 출력)
    print(i)                  # 들여쓰기 무조건 해줘야 함.

for i in range(10):           # 0 ~ 9 *
    print(i)

for i in range(10, 1, -1):    # 10 ~ 2까지 1씩 감소  * 내림차순으로 갈 때 최종값은 '최종 값 + 1'
    print(i)

'''
내장 함수 : input(), int(), type()
input() : 키보드로 입력을 받는 경우에 사용하는 내장함수
int() : 문자형 데이터를 정수형으로 변환해주는 내장함수
type() : 변수에 저장된 데이터의 자료형을 구해주는 내장함수
'''
name = input('이름을 입력 하세요?')
age = int(input('나이를 입력 하세요?'))
print(type(name))                  # <class 'str'>
print(type(age))                   # <class 'int'>

if age >= 20: # 20살 이상일 경우
    print('성인 입니다.') # '성인 입니다.' 출력
else:          #아니라면
    print('미성년 입니다.')


# 내장 함수 : print()

print(1, 2)
print(3, 4)

# 한줄에 2개 이상의 명령을 사용할 경우에는 세미콜론(;)을 붙여야 한다.
print(1, 2);     print(3, 4)

# 출력할 때 줄을 바꾸지 않으려면 print()함수 안에 end=''(""도 가능)를 추가하면 된다.  * 따옴표 안에 공백은 한 줄 안에 출력되는 간격을 조절한다.
print(1, 2, end=' ');     print(3, 4)

# 값 사이의 간격은 sep='\t' 를 추가  *sep(seperated)
print(1,2,3,4,5)                # 1 2 3 4 5
print(1,2,3,4,5, sep='  ')      # 1  2  3  4  5
print(1,2,3,4,5, sep='\t')      # 1	 2	 3	 4   5
print(1,2,3,4,5, sep='\t\t')    # 1		2		3		4		5

# 내장 함수 : format()

# format(데이터, 서식형식)
print(4)
print(format(4, '10d'))          # 정수를 출력하는 10자리수를 만듬   *d(deciaml)
print(format(4.3, '10.3f'))      # 실수를 출력하는 전체 10자리, 소숫점 이하 3자리  *f(fraction)
print(format(42.195678,  '.3f')) # 소숫점 3자리까지 출력 : 42.196
print(format('안녕하세요', 's'))   # s(string) 문자열

# {숫자}와 format()함수를 이용한 데이터 매핑
print('{0} is {1}'.format('Python', 'fun'))     # Python is fun     * 파이썬은 0번 자리, fun은 1번 자리.
print('{} is {}'.format('Python', 'fun'))       # Python is fun     * 공백도 위와 동일한 결과 출력
print('{1} is {0}'.format('Python', 'fun'))     # fun is Python     * 번호수를 바꾸면 출력 순서가 바뀐다.

# 키보드로 입력한 문자를 format()함수로 출력  *변수를 input 함수로 묶어주고, 값을 입력하면 fomat함수에서 설정한대로 출력
name = input('이름을 입력하세요?')
job = input('직업을 입력하세요?')

print('{0} is a {1}'.format(name, job))     # 홍길동 is a 프로그래머
print('{} is a {}'.format(name, job))       # 홍길동 is a 프로그래머
print('{1} is a {0}'.format(name, job))     # 프로그래머 is a 홍길동
print('{j} is a {n}'.format(n=name, j=job)) # 프로그래머 is a 홍길동    *괄호 안에 문자가 들어가게 되면 변수에 문자를 표시해줘야 함.