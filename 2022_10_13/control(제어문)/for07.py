'''
반복문 : for문

구구단 2~9단 까지 출력하는 프로그램 작성  2022.10.13 과제
'''

for dan in range(2, 10):                    # 2 ~ 9 * 단을 처리하기 위한 'for문'
    # print('[',dan,'단 ]') *아래와 다른 방법
    print('[ {}단 ]'.format(dan))
    for i in range(1, 10):                  # 1 ~9  * 곱해질 숫자를 처리하기 위한 'for문'
        # print(dan, '*', i, '=', dan*i)  *아래와 다른 방법
        print('{0} * {1} = {2}'.format(dan, i, dan*i))
    print()