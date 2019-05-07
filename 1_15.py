# #day1
# import turtle
#
# turtle.pensize(4)
# turtle.pencolor('red')
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.mainloop()


# day2
# a = int(input('a='))
# b = int(input('b='))
#
# print('%d + %d = %d' % (a,b,a+b))
#
# a = 100
# b = 12.345
# c = 1+5j
# d = 'hello'
# e = True
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
#
# import math
#
# redius = float(input("qing shu ru banjing:"))
# perimeter = 2 * math.pi * redius
# area = math.pi * redius * redius
# print('zhouchang: %.2f'%(perimeter))
# print('mianji: %2f'%(area))
#
# year = int(input('year is'))
# is_leap = (year % 4 == 0 and year % 100 != 0 or
#            year % 400 == 0)
# print(is_leap)


#day3

# username = input('username: ')
# password = input('password: ')
#
# if username == 'admin' and password == '123456':
#     print('succussful')
# else:
#     print('failed')


# x = float(input('x = '))
# if x > 1:
#     y = x * 3 - 5
# else:
#     if x >= -1:
#         y = x+2
#     else:
#         y = 5 * x + 3
# print('f(%.2f) = %.2f' %(x,y))

# import math

# a = float(input('a= '))
# b = float(input('b= '))
# c = float(input('c= '))
#
# if a + b > c and a + c > b and b + c > a:
#     print('zhouchang: %f' %(a + b + c))
# else:
#     print('cannot')


# day4

# sum = 0
# for x in range(101):
#     sum += x
# print(sum)

# sum = 0
# for i in range(1,100,2):
#     sum += i
# print(sum)

# import random
#
# answer = random.randint(1,100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('input: '))
#     if number < answer:
#         print('bigger')
#     elif number > answer:
#         print('smaller')
#     else:
#         print('right')
#         break
# print('caile  %d ci' % counter)

# from math import sqrt
#
# num = int(input('num; '))
# end = int(sqrt(num))
# is_primer = True
#
# for x in range(2,end+1):
#     if num % x == 0:
#         is_primer = False
#         break
# if is_primer and num != 1:
#     print('No')
# else:
#     print('YES')

# x = int(input('x = '))
# y = int(input('y = '))
#
# if x > y:
#     x,y = y,x
# for factor in range(x,0,-1):
#     if x % factor == 0 or y % factor == 0:
#         print(factor)
#         print(x*y)
#         break

# row = int(input('请输入行数: '))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end='')
#     print()
#
#
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()
#
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()