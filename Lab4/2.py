from math import *

a = int(input())
b = int(input())
c = int(input())

if a == 0:
    print(-c/b)

else:
    d = b**2 - 4*a*c
    if d<0:
        print('Корней нет')
    elif d == 0:
        print(-b/(2*a))
    else:
        print((-b + sqrt(d))/(2*a), (-b - sqrt(d))/(2*a))
