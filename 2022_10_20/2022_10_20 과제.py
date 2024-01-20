'''
과제 1. filter와 lambda를 이용해서 다음 리스트 [10, -2, 3, -5, 8, -3] 에서 음수를 제거한후, 오름차순으로 정렬 시키는  프로그램을 작성하세요 ?
'''

# 답안
li = [10, -2, 3, -5, 8, -3]

result = list(filter(lambda x : x>0 , li))

# sort()함수로 오름차순 정렬
result.sort()
print(result)

# sorted()함수로 오름차순 정렬
print(sorted(result))
#'''
과제 2.다음과 같은 정보가 있는 리스트에서 나이(age)를 기준으로 오름차순으로 정렬하는 프로그램을 작성하세요?

people = [{'name': 'noah', 'age': 19},
          {'name': 'liam', 'age': 23},
          {'name': 'jacob', 'age': 9},
          {'name': 'mason', 'age': 21}]
#'''


# 답안

#방법1.
people.sort(key=lambda x: x['age'])
print(people)

# 방법2.
result = sorted(people, key=lambda x: x['age'])
print(result)

# giduck23 @ nave.com제출
