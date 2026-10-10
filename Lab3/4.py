a = int(input())

k1 = a//100 + a%10
k2 = (a//100) * (a%10)

a = a - (a//100)*100

print(k1 + a//10, k2 * (a//10))
