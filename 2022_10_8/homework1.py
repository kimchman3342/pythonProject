# 1주차 과제 -1 Q : 1 ~ 12월 중에서 달(Month)에 'r'이 들어있는 달(Month)을 출력하는 프로그램을 작성 하세요.

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
matching = [s for s in month_list if "r" in s]
print(matching)

# 1주차 과제 - 2 Q : 키보드로 3개의 정수를 입력 받았을때, 입력한 값 중에서 최대값과 최소값을 구하는 프로그래을 작성하세요. (단, if  else 문을 이용하세요.)

nums = [3,5,10]
print("최대값 : ", max(nums))
print("최소값 : ", min(nums))