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