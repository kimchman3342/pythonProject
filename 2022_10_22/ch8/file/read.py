'''
 data/test.txt 파일 읽기 :  read() 함수
 read() : 텍스트 파일의 모든 내용을 읽어와서 문자형 리턴
 - 'r' : 기본값으로 정해져 있으며 파일을 읽기 위한 옵션 입니다.
 - 'w' : 쓰기모드이며 파일에 내용을 쓸 때 사용하는 옵션 입니다. 만약 이미 파일이 존재하면 커서를 맨 앞으로 돌리면서 뒤에 내용을 다 잘라내기 때문에 내용이 사라질 수 있습니다. 파일이 존재하지 않는다면 새롭게 파일을 생성합니다.- 'a' : 쓰기모드이며 파일에 내용을 쓸 때 사용하는 옵션입니다. w 옵션과는 달리 이미 파일이 존재하면 그 파일의 끝에 커서가 존재하고, 그 뒤에 이어쓰기가 가능합니다. 즉, 파일 내용을 잘라내지 않고 이어서 쓸 수 있습니다.
 - 'x' : 파일이 없으면 파일을 생성하고 쓰기모드로 열립니다. 만약 파일이 있으면 에러를 발생시킵니다.
 - 'b' : 바이너리 모드 입니다.
 - 't' : 텍스트 모드 입니다. (기본값)

'''

# 1. 읽기모드로 test.txt 파일 열기 : 상대경로

import pandas as pd
import os
currentPath = os.getcwd()
print(currentPath)

file = open('../data/test.txt', 'r', encoding= 'cp949')  # encoding 안맞으면 오류 남. (ANSI로 되어있을 땐 cp949로 해야함.)

# 읽기모드로 test.txt 파일 열기 : 절대경로
# file = open('C:/Users/user/PycharmProjects/python3/src/2020_11_30/data/test.txt', 'r', encoding='utf-8')

# 2. test.txt 파일의 모든 내용을 읽어와서 str 변수에 저장
str = file.read()
print(type(str))            # <class 'str'>
print(str)

# 3. 파일 닫기
file.close()

