# 반복문 : while문
# while  조건식 :
#     조건식이 참인 경우에 실행될 문장

# 1 ~ 10 까지 합을 구하는 프로그램 작성

i=1; sum=0                      # 초기값 : i는 1이고; 0을 더해라
while i <= 10:                  # 조건식
    sum += i    # 1 = 0 + 1
    # sum = sum + i * 같은결과  : i를 반복적으로 더해라
    i += 1                      # 증감식  * while에서는 보통 증감식을 사용
    # i = i + 1 * 같은결과
print('1~10까지 합:', sum)



