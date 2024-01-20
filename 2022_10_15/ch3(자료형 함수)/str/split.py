'''
split() : 문자열을 특정 구분기호로 분리 시키는 함수   * 'strip(공백제거) 함수'와 헷갈리면 안 됨.
split('구분기호')
'''

s = 'Life is too short'
result = s.split(' ')       # 공백으로 파싱(parsing)  * 파싱
print(type(result))         # <class 'list'>
print(result)               # ['Life', 'is', 'too', 'short']

s1 = 'python:java:oracle:jsp:spring:tensorflow'
result1 = s1.split(':')     # 콜론(:)으로 파싱
print(result1)              # ['python', 'java', 'oracle', 'jsp', 'spring', 'tensorflow']

for i in result1:
    print(i)        # 'result1 변수' 안의 문자열들을 세로로 하나씩 출력