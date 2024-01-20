import pandas as pd
import random as rd
import numpy as np
import os
currentPath = os.getcwd()
print(currentPath)


'''
과제 1. 다음과 같은 내용의 파일 abc.txt 가 있다.
        AAA
        BBB
        CCC
        DDD
        EEE
   이 파일의 내용을 읽어와서 다음과 같이 역순으로 바꾸어 result.txt로 저장 하세요?
       EEE
       DDD
       CCC
       BBB
       AAA
'''

# 과제 1 문제풀이 : write 함수를 써서 안에 있는 값이 없어지고 새로운 값으로 대체되는 원리



file = open('abc.txt','w')
file.write('EEE\nDDD\nCCC\nBBB\nAAA\n')
print('저장 성공')

file.close()

'''
답안 
with open('abc.txt', 'r') as f:
    lines = f.readlines()
    print(lines)                # ['AAA\n', 'BBB\n', 'CCC\n', 'DDD\n', 'EEE']

lines.reverse()     # 데이터를 역순으로 바꿈.
print(lines)                    # ['EEE', 'DDD\n', 'CCC\n', 'BBB\n', 'AAA\n']

with open('result.txt', 'w') as f:  # result.txt 파일을 'f'라고 부르겠다.
    for line in lines:
        line = line.strip()     # 줄바꿈 문자(공백) 제거
        f.write(line+'\n')  # 다시 줄바꿈을 해줌
'''

'''
과제 2.  다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균값 구한 후 평균값을 result.txt 파일에 저장하는 프로그램을 작성하세요?

70
60
55
75
95
90
80
80
85
100
giduck23@naver.com 제출
'''

# 과제 2 문제풀이 : 리스트로 만들어서 접근 (하지만 끝을 내진 못했습니다.)

tfile = open('sample.txt','r')

lst = []

line = tfile.read().splitlines()
lst.append(line)
print(line)

tfile.close()

rfile = open('result.txt','w')
rfile.write('')
print('생성성공')

close = rfile


'''
답안 
with open('sample.txt', 'r') as f:
    lines = f.readlines()       # redlines() : 파일 안에 있는 데이터를 리스트로 바꾸는 함수
    print(lines)                 # ['70\n', '60\n', '55\n', '75\n', '95\n', '90\n', '80\n', '80\n', '85\n', '100']

total = 0
for line in lines:  # 반복문 생성
    total += int(line)  # '+='는 반복해서 더하라는 뜻.
avg = total / len(lines)
print('total:', total)           # total: 790
print('avg:', avg)               # avg: 79.0

with open('result.txt', 'w') as f:
    f.write(str(avg))
'''



