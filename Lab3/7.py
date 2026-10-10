h = int(input())
m = int(input())
s = int(input())
h1 = int(input())
m1 = int(input())
s1 = int(input())

r = h * 3600 + m * 60 + s
r1 = h1 * 3600 + m1 * 60 + s1

h = r1 - r

print(h // 3600,'ч',(h%3600) // 60,'м', h%60,'с')
