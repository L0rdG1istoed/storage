
a = int(input())
b = int(input())
c = int(input())

if ((a+b) > c) and ((a+c) > b) and ((c+b) > a):
    print('Да')
    if a == b == c:
        print('Равносторонний')
    elif (a == b) or (b == c) or (c == a):
        print('Равнобедренный')
    else:
        print('Разносторонний')
else:
    print('Нет')
