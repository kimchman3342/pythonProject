# 해답 1 : tuple
months = ("January", "February", "March", "April", "May", "June",
           "July", "August", "September", "October", "November", "December")

for month in months:  # 튜플을 month 변수에 저장
    if 'r' in month.lower(): #'.lower()'는 소문자로 바꾸는 작업을 한다.
        print(month)

for month in months:
    if month.count('r')>0:
        print(month)


# 해답 :
n1 = int(input('정수1을 입력하세요?'))
n2 = int(input('정수2을 입력하세요?'))
n3 = int(input('정수3을 입력하세요?'))

# 최대값
if n1>=n2 and n1>=n3: # n1은 n2보다 크거나 같고, n1은 n3보다 크거나 같다.
    max = n1
else:  # 아니면
    if n2>=n1 and n2>=n3:
        max = n2
    else:
        max = n3

# 최소값
if n1<=n2 and n1<=n3:
    min = n1
else:
    if n2<=n1 and n2<=n3:
        min = n2
    else:
        min = n3
print('max:', max)
print('min:', min)
