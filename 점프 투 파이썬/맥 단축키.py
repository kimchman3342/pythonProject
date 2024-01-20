'''
1. 저장 : 커맨드 + s
2. 전체 실행 : shift + r
3. 개별 실행(콘솔 창) : 컨트롤 + 쉬프트 + e
4. 좌측 폴더창 : 커맨드 + 1
5. 키보드 커서 어디에 있던, 문장 한줄 바로 복사하기 : 커맨드 + c
6. 키보드 커서 어디에 있던, 문장 한 줄 삭제 : 커맨드 + Backspace

변수 설정은 숫자, 문자열, 리스트 중 하나 골라서 사용.
'''
a = 'life is too short, you need python'
if 'wife' in a:print('wife')        # 와이프란 단어가 있으면 'wife'를 출력해라
elif 'python' in a and 'you' not in a: print('python')      # 파이썬이란 단어가 있고 너라는 단어가 없으면 'python'을 출력해라
elif 'shirt' not in a : print('shirt')      # 'shirt'란 단어가 없으면 'shirt'를 출력해라
else: print('none')
# 예제 1 : 평균 구하기
a = [80,75,55]
a_sum = sum(a)
print("avg : ", {a_sum/len(a)})

a = [69,49,16,46,14,35,8,68,21,22,38,42,80,27,20,68,50,19,39,
45,81,15,37,16,41,9,64,37,71,48,47,20,51,61,31,23,15,15,66,65,12,63]
result = 0
for val in a:
    result += val
print("avg : ",{result/len(a)})

a = [69,49,16,46,14,35,8,68,21,22,38,42,80,27,20,68,50,19,39,
45,81,15,37,16,41,9,64,37,71,48,47,20,51,61,31,23,15,15,66,65,12,63]

result = sum(a)     # 가장 간단한 함수
print("avg : ",{result/len(a)})

# 예제 2 :주민번호 슬라이싱

jumin = "881120-1068234"    # 문자열로 변수 만들기
yyyymmdd = jumin[:6]        # 처음부터 6번째 인덱스 번호까지 (헷갈리면 중간에 run)
num = jumin[7:]             # 7번째 인덱스 번호부터 끝까지
print(yyyymmdd)
print(num)

# 예제 3 : replace 함수
a = "a:b:c:d"
b = a.replace(":","#")  # 대치될 값, 대치할 값
print(b)

# 예제 4 : 리스트 정렬
a = [1,3,5,4,2]
a.sort(reverse=True)   # 아래에 a.reverse를 출력해도 같은 결과
print(a)

# 
a = 0
b = a % 3
while a < 1000:
    a = a + 1
print(a)

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

