# remove() : 리스트의 특정 원소를 삭제하는 함수
# 형식 : remove('삭제할 데이터')

a = [1, 2, 3, 1, 2, 3]
a.remove(3)                 # 첫번째로 나오는 3을 삭제
print('a:', a)              # [1, 2, 1, 2, 3]

a.remove(3)                 # 두번째로 나오는 3을 삭제
print('a:', a)              # [1, 2, 1, 2]
