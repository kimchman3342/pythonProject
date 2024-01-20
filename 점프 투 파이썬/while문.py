'''
# 반복을 위한 제어문
 1. True 입력 후, 조건 연산 & if문 사용 가능.
 2. while문 빠져나가기 (값이 거짓일 경우, break문을 사용할 경우)


'''

# 나무찍기 예제(%d번 반복)
treeHit = 0     # 나무를 찍은 횟수
while treeHit < 10:      # 10번이 안되게 나무 찍는걸 반복해라. (끝에 콜론(:) 무조건 붙여야 함.) * 제어문에 대문자 섞으면 안됨.
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)       # %d는 어떠한 정수를 표시할 때 사용.
    if treeHit == 10:       # while문 특성상 거짓이면 종료  (10<10은 거짓)
        print("나무 넘어갑니다.")

# break문으로 멈추기
a = 0
b = 1
while True:     # while문 참 조건 설정.
    a = a + b   # 기본적으로 a + b 계속반복
    b = b + 1   # b는 반복할 때 마다 1씩 증가. (a는 그대로)
    if b > 4:   # 만약 b가 4보다 커지면 (결국 a는 1+2+3+4가 됨.)
        break   # while문을 멈추는 break문
print(a)

# 1부터 10까지 더하기
i = 0
total = 0

while i < 10:   # i가 10보다 아래일 동안만
    i = i + 1
    total = total + i       # total += i(같은 결과) *오타 났거나 변수에 대한 생각을 줄일 수 있음.

print(total)

# if문과 else과 같이
i = 0
total = 0
while True:
    if i < 10:      # i가 10보다 작은 동안
        i += 1      # i에 1씩 증가하며
        total += i   # total에 i를 증가 시킨다.
    else:
        break

print(total)


# while문 만들기 (리스트를 만들고 거짓으로 빠져나가기)
prompt = """
        1. Add
        2. Del
        3. List
        4. Quit
Enter number: """

number = 0
while number != 4:   # != : 같지 않다. (4를 거짓으로 만들어서 while문을 빠져나감.)
    print(prompt)
    number = int(input())

# 재고관리
coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee = coffee - 1     # 커피는 커피 - 1
    print("남은 커피의 양은 %d 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 팔렸으니 판매 중지")
        break

# 재고관리 2
coffee = 10
while True:
    money = int(input("돈을 넣어주세요 : "))       # input으로 넣은 수를 int 함수로 정수만 나오게끔 만든다.
    if money == 300:        # 커피 값은 300원
        print("커피를 줍니다.")
        coffee = coffee - 1

    elif money > 300:       # 300원보다 많이 줬을 때
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))       # 입력한 수에서 300을 뺀 수 출력.
        coffee = coffee - 1

    else:
        print("돈을 돌려주고 커피를 주지 않습니다.")   # 위의 두 조건이 아닐경우(300원보다 적게 줬을 때.)
        print("남은 커피의 양은 %d개 입니다."% coffee)

    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# while로 리스트 반복
i = 0
ani = ['사자', '호랑이', '늑대']

while i < 10:
    i = i + 1
    print(i)
    if i < 11:
        print(ani)


# 무한루프
while True:     # 참 일동안 계속
    print("Ctrl + C를 눌러야 while문을 빠져나갈 수 있습니다.")
