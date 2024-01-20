'''
과제 1. 영어로 1 ~ 12월 정보를 가진 리스트에서 각 달을 3자리 약어로 출력하는 프로그램을
작성하세요. ( ex) January  -> Jan )	 * 슬라이싱 사용
출력 :   ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']
'''
'''
방법 1.
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
mon = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
'''


# 방법 2.
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
mon = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
s = months
mon_list = s[0:]
s2 = mon

result = mon_list.replace(mon)

'''
답안 :
1 ~ 12월을 3자리 약어로 출력하는 프로그램 작성
  ex) January  ->  Jan

months = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']

        range(12)
for i in range(len(months)):    # 0 ~ 11    * for문으로 month 변수 전체를 for문 변수 i로 변환
    months[i] = months[i][:3]   # i 는 i에서 3번째까지.    
    # print(months[i])
    # print(months[i][:3])  

print(months)
'''

'''
과제 2. 키보드를 통해서 연도(ex) 2020)를  입력 받는다. 이때 입력 받은 연도가 윤년인지 평년인지를 판별하는 프로그램을 작성하세요?

// 1년 365.242374
// 평년 = 365일 (2월달 - 28일까지)
// 윤년 = 366일 (2월달 - 29일까지)

* 윤년의 정의		*  '%  ==' 사용
1. 해당 연도를 4로 나누어 떨어지면 윤년 	
2. 그 중에서 100으로 나누어 떨어지면 윤년이 아님
3. 그 중에서 400으로 나누어 떨어지면 윤년
'''

'''
답안 : 
1년 365.242374
평년 = 365일 (2월달 - 28일까지)
윤년 = 366일 (2월달 - 29일까지)

윤년의 정의
1. 해당 연도를 4로 나누어 떨어지면 윤년
2. 그 중에서 100으로 나누어 떨어지면 윤년이 아님
3. 그 중에서 400으로 나누어 떨어지면 윤년

윤년은 4의 배수이고 100배수는 아니거나 400의 배수이면 윤년


year = int(input('원하는 연도를 입력하세요?'))

if year%400==0 or (year%4==0 and year%100!=0):
    print(year, "는 윤년입니다")
else:
    print(year, "는 평년입니다")
'''