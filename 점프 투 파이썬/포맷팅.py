'''
* '%' 사용 포매팅 : 프린트 할 필요 없이 출력
1. 문자열 안에 값을 삽입할 때 사용
2. print 괄호 안에 쉼표가 안들어 감.
3. 숫자 대입(%d), 모든 형태 문자열 대입(%s)
4. 문자열 대입은 따옴표 o, 변수 대입은 따옴표 x
5. %를 따로 출력하고 싶다면 '%%'이렇게 써야함.
6. 변수 간 연산을 삽입 하고 싶다면 % 뒤에 괄호처리
'''
# 숫자 대입(%d)
"i eat %d apples." % 3

# 문자열 대입(%s)
print("i eat %s apples." % 'five')   # 변수 설정을 제외하고 문자는 반드시 따옴표를 붙여줘야 함.

# 숫자를 나타내는 변수 대입
num = 3
print("i eat %s apples" % num)

# 2개 이상 값 넣기(숫자와 문자열 혼합.)
number = 10
day = "three"
print("i ate %s apples. so i was sick for %s days." % (number,day))

# 정렬과 공백(%공백할크기s) * '-'는 왼쪽으로 정렬.
print("%10s"% "hi")   # 인덱스 번호 9개 뒤

# 소수점 (% 소수점 자리수f)
print("%0.4f" % 0.434241)   # 소수점 4자리 까지 출력.
print("%0.6s" % 0.434241)   # %s를 사용할 경우 소수점 자리수 -2 가 됨.
print("%10.6s" % 0.434241)   #(또한 소수점 앞에 정수를 넣으면 위와 같이 공백처리)

'''
format 함수 사용 포매팅 (print 해줘야 함)
1. '%'대신 '.format()'을 사용
2. 따옴표 안에는 중괄호({변수인덱스 번호}) 사용
3. 변수 순서대로 번호 기입.(0)부터 시작.
4. %와 다르게 문자열 타입 안따짐.
'''
# 기본 함수 포매팅
print("i eat {0} apples.".format(3))

# 2개 이상 값 넣기
dd = 10
ddy = "three"
print("i eat {0} apples. so i was sick for {1} days.".format(dd,ddy))

# 이름으로 넣기
print("i eat {aaa} apples. so i was sick for {aay} days.".format(aaa = 10,aay = "three"))

# 값 이랑 혼용해서 넣기
print("i eat {0} apples. so i was sick for {aay} days.".format(10,aay = "three"))

# 정렬
print("{0:<10}".format("hi"))   # 왼쪽 정렬 :(<)
print("byung hoon{0:>4}".format("hi")) # 오른쪽 정렬 : (>)   * 문자도 혼용 가능.
print("{0:^10}".format("hi")) # 오른쪽 정렬 : (>)   * 문자도 혼용 가능.

# 공백 채우기
print("{0:=^10}".format(hi))     # 인덱스 번호와 정렬 가운데에 채울 값을 입력.

# 소수점 표현
y = 3.42343414
print("{0:10.4f}".format(y))