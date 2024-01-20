# break 문 : 반복문을 빠져 나오는 역할

for i in range(1, 1001):            # 1 ~ 1000
    print(i,'출력')

    if i==100: # i가 100일 때 빠져나옴.
        print('루프를 빠져 나옴')
        break
