a = int(input())
b = int(input())
l = int(input())
n = int(input())

d = 2*a + b
k = not(n%2)

summ = 2*(d*(n//2) + b*(n//2) - b*k + l)
print(summ)
