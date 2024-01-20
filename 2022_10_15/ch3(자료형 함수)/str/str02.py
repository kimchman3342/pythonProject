# 문자열 연산하기 : +, *(반복)

head = 'Python'
tail = ' is fun'
str = head + tail               # str 연산 (한 번에 묶어서 편함.)
print(str)                      # Python is fun
print(head + tail)              # Python is fun (같은 결과지만 비교적 불편.)

s = 'python'
print(s * 2)                    # 2번 반복 : pythonpython ('*'는 반복을 의미.)
print(s * 3)                    # 3번 반복 : pythonpythonpython

print('='*50)                   # 50번 반복
print('My Program')
print('='*50)                   # 50번 반복 * 다른 랭귀지에선 지원이 안됨.

print('*'*1)
print('*'*2)
print('*'*3)
print('*'*4)
print('*'*5)

print('*'*5)
print('*'*4)
print('*'*3)
print('*'*2)
print('*'*1)
