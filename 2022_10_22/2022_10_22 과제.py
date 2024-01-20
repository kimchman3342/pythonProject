'''
과제.
random모듈을 이용해서 1~ 45 사이의 값 중에서 6개의 숫자를 추출하는 로또 프로그램을 작성하세요?
조건.
1.발생된 난수 6개의 숫자는 서로중복되지 않도록 한다.
2. 발생된 난수 6개의 숫자는 오름차순으로 정렬해서 출력한다.
     giduck23@nave.com 제출
'''



# 해답
import random

lot = []                           # 비어있는 리스트

'''
lot.append(random.randint(1,45))
lot.append(random.randint(1,45))
print(lot)
'''

while True:
    r = random.randint(1,45)       # 1 ~ 45 사이의 난수 발생
    if r not in lot:               # 발생된 난수가 list에 없으면 추가
        lot.append(r)
        if len(lot) == 6:          # list 에 6개의 난수가 저장되면
            break                  # 무한루프를 빠져나옴

print(sorted(lot))                 # list 를 오름차순으로 정렬해서 출력