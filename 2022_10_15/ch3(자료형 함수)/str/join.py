# join() : 문자열을 특정 문자열로 결합할 때 사용되는 함수   * 변수가 변수 사이사이에 들어감.

a = ','
s = 'abcd'
result = a.join(s)          # 'a 변수'를 's 변수'안에 집어넣어 'result 변수'에 리턴함.
print('result:', result)            # a,b,c,d

b = '_'
list = ['사과','배','포도','수박','키위','바나나']
result1 = b.join(list)
print(type(result1))                # <class 'str'>
print('result1:', result1)          # 사과_배_포도_수박_키위_바나나



