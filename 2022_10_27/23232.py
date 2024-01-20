
'''
# 동전 던지기 실험
# 몬테카를로 실험
import numpy as np

num_try = 10000  # 실행횟수
num_head = 0
case_toss = ['H', 'T']  # 앞면 Head H , 뒷면 Tail T (리스트로 묶기)

for i in range(num_try):
    np.random.randint(0, 2)  # 코인 던지기 (0 & 1 중 랜덤.)   or np.random.choice도 가능
    toss_coin_idx = np.random.randint(0, 2)  # 코인 던지는 변수 생성.
    coin = case_toss[toss_coin_idx]     # 코인을 던져서 나오는 면을 변수로 생성.
    if coin == 'H':
        num_head += 1

print("앞면 나온 횟수 : ", num_head)
print("총 횟수 : ", num_try)
print("앞면 나오는 확률 : ", num_head / num_try)
'''




'''
1.주사위 던져서 1,2,3,4,5,6이 나올 확률
2.주사위 2개 던질 때, 합이 6이 나올 확률
3.주사위 던져서 n이 나올 확률
'''
# 주사위에서 n이 나올 확률
import pandas as pd
import numpy as np      # numpy 불러오기

num_try_dice = 100       # 주사위를 던지는 총 횟수 설정
dice_toss = [1, 2, 3, 4, 5, 6]      # 주사위 숫자들

D_N_ONE = 0   # 주사위가 나온 횟수 설정
D_N_TWO = 0
D_N_THREE = 0
D_N_FOUR = 0
D_N_FIVE = 0
D_N_SIX = 0
D_R_N = 0

for d in range(num_try_dice):       # 주사위를 num_try_dice만큼 던진다.
    np.random.randint(0, 6)     # 랜덤 범위 지정
    toss_dice_idx = np.random.randint(0, 6)     # toss_dice_idx = 넘파이(np.)와 랜덤(random.)을 사용해 랜덤한 정수(randint범위 1~6)를 집어 넣는다.
    dice = dice_toss[toss_dice_idx]
    if dice == 1:      # 던진 숫자가 1일 때
        D_N_ONE += 1   # 넘버 원에 1을 더해라.

    elif dice == 2:      # 던진 숫자가 1일 때
        D_N_TWO += 1   # 넘버 원에 1을 더해라.

    elif dice == 3:      # 던진 숫자가 1일 때
        D_N_THREE += 1   # 넘버 원에 1을 더해라.

    elif dice == 4:      # 던진 숫자가 1일 때
        D_N_FOUR += 1   # 넘버 원에 1을 더해라.

    elif dice == 5:      # 던진 숫자가 1일 때
        D_N_FIVE += 1   # 넘버 원에 1을 더해라.

    elif dice == 6:      # 던진 숫자가 1일 때
        D_N_SIX += 1   # 넘버 원에 1을 더해라.

print('1이 나올 확률 : %s %% ' % (D_N_ONE/num_try_dice))   # if문을 통해 1이 나온 경우의 수 / 주사위를 던진 횟수
print('2가 나올 확률 : %s %% ' %(D_N_TWO/num_try_dice))
print('3이 나올 확률 : %s %% ' %(D_N_THREE/num_try_dice))
print('4가 나올 확률 : %s %% ' %(D_N_FOUR/num_try_dice))
print('5가 나올 확률 : %s %% ' %(D_N_FIVE/num_try_dice))
print('6이 나올 확률 : %s %% ' %(D_N_SIX/num_try_dice))

'''
print('1이 나온 횟수 : ',D_N_ONE)    # if문을 통해 1이 나온 경우의 수
print('2가 나온 횟수 : ',D_N_TWO)
print('3이 나온 횟수 : ',D_N_THREE)
print('4가 나온 횟수 : ',D_N_FOUR)
print('5가 나온 횟수 : ',D_N_FIVE)
print('6이 나온 횟수 : ',D_N_SIX)
'''

'''
다른 답안 :
'''
import random       # random import
print('주사위를 100회 던집니다.')

result=[0]*6
for i in range(100):
    dice=random.randint(1,6)
    result[dice-1] += 1

print('결과 : ',end='')
for idx,i in enumerate(result):
    print(idx,'-',i,'번,',end='  ')


# 주사위 2개 던져서 합이 6이 나올 확률

import numpy as np

toss_2dice = 100
dice1 = [1, 2, 3, 4, 5, 6]      # 주사위 숫자들
dice2 = [1, 2, 3, 4, 5, 6]      # 주사위 숫자들

lst = []
lst2 = []
S_dice = 0
for i in range(101):
    lst.append(np.random.randint(1, 6))
    lst2.append(np.random.randint(1, 6))

    if lst[i]+lst2[i] == 6:
        S_dice += 1


print('주사위 2개 던져서 합이 6이 나올 확률 :  ',S_dice/toss_2dice)



#random
np.random.random(10) #0~10까지 랜덤한 수들로 행렬로 만들어라 (소수 포함)
np.random.random((4,3)) *100 + 50  # '*100 + 50'은 스칼라곱을 나타냄.(np.random.random(4,3)는 에러 뜸.)
np.random.rand(10)
np.random.rand(4,3) # 랜덤과 다르게 괄호 하나 더 없어도 실행 가능.
np.random.randn(10) # 음수랑 섞어서 나옴
np.random.randn(4,3) #rand와 동일 반대로 괄호하나 더 넣으면 오류 뜸.
np.random.choice(3,5) #[0,1,2] 3개 정수 중 5개 출력
np.random.choice(3,5,p=[0.2,0.3,0.5]) # '0,1,2'에 대하여 0.2,0.3,0.5 확률 부여
np.random.choice(['dog','cat','bear','fish'],6) #문자열도 가능