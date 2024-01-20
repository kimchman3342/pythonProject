# 대입 연산자 : '='

a = 10
print('a=', a)  # a앞의 공백은 먹히지 않는다.

x = y = z = 0
print('x=', x)
print('y=', y)
print('z=', z)

c, d = 10, 20
print('c=', c)              # c= 10
print('d=', d)              # d= 20

# 값 교환
c, d = d, c
print('c=', c)              # c= 20
print('d=', d)              # d= 10
