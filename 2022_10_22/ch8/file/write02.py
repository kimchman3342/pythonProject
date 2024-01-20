'''
파일 쓰기(파일 생성) : writelines() 함수
writelines() : 리스트의 내용을 읽어와서 파일로 저장하는 역할
'''

lines = ['안녕 하세요\n', 'Hello\n', 'Good Morning\n','심심하다\n']   # 공백 가능, '\n'빼면 같은 줄에 쓰기 가능.

with open('../data/greetings.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines)
    print('저장 성공')


